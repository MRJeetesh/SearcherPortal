import React from "react";
import { SearchResult } from "../types";

interface Props {
  results: SearchResult[];
  title: string;
}

const Summary: React.FC<Props> = ({ results, title }) => {
  if (results.length === 0) return <p>No results found.</p>;

  const totalProperties = results.length;

  return (
    <div className="summary-container">
      <h2>{title}</h2>
      <p><strong>Total Properties Found:</strong> {totalProperties}</p>
    </div>
  );
};

export default Summary;
