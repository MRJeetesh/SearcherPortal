import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import InitialSearchPage from "./pages/InitialSearchPage";
import OptimizedSearchPage from "./pages/OptimizedSearchPage";
import PerformanceComparison from "./pages/PerformanceComparison";
import "./styles/colors.css"; 

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/search1" element={<InitialSearchPage />} />
        <Route path="/search2" element={<OptimizedSearchPage />} />
        <Route path="/performance" element={<PerformanceComparison />} />
      </Routes>
    </Router>
  );
};

export default App;
