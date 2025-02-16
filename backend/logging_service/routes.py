from fastapi import APIRouter
from database.db import db
from logging_service.models import SearchLog
from typing import List

router = APIRouter()
logs_collection = db["search_logs"]

@router.get("/logs", response_model=List[SearchLog])
async def get_search_logs():
    """
    Retrieves the last 20 logged search requests.
    """
    logs = list(logs_collection.find().sort("timestamp", -1).limit(20))
    return logs
