import React, { useState } from "react";
import { fetchOptimizedSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";
import "../styles/style.css";

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
    <div className="optimized-search-page">
      {/* Header Section */}
      <div className="optimized-search-header">
        <h1>🔍 Advanced Property Search</h1>
        
        {/* Search Bar */}
        <div className="search-bar">
          <input
            type="text"
            placeholder="Enter Name or Address..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <select className="filter-dropdown" onChange={(e) => setPropertyType(e.target.value)}>
            <option value="">Property Type</option>
            <option value="Apartment">Apartment</option>
            <option value="Commercial">Commercial</option>
          </select>
          <select className="filter-dropdown" onChange={(e) => setZoningType(e.target.value)}>
            <option value="">Zoning Type</option>
            <option value="Residential">Residential</option>
            <option value="Agricultural">Agricultural</option>
          </select>
          <button className="optimized-search-btn" onClick={handleSearch}>Search</button>
        </div>
      </div>

      {/* Search Results - Same Style as Initial Search Page */}
      <div className="results-container">
        {results.length > 0 ? (
          <ResultsTable results={results} />
        ) : (
          <p className="no-results-message">No results found. Try modifying your filters.</p>
        )}
      </div>
    </div>
  );
};

export default OptimizedSearchPage;
