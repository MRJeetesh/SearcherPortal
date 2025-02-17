import json
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def convert_objectid_to_str(doc):
    """Converts MongoDB ObjectId to string for API response."""
    doc["_id"] = str(doc["_id"])
    return doc

def cache_search_results(key, results, expiry=300):
    if not results:
        print("⚠️ No results to cache!")
        return
    try:
        json_data = json.dumps([convert_objectid_to_str(doc) for doc in results])  # Convert Mongo ObjectId to string
        redis_client.setex(key, expiry, json_data)
        print(f"Cached Results with Key: {key}")
    except Exception as e:
        print(f" Redis Caching Error: {e}")

def get_cached_results(key):
    try:
        cached_data = redis_client.get(key)
        if cached_data:
            print(f" Cache Hit: Key {key} Found!")
            return json.loads(cached_data)
        else:
            print(f"Cache Miss: Key {key} Not Found!")
            return None
    except Exception as e:
        print(f"Redis Retrieval Error: {e}")
        return None
