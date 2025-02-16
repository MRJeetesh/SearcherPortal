import React, { useState } from "react";
import { fetchOptimizedSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";

const OptimizedSearchPage: React.FC = () => {
  const [query, setQuery] = useState("");
  const [propertyType, setPropertyType] = useState("");
  const [zoningType, setZoningType] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const data = await fetchOptimizedSearch(query, propertyType, zoningType);
    setResults(data.results || []);
  };

  return (
    <div className="search-page">
      <h1>Search 2 (Optimized Search)</h1>
      <input
        type="text"
        placeholder="Enter search query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <select onChange={(e) => setPropertyType(e.target.value)}>
        <option value="">Select Property Type</option>
        <option value="Apartment">Apartment</option>
        <option value="Commercial">Commercial</option>
      </select>
      <select onChange={(e) => setZoningType(e.target.value)}>
        <option value="">Select Zoning Type</option>
        <option value="Residential">Residential</option>
        <option value="Agricultural">Agricultural</option>
      </select>
      <button onClick={handleSearch}>Search</button>
      <ResultsTable results={results} />
    </div>
  );
};

export default OptimizedSearchPage;
