import React, { useState } from "react";
import { SearchResult } from "../types";
import "../styles/index.css";

interface ResultsTableProps {
  results: SearchResult[];
  isPerformancePage?: boolean; // Determines whether to show all details
}

const ResultsTable: React.FC<ResultsTableProps> = ({ results, isPerformancePage = false }) => {
  const [expandedIndex, setExpandedIndex] = useState<number | null>(null);

  return (
    <div className="results-container">
      {results.length === 0 ? (
        <p>No results found.</p>
      ) : (
        <table className="search-results-table">
          <thead>
            <tr>
              <th>Address</th>
              {isPerformancePage && <th>Owners</th>}
              {isPerformancePage && <th>Property Type</th>}
              {isPerformancePage && <th>Year Built</th>}
              {isPerformancePage && <th>Square Feet</th>}
              {isPerformancePage && <th>Zoning</th>}
            </tr>
          </thead>
          <tbody>
            {results.map((res, index) => (
              <React.Fragment key={index}>
                <tr
                  className="address-row"
                  onMouseEnter={() => !isPerformancePage && setExpandedIndex(index)}
                  onMouseLeave={() => !isPerformancePage && setExpandedIndex(null)}
                >
                  <td>{res.address}</td>
                  {isPerformancePage && <td>{res.owners.map(owner => owner.owner_name).join(", ")}</td>}
                  {isPerformancePage && <td>{res.property_features.property_type}</td>}
                  {isPerformancePage && <td>{res.property_features.year_built}</td>}
                  {isPerformancePage && <td>{res.property_features.square_feet}</td>}
                  {isPerformancePage && <td>{res.zoning_info.zoning_type}</td>}
                </tr>

                {/* Expandable details only for search results (not performance page) */}
                {!isPerformancePage && expandedIndex === index && (
                  <tr className="expanded-row">
                    <td colSpan={1}>
                      <div className="expanded-content">
                        <h3>🏠 Property Overview</h3>
                        <p><strong>Property ID:</strong> {res.property_id}</p>
                        <p><strong>Legal Description:</strong> {res.legal_description}</p>

                        <h3>Owners</h3>
                        <p>{res.owners.map(owner => `${owner.owner_name} (${owner.owner_type})`).join(", ")}</p>

                        <h3>📜 Zoning</h3>
                        <p>{res.zoning_info.zoning_type}, {res.zoning_info.lot_size_acres} acres</p>

                        <h3>🏡 Features</h3>
                        <p>{res.property_features.property_type}, {res.property_features.bedrooms} Beds, {res.property_features.bathrooms} Baths</p>
                        <p>Garage: {res.property_features.garage}, Pool: {res.property_features.pool}</p>
                      </div>
                    </td>
                  </tr>
                )}
              </React.Fragment>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ResultsTable;
