import pymongo
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["title_research_db"]
properties_collection = db["properties"]

# Function to generate property owners
def generate_owners():
    num_owners = random.randint(1, 3)  # Each property has 1 to 3 owners
    return [{"owner_name": fake.name(), "owner_type": random.choice(["Individual", "Corporation"])} for _ in range(num_owners)]

# Function to generate sale history where seller and buyer are from owners
def generate_sale_history(owners):
    payment_methods = ["Cash", "Mortgage", "Installments", "Owner Financing"]
    sale_history = []

    # Sort sales in chronological order
    sale_dates = [fake.date_between(start_date="-20y", end_date="today").strftime("%Y-%m-%d") for _ in range(random.randint(1, 5))]
    sale_dates.sort()  # Oldest sale first

    for i, date in enumerate(sale_dates):
        if len(owners) >= 2:
            # Pick a seller and a buyer from the list
            seller, buyer = random.sample([o["owner_name"] for o in owners], 2)
        else:
            # If there's only one owner, they are both the seller and buyer (re-selling within the same entity)
            seller = buyer = owners[0]["owner_name"]

        sale_history.append({
            "date": date,
            "sale_price": random.randint(75000, 950000),
            "buyer": buyer,
            "seller": seller,
            "payment_method": random.choice(payment_methods),
            "real_estate_agent": fake.name()
        })

    return sale_history

# Function to generate mortgage records
def generate_mortgages():
    return [
        {
            "lender": fake.company(),
            "amount": random.randint(50000, 900000),
            "date": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d"),
            "interest_rate": round(random.uniform(2.0, 7.5), 2),
            "term_years": random.choice([15, 20, 30]),
            "status": random.choice(["Active", "Paid Off", "Default"])
        }
        for _ in range(random.randint(0, 3))
    ]

# Function to generate encumbrances (liens, unpaid taxes, easements)
def generate_encumbrances():
    encumbrance_types = ["Tax Lien", "Mechanic's Lien", "Easement", "HOA Lien", "Zoning Restriction"]
    return [
        {
            "type": random.choice(encumbrance_types),
            "amount": random.randint(5000, 100000),
            "status": random.choice(["Active", "Resolved"]),
            "date_filed": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d")
        }
        for _ in range(random.randint(0, 2))
    ]

# Function to generate zoning and land use details
def generate_zoning_info():
    zoning_types = ["Residential", "Commercial", "Industrial", "Agricultural", "Mixed-Use"]
    return {
        "zoning_type": random.choice(zoning_types),
        "lot_size_acres": round(random.uniform(0.5, 15.0), 2),
        "land_use_restrictions": fake.sentence(nb_words=10)
    }

# Function to generate property features
def generate_property_features():
    property_types = ["Single Family", "Multi-Family", "Townhouse", "Condo", "Apartment", "Commercial Building"]
    return {
        "property_type": random.choice(property_types),
        "year_built": random.randint(1900, 2023),
        "bedrooms": random.randint(1, 7),
        "bathrooms": random.randint(1, 5),
        "square_feet": random.randint(500, 100000),
        "garage": random.choice(["Yes", "No"]),
        "pool": random.choice(["Yes", "No"]),
        "basement": random.choice(["Yes", "No"]),
    }

# Generate 15,000 property records
property_data = []
for _ in range(15000):
    owners = generate_owners()
    property_record = {
        "property_id": fake.uuid4(),
        "address": fake.address(),
        "owners": owners,
        "legal_description": f"Lot {random.randint(1, 100)}, Block {random.randint(1, 10)}, {fake.city()}",
        "sale_history": generate_sale_history(owners),
        "mortgages": generate_mortgages(),
        "encumbrances": generate_encumbrances(),
        "zoning_info": generate_zoning_info(),
        "property_features": generate_property_features(),
        "last_updated": datetime.utcnow().isoformat()
    }
    property_data.append(property_record)

# Clear existing database and insert new data
properties_collection.delete_many({})
properties_collection.insert_many(property_data)

print("Successful")
