import React, { useState } from "react";
import { fetchPerformanceComparison } from "../services/performanceService";
import { PerformanceMetrics } from "../types";
import "../styles/style.css";
import { ArrowLeft } from "lucide-react";
import { useNavigate } from "react-router-dom";

const PerformanceComparison: React.FC = () => {
  const [query, setQuery] = useState("");
  const [performanceData, setPerformanceData] = useState<PerformanceMetrics | null>(null);
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const handleCompare = async () => {
    setError("");
    setPerformanceData(null);
    
    if (!query.trim()) {
      setError("Please enter a search query.");
      return;
    }

    try {
      const data = await fetchPerformanceComparison(query);
      console.log("Performance Data:", data); // Debugging API response

      if (
        data.execution_time &&
        data.results_comparison &&
        data.search_effectiveness &&
        data.caching_performance
      ) {
        setPerformanceData({
          executionTime: {
            initialSearchMs: data.execution_time.initial_search_ms,
            optimizedSearchMs: data.execution_time.optimized_search_ms,
          },
          resultsComparison: {
            totalInitialResults: data.results_comparison.total_initial_results,
            totalOptimizedResults: data.results_comparison.total_optimized_results,
            commonProperties: data.results_comparison.common_properties,
            uniqueToInitial: data.results_comparison.unique_to_initial,
            uniqueToOptimized: data.results_comparison.unique_to_optimized,
          },
          searchEffectiveness: {
            initialSimilarityScore: data.search_effectiveness.initial_similarity_score,
            optimizedSimilarityScore: data.search_effectiveness.optimized_similarity_score,
          },
          cachingPerformance: {
            cacheHit: data.caching_performance.cache_hit,
            cacheResponseTimeMs: data.caching_performance.cache_response_time_ms,
            cacheMiss: data.caching_performance.cache_miss,
          },
        });
      } else {
        setError("Invalid API response structure.");
      }
    } catch (err) {
      setError("Failed to fetch performance comparison. Please try again.");
    }
  };

  return (
    <div className="performance-container">
      <button className="back-btn" onClick={() => navigate("/")}>
        <ArrowLeft size={20} /> 
      </button>
      <h1>Performance Comparison</h1>
      <p>Compare execution time, effectiveness, and caching performance of Initial vs Optimized search.</p>

      <div className="search-bar">
        <input
          type="text"
          placeholder="Enter search query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button className="compare-btn" onClick={handleCompare}>Compare</button>
      </div>

      {error && <p className="error-message">{error}</p>}

      {performanceData && (
        <div className="performance-results">
          <h2>Comparison Results</h2>
          <table className="performance-table">
            <thead>
              <tr>
                <th>Metric</th>
                <th>Initial Search</th>
                <th>Optimized Search</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Execution Time (ms)</td>
                <td>{performanceData.executionTime.initialSearchMs?.toFixed(2) ?? "N/A"}</td>
                <td>{performanceData.executionTime.optimizedSearchMs?.toFixed(2) ?? "N/A"}</td>
              </tr>
              <tr>
                <td>Total Properties Found</td>
                <td>{performanceData.resultsComparison.totalInitialResults ?? "N/A"}</td>
                <td>{performanceData.resultsComparison.totalOptimizedResults ?? "N/A"}</td>
              </tr>
              <tr>
                <td>Common Properties</td>
                <td colSpan={2}>{performanceData.resultsComparison.commonProperties ?? "N/A"}</td>
              </tr>
              <tr>
                <td>Unique Properties</td>
                <td>{performanceData.resultsComparison.uniqueToInitial ?? "N/A"}</td>
                <td>{performanceData.resultsComparison.uniqueToOptimized ?? "N/A"}</td>
              </tr>
              <tr>
                <td>Search Effectiveness (Similarity Score)</td>
                <td>{performanceData.searchEffectiveness.initialSimilarityScore?.toFixed(2) ?? "N/A"}</td>
                <td>{performanceData.searchEffectiveness.optimizedSimilarityScore?.toFixed(2) ?? "N/A"}</td>
              </tr>
              <tr>
                <td>Cache Hit?</td>
                <td colSpan={2}>{performanceData.cachingPerformance.cacheHit ? "Yes" : "No"}</td>
              </tr>
              <tr>
                <td>Cache Response Time (ms)</td>
                <td colSpan={2}>{performanceData.cachingPerformance.cacheResponseTimeMs?.toFixed(2) ?? "N/A"}</td>
              </tr>
              <tr>
                <td>Cache Miss?</td>
                <td colSpan={2}>{performanceData.cachingPerformance.cacheMiss ? "Yes" : "No"}</td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default PerformanceComparison;
