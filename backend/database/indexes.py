from db import properties_collection

def create_indexes():
    properties_collection.create_index([("owners.owner_name", "text"), ("address", "text"), ("legal_description","text")], name="text_index")
    properties_collection.create_index([("address", 1)],name="address_index")

    #Index for property type
    properties_collection.create_index([("property_features.property_type",1)], name="property_type_index")

    #Index for mortgage status
    properties_collection.create_index([("mortgages.status",1)], name="mortgage_status_index")

    #Index based on zoning type
    properties_collection.create_index([("zoning_info.zoning_type",1)],name="zoning_type_index")

    #Indexes on last updated timestamp
    properties_collection.create_index([("last_updated",-1)],name="last_updated_index")

    print("Indexes Created Successfully")

if __name__ == "__main__":
    create_indexes()
