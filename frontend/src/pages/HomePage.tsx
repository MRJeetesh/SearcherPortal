import React from "react";
import { useNavigate } from "react-router-dom";
import { Scale } from "lucide-react"; // Using Scale icon for comparison
import "../styles/style.css";

const HomePage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <div className="layout-container">
        {/* Left Section - Search 1 */}
        <div className="search-section left" onClick={() => navigate("/search1")}>
          <div className="search-box">
            <h2>Search 1 (Basic)</h2>
            <p>Fuzzy search with typo handling and basic ranking.</p>
          </div>
        </div>

        {/* Middle Section - Performance Comparison */}
        <div className="performance-section" onClick={() => navigate("/performance")}>
          <div className="performance-circle">
            <Scale size={32} color="white" />
            <p>Compare</p>
          </div>
        </div>

        {/* Right Section - Search 2 */}
        <div className="search-section right" onClick={() => navigate("/search2")}>
          <div className="search-box">
            <h2>Search 2 (Optimized)</h2>
            <p>Enhanced search accuracy with optimized filtering.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
