from fastapi import FastAPI
from search_service.routes import router as search_router
from logging_service.routes import router as logging_router
from indexing_service.routes import router as indexing_router
from performance_service.routes import router as performance_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Searcher Portal API",
    description="Property Search API with Fuzzy Search, Optimized Search, Logging and Caching."
)

#Enable CORS(Allow Frontend to Access API)
app.add_middleware(
   CORSMiddleware,
   allow_origins=["http://localhost:3000"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
app.include_router(search_router, prefix="/api/search", tags=["Search"])
app.include_router(logging_router, prefix="/api/logs", tags=["Logging"])
app.include_router(indexing_router, prefix="/api/index", tags=["Indexing"])
app.include_router(performance_router, prefix="/api/performance", tags=["Performance"])

@app.get("/")
async def root():
    return{"message": "Welcome to the Searcher Portal API"}

#Handling the favicon request
#@app.get("/favicon.ico",include_in_schema=False)
#async def favicon():
 #   return FileResponse("static/favicon.ico")