const BASE_URL = "http://127.0.0.1:8000/api/search/search";

export const fetchInitialSearch = async (query: string) => {
  const response = await fetch(`${BASE_URL}/initial?query=${query}`);
  return await response.json();
};

export const fetchOptimizedSearch = async (query: string, propertyType?: string, zoningType?: string) => {
  let url = `${BASE_URL}/optimized?query=${query}`;
  if (propertyType) url += `&property_type=${propertyType}`;
  if (zoningType) url += `&zoning_type=${zoningType}`;

  const response = await fetch(url);
  return await response.json();
};
