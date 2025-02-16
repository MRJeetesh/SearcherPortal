import React from "react";
import { useNavigate } from "react-router-dom";
import "./styles/colors.css";

const SearchSelection: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="search-selection">
      <h1>Search Comparison Portal</h1>
      <p>Select a search type to proceed.</p>
      
      <div className="search-options">
        <div className="search-card" onClick={() => navigate("/search1")}>
          <h2>Search 1 (Initial)</h2>
          <p>Performs a fuzzy search with typo handling and basic ranking.</p>
          <button>Go to Search 1</button>
        </div>

        <div className="search-card" onClick={() => navigate("/search2")}>
          <h2>Search 2 (Optimized)</h2>
          <p>Combines optimized and advanced search for better accuracy.</p>
          <button>Go to Search 2</button>
        </div>
      </div>
    </div>
  );
};

export default SearchSelection;
