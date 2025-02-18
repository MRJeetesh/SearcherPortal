import React, { useState } from "react";
import { fetchInitialSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";
import "../styles/style.css";
import { ArrowLeft } from "lucide-react";
import { useNavigate } from "react-router-dom";

const InitialSearchPage: React.FC = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [showNote, setShowNote] = useState(false);
  const navigate = useNavigate();
  const handleSearch = async () => {
    const data = await fetchInitialSearch(query);
    setResults(data.results || []);
  };

  return (
    <div className="search-page">
        <button className="back-btn" onClick={() => navigate("/")}>
              <ArrowLeft size={20} /> 
            </button>
      {/* Search Bar Section */}
      <div className="search-header">
        <h1>🔍 Find Property Records</h1>
        <div 
          className="search-bar" 
          onMouseEnter={() => setShowNote(true)} 
          onMouseLeave={() => setShowNote(false)}
        >
          <input
            type="text"
            placeholder="Enter Name or Address..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button onClick={handleSearch}>Search</button>
        </div>
        {/* Hover Note Below Search Bar */}
        {showNote && <p className="search-note">Results are generated based on Name and Address.</p>}
      </div>

      {/* Search Results Section - Now Uses Card Layout */}
      <div className="results-container">
        {results.length > 0 ? (
          <ResultsTable results={results} />
        ) : (
          <p className="no-results-message">No results found. Try searching for another property.</p>
        )}
      </div>
    </div>
  );
};

export default InitialSearchPage;
