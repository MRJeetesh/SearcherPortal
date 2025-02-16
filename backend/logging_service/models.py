from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# 🎯 Log Schema for storing search queries & results
class SearchLog(BaseModel):
    search_query: str = Field(..., title="User Search Query")
    filters_used: Optional[dict] = Field({}, title="Filters Applied")
    results_count: int = Field(..., title="Number of Results Returned")
    results_preview: List[dict] = Field([], title="Preview of Top 3 Results")
    timestamp: datetime = Field(default_factory=datetime.utcnow, title="Timestamp of Search")
