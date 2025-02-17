const BASE_URL = "http://127.0.0.1:8000/api/performance";

export const fetchPerformanceComparison = async (query: string) => {
  const response = await fetch(`${BASE_URL}/compare_performance?query=${query}`);
  return await response.json();
};
