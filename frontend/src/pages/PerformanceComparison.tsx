import React, { useState } from "react";
import { fetchInitialSearch, fetchOptimizedSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";

interface Result {
  property_id: string;
  address: string;
  owners: { owner_name: string; owner_type: string }[];
}

const PerformanceComparison: React.FC = () => {
  const [query, setQuery] = useState("");
  const [initialResults, setInitialResults] = useState<Result[]>([]);
  const [optimizedResults, setOptimizedResults] = useState<Result[]>([]);
  const [initialTime, setInitialTime] = useState(0);
  const [optimizedTime, setOptimizedTime] = useState(0);
  const [error, setError] = useState("");

  const handleCompare = async () => {
    if (!query.trim()) {
      setError("Please enter a search query.");
      return;
    }
    setError("");

    try {
      // Measure Initial Search Time
      const startInitial = performance.now();
      const initialData = await fetchInitialSearch(query);
      const endInitial = performance.now();
      setInitialTime(endInitial - startInitial);
      setInitialResults(initialData.results || []);

      // Measure Optimized Search Time
      const startOptimized = performance.now();
      const optimizedData = await fetchOptimizedSearch(query);
      const endOptimized = performance.now();
      setOptimizedTime(endOptimized - startOptimized);
      setOptimizedResults(optimizedData.results || []);
    } catch (err) {
      setError("Failed to fetch results. Please try again.");
    }
  };

  return (
    <div className="performance-container">
      <h1>Search Performance Comparison</h1>
      <p>Compare how the optimized search performs against the initial search.</p>

      <div className="search-box">
        <input
          type="text"
          placeholder="Enter search query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleCompare}>Compare</button>
      </div>

      {error && <p className="error-message">{error}</p>}

      <div className="results-section">
        <div className="result-box">
          <h2>Initial Search</h2>
          <p>Execution Time: <strong>{initialTime.toFixed(2)} ms</strong></p>
          <ResultsTable results={initialResults} />
        </div>

        <div className="result-box">
          <h2>Optimized Search</h2>
          <p>Execution Time: <strong>{optimizedTime.toFixed(2)} ms</strong></p>
          <ResultsTable results={optimizedResults} />
        </div>
      </div>
    </div>
  );
};

export default PerformanceComparison;
