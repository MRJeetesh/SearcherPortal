from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)
db = client["title_research_db"]

properties_collection = db["properties"]
logs_collection = db["search_logs"]

print("Connection Established")