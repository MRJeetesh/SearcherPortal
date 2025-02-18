import React, { useState } from "react";
import { fetchOptimizedSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";
import "../styles/style.css";
import { ArrowLeft } from "lucide-react";
import { useNavigate } from "react-router-dom";

const OptimizedSearchPage: React.FC = () => {
  const [query, setQuery] = useState("");
  const [propertyType, setPropertyType] = useState("");
  const [zoningType, setZoningType] = useState("");
  const [results, setResults] = useState([]);
  const navigate = useNavigate();
  const propertyTypes = [
    "Single Family",
    "Multi-Family",
    "Townhouse",
    "Condo",
    "Apartment",
    "Commercial Building",
  ];
  
  const zoningTypes = [
    "Residential",
    "Commercial",
    "Industrial",
    "Agricultural",
    "Mixed-Use",
  ];

  const handleSearch = async () => {
    const data = await fetchOptimizedSearch(query, propertyType, zoningType);
    setResults(data.results || []);
  };


  return (
    <div className="optimized-search-page">
      <button className="back-btn" onClick={() => navigate("/")}>
        <ArrowLeft size={20} /> 
      </button>
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
           {/* Property Type Dropdown */}
            <select className="filter-dropdown" onChange={(e) => setPropertyType(e.target.value)}>
              <option value="">Property Type</option>
              {propertyTypes.map((type, index) => (
                <option key={index} value={type}>{type}</option>
              ))}
            </select>

            {/* Zoning Type Dropdown */}
            <select className="filter-dropdown" onChange={(e) => setZoningType(e.target.value)}>
              <option value="">Zoning Type</option>
              {zoningTypes.map((zone, index) => (
                <option key={index} value={zone}>{zone}</option>
              ))}
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
