from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Define Owner Schema
class Owner(BaseModel):
    owner_name: str = Field(..., title="Owner Name")
    owner_type: str = Field(..., title="Owner Type", example="Individual or Corporation")

# Define Sale History Schema
class SaleHistory(BaseModel):
    date: str = Field(..., title="Sale Date", example="2023-01-15")
    sale_price: int = Field(..., title="Sale Price", example=500000)
    buyer: str = Field(..., title="Buyer Name")
    seller: str = Field(..., title="Seller Name")
    payment_method: str = Field(..., title="Payment Method", example="Cash or Mortgage")
    real_estate_agent: Optional[str] = Field(None, title="Real Estate Agent")

# Define Mortgage Schema
class Mortgage(BaseModel):
    lender: str = Field(..., title="Lender Name")
    amount: int = Field(..., title="Mortgage Amount")
    date: str = Field(..., title="Mortgage Date", example="2021-06-15")
    interest_rate: float = Field(..., title="Interest Rate", example=3.5)
    term_years: int = Field(..., title="Loan Term in Years")
    status: str = Field(..., title="Mortgage Status", example="Active, Paid Off, or Default")

# Define Encumbrance Schema (Liens, Unpaid Taxes, Easements)
class Encumbrance(BaseModel):
    type: str = Field(..., title="Encumbrance Type", example="Tax Lien")
    amount: int = Field(..., title="Encumbrance Amount")
    status: str = Field(..., title="Encumbrance Status", example="Active or Resolved")
    date_filed: str = Field(..., title="Date Filed", example="2020-03-10")

# Define Zoning Information Schema
class ZoningInfo(BaseModel):
    zoning_type: str = Field(..., title="Zoning Type", example="Residential, Commercial, Industrial")
    lot_size_acres: float = Field(..., title="Lot Size in Acres")
    land_use_restrictions: str = Field(..., title="Land Use Restrictions")

# Define Property Features Schema
class PropertyFeatures(BaseModel):
    property_type: str = Field(..., title="Property Type", example="Single Family, Condo, Commercial Building")
    year_built: int = Field(..., title="Year Built")
    bedrooms: int = Field(..., title="Number of Bedrooms")
    bathrooms: int = Field(..., title="Number of Bathrooms")
    square_feet: int = Field(..., title="Total Square Feet")
    garage: str = Field(..., title="Garage Availability", example="Yes or No")
    pool: str = Field(..., title="Pool Availability", example="Yes or No")
    basement: str = Field(..., title="Basement Availability", example="Yes or No")

# Define Main Property Schema (Matches Your MongoDB Structure)
class Property(BaseModel):
    property_id: str = Field(..., title="Property ID", example="uuid-1234")
    address: str = Field(..., title="Property Address")
    legal_description: str = Field(..., title="Legal Description")
    owners: List[Owner] = Field(..., title="List of Owners")
    sale_history: List[SaleHistory] = Field([], title="Sale History Records")
    mortgages: List[Mortgage] = Field([], title="Mortgage Records")
    encumbrances: List[Encumbrance] = Field([], title="Encumbrance Records")
    zoning_info: ZoningInfo
    property_features: PropertyFeatures
    last_updated: datetime = Field(default_factory=datetime.utcnow, title="Last Updated Timestamp")

# Define Search Response Schema
class SearchResponse(BaseModel):
    results: List[Property] = Field(..., title="List of Search Results")
