🔎 Searcher Portal: Intelligent Property Search System
🚀 Searcher Portal is a high-performance property search platform designed to optimize title research. It leverages fuzzy search, typo tolerance, advanced ranking algorithms, caching, and performance analytics to deliver fast and accurate results.

📌 Features
✅ Dual Search Modes:

Initial Search: Uses Levenshtein distance for typo handling.
Optimized Search: Combines Jaro-Winkler similarity & N-gram matching for better accuracy.
✅ High-Performance Search Engine

Fuzzy search with partial matching
Redis caching for fast responses
MongoDB indexing for optimized queries
✅ Performance Monitoring & Analytics

API response time tracking
Cache hit/miss analysis
Similarity score comparison
✅ Scalable Microservices Architecture

FastAPI-based backend
React + TypeScript frontend
MongoDB (NoSQL) for property data storage
✅ Enhanced API Security & Logging

JWT-based authentication (future enhancement)
Rate limiting to prevent API abuse
Search query logging for analytics
📂 Project Structure
graphql
Copy
Edit
/Searcher_Portal
│── backend/
│   ├── database/                 # MongoDB connection setup  
│   ├── indexing_service/         # Background indexing & caching logic  
│   ├── logging_service/          # Search logging service  
│   ├── performance_service/      # Performance comparison & analytics  
│   ├── search_service/           # Core search logic & API routes  
│   ├── main.py                   # FastAPI entry point  
│── frontend/
│   ├── src/                      # React & TypeScript frontend  
│   │   ├── components/           # UI components  
│   │   ├── pages/                # Search, Performance Comparison pages  
│   │   ├── services/             # API service handlers  
│   │   ├── styles/               # CSS styles  
│   ├── public/                   # Static assets  
│── .venv/                        # Virtual environment  
│── requirements.txt               # Python dependencies  
│── package.json                   # Frontend dependencies  
│── README.md                      # Project documentation  
🛠️ Tech Stack
Backend
Python + FastAPI (for API development)
MongoDB (for property data storage)
Redis (for caching)
Levenshtein & Jaro-Winkler algorithms (for fuzzy search)
Frontend
React + TypeScript (for UI)
Axios (for API communication)
🚀 Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/MRJeetesh/Searcher_Portal.git
cd Searcher_Portal
2️⃣ Backend Setup
🔹 Create a Virtual Environment
bash
Copy
Edit
cd backend
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows
🔹 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 Start MongoDB & Redis
bash
Copy
Edit
# Run MongoDB (Ensure it's installed)
mongod --dbpath /data/db

# Run Redis (Ensure it's installed)
redis-server
🔹 Start Backend Server
bash
Copy
Edit
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

3️⃣ Frontend Setup
bash
Copy
Edit
cd frontend
npm install  # Install dependencies
npm start    # Start React frontend
The UI will be available at: http://localhost:3000

🖥️ API Endpoints
🔍 Search APIs
Method	Endpoint	Description
GET	/api/search/initial?query={q}	Performs Initial Search using Levenshtein distance
GET	/api/search/optimized?query={q}	Performs Optimized Search using Jaro-Winkler & N-gram
📊 Performance Comparison API
Method	Endpoint	Description
GET	/api/performance/compare_performance?query={q}	Compares Initial vs. Optimized Search performance
🗄️ Caching API
Method	Endpoint	Description
GET	/api/cache/status	Checks cache health status
DELETE	/api/cache/clear	Clears all cached search results
🚀 Future Enhancements
✅ 🔹 Synonym Expansion – Supports searching for alternative property terms
✅ 🔹 Role-Based Access Control (RBAC) – Secure API endpoints based on user roles
✅ 🔹 Bulk Search API – Allows searching multiple queries in one request
✅ 🔹 Auto-Suggestions API – Provides smart autocomplete suggestions
✅ 🔹 WebSockets for Real-Time Updates – Pushes live property updates to users

👨‍💻 Contributors
Jeetesh Chamana
