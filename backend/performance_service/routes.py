from fastapi import APIRouter
from performance_service.performance_comparator import compare_search_performance

router = APIRouter()

# Route to compare search performance
router.get("/compare_performance")(compare_search_performance)
