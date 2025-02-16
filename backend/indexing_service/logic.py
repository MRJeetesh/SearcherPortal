from database.db import db

# Connect to MongoDB properties collection
properties_collection = db["properties"]

def create_indexes():
    """
    Ensures MongoDB indexes are created for optimized search performance.
    """
    properties_collection.create_index([("address", "text")])  # Full-text search index
    properties_collection.create_index([("owners.owner_name", "text")])  # Owner name index
    properties_collection.create_index([("property_features.property_type", 1)])  # Sorting index
    properties_collection.create_index([("zoning_info.zoning_type", 1)])  # Sorting index
    properties_collection.create_index([("last_updated", -1)])  # Sorting index for recent data

    print("Indexes successfully created in MongoDB!")

def trigger_reindexing():
    """
    Drops and re-creates indexes (useful if data structure changes).
    """
    properties_collection.drop_indexes()
    create_indexes()
    print(" Indexing has been re-triggered successfully!")
