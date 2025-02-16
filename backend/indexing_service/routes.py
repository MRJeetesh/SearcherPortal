from fastapi import APIRouter
from indexing_service.logic import trigger_reindexing

router = APIRouter()

@router.post("/index/rebuild")
def rebuild_indexes():
    """
    Drops and re-creates MongoDB indexes for optimized search performance.
    """
    trigger_reindexing()
    return {"message": "Indexes successfully rebuilt!"}
