export interface Owner {
  owner_name: string;
  owner_type: string; // Individual or Corporation
}

export interface SaleHistory {
  date: string;
  sale_price: number;
  buyer: string;
  seller: string;
  payment_method: string;
  real_estate_agent: string;
}

export interface Mortgage {
  lender: string;
  amount: number;
  date: string;
  interest_rate: number;
  term_years: number;
  status: string;
}

export interface Encumbrance {
  type: string;
  amount: number;
  status: string;
  date_filed: string;
}

export interface ZoningInfo {
  zoning_type: string;
  lot_size_acres: number;
  land_use_restrictions: string;
}

export interface PropertyFeatures {
  property_type: string;
  year_built: number;
  bedrooms: number;
  bathrooms: number;
  square_feet: number;
  garage: string;
  pool: string;
  basement: string;
}

export interface SearchResult {
  property_id: string;
  address: string;
  owners: Owner[];
  legal_description: string;
  sale_history: SaleHistory[];
  mortgages: Mortgage[];
  encumbrances: Encumbrance[];
  zoning_info: ZoningInfo;
  property_features: PropertyFeatures;
}
