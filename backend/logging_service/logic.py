from database.db import logs_collection
from datetime import datetime

def log_search(query, search_type, results):
    """
    Logs search queries and results into MongoDB.
    """
    log_entry = {
        "query": query,
        "search_type": search_type,
        "results_count": len(results),
        "timestamp": datetime.utcnow().isoformat()
    }
    logs_collection.insert_one(log_entry)
    print(f" LOGGED SEARCH: {query} ({search_type}) -> {len(results)} results")
