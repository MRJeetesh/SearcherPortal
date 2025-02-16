import React from "react";

interface Result {
  property_id: string;
  address: string;
  owners: { owner_name: string; owner_type: string }[];
}

interface ResultsTableProps {
  results: Result[];
}

const ResultsTable: React.FC<ResultsTableProps> = ({ results }) => {
  return (
    <div className="results-container">
      {results.length === 0 ? <p>No results found.</p> : (
        <table>
          <thead>
            <tr>
              <th>Property ID</th>
              <th>Address</th>
              <th>Owners</th>
            </tr>
          </thead>
          <tbody>
            {results.map((res, index) => (
              <tr key={index}>
                <td>{res.property_id}</td>
                <td>{res.address}</td>
                <td>
                  {res.owners.map((owner, i) => (
                    <div key={i}>{owner.owner_name} ({owner.owner_type})</div>
                  ))}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ResultsTable;
