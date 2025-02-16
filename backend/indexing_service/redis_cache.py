import redis
import json
from bson import ObjectId

# Redis connection setup
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Utility function to convert ObjectId to string
def convert_objectid_to_str(doc):
    """Recursively converts ObjectId fields to strings for JSON serialization."""
    if isinstance(doc, list):
        return [convert_objectid_to_str(item) for item in doc]
    if isinstance(doc, dict):
        return {k: convert_objectid_to_str(v) for k, v in doc.items()}
    if isinstance(doc, ObjectId):
        return str(doc)
    return doc

def cache_search_results(query: str, results: list, expiry: int = 300):
    """
    Caches search results in Redis after converting ObjectId fields.
    """
    serialized_results = convert_objectid_to_str(results)
    redis_client.setex(f"search:{query}", expiry, json.dumps(serialized_results))

def get_cached_results(query: str):
    """
    Retrieves cached search results from Redis and deserializes them.
    """
    cached_data = redis_client.get(f"search:{query}")
    return json.loads(cached_data) if cached_data else None

def clear_cache():
    """
    Clears all cached search results.
    """
    redis_client.flushdb()
    print("Redis cache cleared!")
