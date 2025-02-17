from fastapi import APIRouter, HTTPException, Query
from pymongo import DESCENDING
from database.db import properties_collection
from search_service.models import SearchResponse
from search_service.typo_handler import is_levenshtein_match, is_jaro_winkler_match, is_ngram_partial_match
from logging_service.logic import log_search
from indexing_service.redis_cache import cache_search_results, get_cached_results
from typing import Optional

router = APIRouter()

# Utility function to convert MongoDB ObjectId to string
def convert_objectid_to_str(doc):
    """Converts MongoDB ObjectId to string for API response."""
    doc["_id"] = str(doc["_id"])
    return doc

# Utility function to get common base query
def build_base_query(query: str):
    """
    Generates a base query that applies to both initial and optimized searches.
    Ensures a common starting point for consistency.
    """
    return {
        "$or": [
            {"owners.owner_name": {"$regex": query, "$options": "i"}},
            {"address": {"$regex": query, "$options": "i"}},
            {"legal_description": {"$regex": query, "$options": "i"}}
        ]
    }

#  Route 1: Initial Search (Levenshtein Typo Handling, No Caching)
@router.get("/search/initial", response_model=SearchResponse)
async def initial_search(query: str = Query(..., title="Search Query"), limit: Optional[int] = 0):
    """
    Performs a fuzzy search with typo handling using Levenshtein Distance.
    Allows dynamic result limits (default: 10).
    """
    query = query.strip().lower()
    base_query = build_base_query(query)

    all_results = list(properties_collection.find(base_query).limit(500))  # Fetch broader dataset first
    results = []

    # Apply Levenshtein Distance Typo Handling
    for result in all_results:
        owner_names = [o["owner_name"] for o in result.get("owners", [])]
        address = result.get("address", "")

        if any(is_levenshtein_match(query, name, 0.8) for name in owner_names) or \
           is_levenshtein_match(query, address, 0.8):
            results.append(result)

    # Retry with regex-based fuzzy matching if no results found
    if not results:
        fuzzy_query = {
            "$or": [
                {"owners.owner_name": {"$regex": query[:3], "$options": "i"}},
                {"address": {"$regex": query[:3], "$options": "i"}}
            ]
        }
        results = list(properties_collection.find(fuzzy_query).sort([("last_updated", DESCENDING)]))

    # Sort results by last_updated
    results = sorted(results, key=lambda x: x.get("last_updated", ""), reverse=True)

    # Apply limit (if set to 0, return all results)
    results = results if limit == 0 else results[:limit]

    log_search("Initial Search", query, results)

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    return {"results": [convert_objectid_to_str(doc) for doc in results]}

#  Route 2: Optimized Search (Hybrid Typo Handling, Caching Enabled)
@router.get("/search/optimized", response_model=SearchResponse)
async def optimized_search(
    query: str = Query(..., title="Search Query"),
    property_type: Optional[str] = None,
    zoning_type: Optional[str] = None,
    mortgage_status: Optional[str] = None,
    limit: Optional[int] = 0
):
    query = query.strip().lower()
    base_query = build_base_query(query)

    # 🔹 Check Redis Cache First
    cache_key = f"optimized_search:{query.lower().strip()}-{property_type or 'any'}-{zoning_type or 'any'}-{mortgage_status or 'any'}-{limit}"
    cached_results = get_cached_results(cache_key)

    if cached_results:
        return {"results": cached_results}

    # Fetch Data from MongoDB
    all_results = list(properties_collection.find(base_query).limit(500))
    results = []

    # Apply Jaro-Winkler and N-Gram Matching
    for result in all_results:
        owner_names = [o["owner_name"] for o in result.get("owners", [])]
        address = result.get("address", "")

        typo_match = any(is_jaro_winkler_match(query, name) for name in owner_names) or is_jaro_winkler_match(query, address)
        partial_match = any(is_ngram_partial_match(query, name) for name in owner_names) or is_ngram_partial_match(query, address)

        if typo_match or partial_match:
            results.append(result)

    # Apply Additional Filters
    if property_type:
        results = [r for r in results if r.get("property_features", {}).get("property_type") == property_type]
    if zoning_type:
        results = [r for r in results if r.get("zoning_info", {}).get("zoning_type") == zoning_type]
    if mortgage_status:
        results = [r for r in results if any(m.get("status") == mortgage_status for m in r.get("mortgages", []))]

    # Sort by Most Recent Updates
    results = sorted(results, key=lambda x: x.get("last_updated", ""), reverse=True)

    # Apply Limit (If 0, Return All)
    results = results if limit == 0 else results[:limit]

    # Log Search & Cache Results
    log_search("Optimized Search", query, results)

    # Convert ObjectId to string before caching
    try:
        cache_search_results(cache_key, results, expiry=300)  # Cache for 5 min
    except Exception as e:
        print(f"Cache Writing Error: {e}")

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    return {"results": [convert_objectid_to_str(doc) for doc in results]}
