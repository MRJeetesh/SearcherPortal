# **Searcher Portal**

## **Overview**
Searcher Portal is a robust property search application designed to perform fuzzy searches efficiently. It utilizes **Levenshtein Distance** for initial searches and **Jaro-Winkler with N-Gram Matching** for optimized searches, ensuring high accuracy and performance. The optimized system also integrates **Redis caching** to improve search response time and **MongoDB** as its database backend.

## **Features**
- **Initial Search**: Uses Levenshtein Distance for typo handling.
- **Optimized Search**: Implements Jaro-Winkler similarity and N-Gram matching for better accuracy.
- **Caching**: Utilizes Redis for performance improvement.
- **Performance Comparison**: Compares execution time, results, and cache efficiency.
- **Logging**: Stores search logs for analysis and debugging.

## **Tech Stack**
- **Backend**: FastAPI, Python, MongoDB, Redis
- **Frontend**: React, TypeScript
- **Database**: MongoDB (NoSQL)
- **Caching**: Redis
- **Deployment**: GitHub

## **Installation and Setup**
### **Prerequisites**
Ensure the following are installed:
- Python (3.7+)
- Node.js and npm
- MongoDB
- Redis

## **Caching Mechanism**
- **Redis stores search results** to reduce repeated database queries.
- **Cache expiration is set to 5 minutes** for fresh results.
- **Cache Hits** return stored results, while **Cache Misses** trigger a new database fetch.

## **Performance Metrics**
- **Execution time** of initial vs optimized search.
- **Number of total results** fetched.
- **Common vs unique properties** between searches.
- **Cache hit/miss** performance tracking.

## **Future Enhancements**
- **Auto-Suggestions** for search queries.
- **Recommendation Engine** based on past searches.
- **Scalability Improvements** using cloud deployment.

## **How to Contribute**
1. **Fork the repository.**
2. **Create a new branch:**
   git checkout -b feature-branch
3. **Commit Changes:**
   git commit -m "Added new feature"
4. **Push To GitHub:**
   git push origin feature-branch
4. **Create Pull Request:**


## **Authored By: Jeetesh Chamana** 
