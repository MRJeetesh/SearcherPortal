import React, { useState } from "react";
import { SearchResult } from "../types";
import "../styles/style.css";
import { Home, Users, MapPin, Layers, Ruler, CheckCircle, XCircle } from "lucide-react"; // Icons for UI enhancement

interface ResultsTableProps {
  results: SearchResult[];
}

const ResultsTable: React.FC<ResultsTableProps> = ({ results }) => {
  const [visibleCount, setVisibleCount] = useState(10); // Show 10 results initially

  // Function to load more results
  const handleShowMore = () => {
    setVisibleCount((prev) => prev + 10);
  };

  return (
    <div className="results-container">
      {/* Total Results Count */}
      {results.length > 0 && (
        <div className="results-count">
          <p>🔍 Showing <strong>{Math.min(visibleCount, results.length)}</strong> out of <strong>{results.length}</strong> results</p>
        </div>
      )}

      {results.length === 0 ? (
        <p className="no-results">No results found.</p>
      ) : (
        <>
          <div className="results-grid">
            {results.slice(0, visibleCount).map((res, index) => (
              <div className="result-card" key={index}>
                <h3><Home size={18} /> {res.address}</h3>
                <p><Users size={16} /> <strong>Owners:</strong> {res.owners.map(owner => owner.owner_name).join(", ")}</p>
                <p><MapPin size={16} /> <strong>Zoning:</strong> {res.zoning_info.zoning_type}</p>
                <p><Layers size={16} /> <strong>Property Type:</strong> {res.property_features.property_type}</p>
                
                {/* Expandable Section */}
                <div className="expandable-content">
                  <p><strong>Legal Description:</strong> {res.legal_description}</p>
                  <p><Ruler size={16} /> <strong>Square Feet:</strong> {res.property_features.square_feet}</p>
                  <p><strong>Year Built:</strong> {res.property_features.year_built}</p>
                  <p>{res.property_features.garage ? <CheckCircle size={16} color="green" /> : <XCircle size={16} color="red" />} <strong>Garage:</strong> {res.property_features.garage ? "Yes" : "No"}</p>
                  <p>{res.property_features.pool ? <CheckCircle size={16} color="green" /> : <XCircle size={16} color="red" />} <strong>Pool:</strong> {res.property_features.pool ? "Yes" : "No"}</p>
                </div>
              </div>
            ))}
          </div>

          {/* Show More Button */}
          {visibleCount < results.length && (
            <div className="show-more-container">
              <button className="show-more-btn" onClick={handleShowMore}>Show More</button>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default ResultsTable;
