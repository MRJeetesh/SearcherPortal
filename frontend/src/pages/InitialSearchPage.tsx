import React, { useState } from "react";
import { fetchInitialSearch } from "../services/searchService";
import ResultsTable from "../components/ResultsTable";

const InitialSearchPage: React.FC = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const data = await fetchInitialSearch(query);
    setResults(data.results || []);
  };

  return (
    <div className="search-page">
      <h1>Search 1 (Initial Search)</h1>
      <input
        type="text"
        placeholder="Enter search query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      <ResultsTable results={results} />
    </div>
  );
};

export default InitialSearchPage;
