import pymongo
from faker import Faker
import random
from datetime import datetime

fake = Faker()

#connect to NoSQL
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["title_research_db"]
properties_collection = db["properties"]

def generate_sale_history():
    payment_methods = ["Cash","Mortgage", "Installments", "Owner Financing"]
    return [
        {
            "date": fake.date_between(start_date = '-20y', end_date="today").strftime("%Y-%m-%d"),
            "sale_price": random.randint(75000, 950000),
            "buyer": fake.name(),
            "seller": fake.name(),
            "payment_method": random.choice(payment_methods),
            "real_estate_agent": fake.name()

        }
        for _ in range(random.randint(1,4))
    ]

def generate_mortgages():
    return [
        {
            "lender": fake.company(),
            "amount": random.randint(50000, 800000),
            "date": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d"),
            "interest_rate":round(random.uniform(2.5,7.5),2),
            "term_years":random.choice([15,20,30]),
            "status": random.choice(["Active","Paid Off","Default"])
        }
        for _ in range(random.randint(0,3))
    ]

# generate encumbrances [liens, unpaid taxes, easements]
def generate_encumbrances():
    encumbrance_types = ["Tax Lein", "Mechanic's Lien", "Easement", "HOA Lien", "Zoning Restriction"]
    return [
        {
            "type": random.choice(encumbrance_types),
            "amount": random.randint(5000, 100000),
            "status": random.choice(["Active", "Resolved"]),
            "date_filed": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d")
        }
        for _ in range(random.randint(0,2))
    ]

# Zoning and land use details
def generate_zoning_info():
    zoning_types = ["Residential","Commercial", "Industrial", "Agricultural", "Mixed-Use"]
    return {
        "zoning_type": random.choice(zoning_types),
        "lot_size_acres": round(random.uniform(0.1,10.0),2),
        "land_use_restrictions": fake.sentence()
    }

def generate_property_features():
    property_types = ["Single Family", "Multi-Family", "Townhouse", "Condo", "Apartment", "Commercial Building"]
    return{
        "property_type":random.choice(property_types),
        "year_built": random.randint(1900, 2022),
        "bedrooms": random.randint(1,7),
        "bathrooms": random.randint(1,5),
        "square_feet": random.randint(500, 100000),
        "garage": random.choice(["Yes", "No"]),
        "pool": random.choice(["Yes", "No"]),
        "basement": random.choice(["Yes", "No"])
    }

property_data = []
for _ in range(5000):
    property_record = {
        "property_id": fake.uuid4(),
        "address": fake.address(),
        "owners": [
            {
                "owner_name": fake.name(), "owner_type": random.choice(["Individual", "Corporation"])
            }
            for _ in range(random.randint(1,3))
        ],
        "legal_description": "Lot {}, Block {}, {}".format(random.randint(1,100), random.randint(1,10), fake.city()),
        "sale_history": generate_sale_history(),
        "mortgages": generate_mortgages(),
        "encumbrances": generate_encumbrances(),
        "zoning_info": generate_zoning_info(),
        "property_features": generate_property_features(),
        "last_updated": datetime.utcnow().isoformat()

    }
    property_data.append(property_record)

properties_collection.insert_many(property_data)

print("Success")
