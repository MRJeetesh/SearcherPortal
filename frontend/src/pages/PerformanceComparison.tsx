import React, { useState } from "react";
import { fetchInitialSearch, fetchOptimizedSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";
import "../styles/index.css";

const PerformanceComparison: React.FC = () => {
  const [query, setQuery] = useState("");
  const [initialResults, setInitialResults] = useState([]);
  const [optimizedResults, setOptimizedResults] = useState([]);
  const [initialTime, setInitialTime] = useState(0);
  const [optimizedTime, setOptimizedTime] = useState(0);

  const handleCompare = async () => {
    if (!query.trim()) return;

    const startInitial = performance.now();
    const initialData = await fetchInitialSearch(query);
    setInitialResults(initialData.results || []);
    setInitialTime(performance.now() - startInitial);

    const startOptimized = performance.now();
    const optimizedData = await fetchOptimizedSearch(query);
    setOptimizedResults(optimizedData.results || []);
    setOptimizedTime(performance.now() - startOptimized);
  };

  return (
    <div className="comparison-container">
      <h1>Performance Comparison</h1>
      <p>Compare the execution time and results of the two search strategies.</p>

      <div className="search-box">
        <input
          type="text"
          placeholder="Enter search query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleCompare}>Compare</button>
      </div>

      <div className="comparison-results">
        <div className="result-box">
          <h2>Initial Search</h2>
          <p>Execution Time: <strong>{initialTime.toFixed(2)} ms</strong></p>
          <ResultsTable results={initialResults} isPerformancePage={true} />
        </div>

        <div className="result-box">
          <h2>Optimized Search</h2>
          <p>Execution Time: <strong>{optimizedTime.toFixed(2)} ms</strong></p>
          <ResultsTable results={optimizedResults} isPerformancePage={true} />
        </div>
      </div>
    </div>
  );
};

export default PerformanceComparison;
