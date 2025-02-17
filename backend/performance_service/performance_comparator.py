from fastapi import APIRouter, HTTPException
from time import time
from typing import Optional
from search_service.routes import initial_search, optimized_search
from database.db import properties_collection
from rapidfuzz import fuzz
from indexing_service.redis_cache import cache_search_results, get_cached_results  # ✅ Import Caching Functions

router = APIRouter()

# Utility function to calculate common properties
def find_common_properties(results1, results2):
    ids_1 = {r["property_id"] for r in results1}
    ids_2 = {r["property_id"] for r in results2}
    common_ids = ids_1.intersection(ids_2)
    return len(common_ids), common_ids

# Utility function to calculate similarity scores
def calculate_average_similarity(query, results):
    if not results:
        return 0.0
    similarities = [fuzz.WRatio(query.lower(), r["address"].lower()) for r in results]
    return sum(similarities) / len(similarities)

@router.get("/compare_performance")
async def compare_search_performance(
    query: str,
    property_type: Optional[str] = None,
    zoning_type: Optional[str] = None,
    mortgage_status: Optional[str] = None,
    limit: Optional[int] = 0
):
    """
    Compares Initial vs Optimized Search based on execution time, results, and common properties.
    Uses caching for optimized search.
    """
    try:
        # Generate cache key
        cache_key = f"optimized_search:{query.lower().strip()}-{property_type or 'any'}-{zoning_type or 'any'}-{mortgage_status or 'any'}-{limit}"
        
        #  Check if optimized search results exist in cache
        cached_results = get_cached_results(cache_key)
        cache_hit = cached_results is not None
        cache_response_time = 0.0
        optimized_time = 0.0

        # Measure Initial Search execution time
        start_time = time()
        initial_results = await initial_search(query, limit=limit)
        initial_time = (time() - start_time) * 1000  # Convert to ms
        initial_data = initial_results["results"]

        if cache_hit:
            optimized_data = cached_results
        else:
            start_time = time()
            optimized_results = await optimized_search(query, property_type, zoning_type, mortgage_status, limit)
            optimized_time = (time() - start_time) * 1000  # Convert to ms
            optimized_data = optimized_results["results"]

            #  Store optimized search results in cache
            cache_search_results(cache_key, optimized_data, expiry=300)  # Cache for 5 min

        # Compute common properties
        common_count, common_ids = find_common_properties(initial_data, optimized_data)

        # Compute exclusive properties
        unique_initial = len(initial_data) - common_count
        unique_optimized = len(optimized_data) - common_count

        # Calculate similarity scores
        initial_similarity = calculate_average_similarity(query, initial_data)
        optimized_similarity = calculate_average_similarity(query, optimized_data)

        # ✅ Return only performance metrics (Fix Applied)
        performance_data = {
            "execution_time": {
                "initial_search_ms": round(initial_time, 2),
                "optimized_search_ms": round(optimized_time, 2) if not cache_hit else cache_response_time,
            },
            "results_comparison": {
                "total_initial_results": len(initial_data),
                "total_optimized_results": len(optimized_data),
                "common_properties": common_count,
                "unique_to_initial": unique_initial,
                "unique_to_optimized": unique_optimized,
            },
            "search_effectiveness": {
                "initial_similarity_score": round(initial_similarity, 2),
                "optimized_similarity_score": round(optimized_similarity, 2),
            },
            "caching_performance": {
                "cache_hit": cache_hit,
                "cache_response_time_ms": round(cache_response_time, 2),
                "cache_miss": not cache_hit,
            }
        }

        return performance_data  #  Returns Performance Metrics, NOT Search Results

    except HTTPException as e:
        return {"error": str(e)}
