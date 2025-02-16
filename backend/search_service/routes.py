from fastapi import APIRouter, HTTPException, Query
from pymongo import DESCENDING
from database.db import properties_collection
from search_service.models import SearchResponse
from search_service.typo_handler import is_levenshtein_match, is_jaro_winkler_match
from logging_service.logic import log_search
from indexing_service.redis_cache import cache_search_results, get_cached_results
from typing import Optional

router = APIRouter()

# Utility function to convert MongoDB ObjectId to string
def convert_objectid_to_str(doc):
    """Converts MongoDB ObjectId to string for API response."""
    doc["_id"] = str(doc["_id"])
    return doc

#  Route 1: Initial Search (Levenshtein Typo Handling, No Caching)
@router.get("/search/initial", response_model=SearchResponse)
async def initial_search(query: str = Query(..., title="Search Query")):
    """
    Performs a fuzzy search with typo handling using Levenshtein Distance.
    """
    all_results = list(properties_collection.find().limit(500))  # Fetch broader dataset first
    results = []

    for result in all_results:
        if any(is_levenshtein_match(query, o["owner_name"], max_distance=3) for o in result.get("owners", [])) or \
           is_levenshtein_match(query, result.get("address", ""), max_distance=3):
            results.append(result)

    if not results:
        # Retry with regex-based fuzzy matching if no Levenshtein match is found
        search_query = {
            "$or": [
                {"owners.owner_name": {"$regex": query[:3], "$options": "i"}},  # Match first 3 characters
                {"address": {"$regex": query[:3], "$options": "i"}}
            ]
        }
        results = list(properties_collection.find(search_query).sort([("last_updated", -1)]).limit(10))

    # Sort and return top 10 results
    results = sorted(results, key=lambda x: x.get("last_updated", ""), reverse=True)[:10]

    log_search(query, {"type": "initial_search"}, results)

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    return {"results": [convert_objectid_to_str(doc) for doc in results]}


#  Route 2: Optimized Search (Jaro-Winkler Typo Handling, Caching Enabled)
@router.get("/search/optimized", response_model=SearchResponse)
async def optimized_search(
    query: str = Query(..., title="Search Query"),
    property_type: Optional[str] = None,
    zoning_type: Optional[str] = None,
    mortgage_status: Optional[str] = None
):
    """
    Performs an optimized search with typo handling, improved partial matching, and caching.
    """
    all_results = list(properties_collection.find().limit(500))  # Fetch broader dataset first
    results = []

    for result in all_results:
        if any(is_jaro_winkler_match(query, o["owner_name"]) for o in result.get("owners", [])) or \
           is_jaro_winkler_match(query, result.get("address", "")):
            results.append(result)

    #  Apply additional filters for more precision
    if property_type:
        results = [r for r in results if r.get("property_features", {}).get("property_type") == property_type]
    if zoning_type:
        results = [r for r in results if r.get("zoning_info", {}).get("zoning_type") == zoning_type]
    if mortgage_status:
        results = [r for r in results if any(m.get("status") == mortgage_status for m in r.get("mortgages", []))]

    # Check Redis cache
    cache_key = f"optimized_search:{query}-{property_type or ''}-{zoning_type or ''}-{mortgage_status or ''}"
    cached_results = get_cached_results(cache_key)
    
    if cached_results:
        return {"results": cached_results}

    # Sort by most recent updates and return top 10
    results = sorted(results, key=lambda x: x.get("last_updated", ""), reverse=True)[:10]

    log_search("Optimized Search", query, results)
    cache_search_results(cache_key, results, expiry=300)

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    return {"results": [convert_objectid_to_str(doc) for doc in results]}
