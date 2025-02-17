import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/index.css";

const HomePage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <h1>🔍 Search Comparison Portal</h1>
      <p>Choose a search strategy to proceed.</p>

      <div className="search-options">
        <div className="search-card search-1" onClick={() => navigate("/search1")}>
          <h2>Search 1 (Initial)</h2>
          <p>A fuzzy search with typo handling and basic ranking.</p>
          <button>Go to Search 1</button>
        </div>

        <div className="search-card search-2" onClick={() => navigate("/search2")}>
          <h2>Search 2 (Optimized)</h2>
          <p>Combines optimized and advanced search for better accuracy.</p>
          <button>Go to Search 2</button>
        </div>
      </div>

      <div className="performance-section">
        <p>Want to compare search performance?</p>
        <button className="performance-btn" onClick={() => navigate("/performance")}>
          Go to Performance Page
        </button>
      </div>
    </div>
  );
};

export default HomePage;
