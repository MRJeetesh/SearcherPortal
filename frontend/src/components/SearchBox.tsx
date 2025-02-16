import React from "react";

interface SearchBoxProps {
  query: string;
  setQuery: (query: string) => void;
  handleSearch: () => void;
}

const SearchBox: React.FC<SearchBoxProps> = ({ query, setQuery, handleSearch }) => {
  return (
    <div className="search-box">
      <input
        type="text"
        placeholder="Enter search query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchBox;
