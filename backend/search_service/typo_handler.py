from rapidfuzz.distance import JaroWinkler
from Levenshtein import ratio as levenshtein_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import textdistance

def is_damerau_levenshtein_match(query: str, candidate: str, threshold: float = 0.2) -> bool:
    """
    Uses Damerau-Levenshtein distance to compare query and candidate strings.
    Handles transpositions and common typos.
    """
    distance = textdistance.damerau_levenshtein.normalized_distance(query.lower(), candidate.lower())
    return distance <= threshold  # Lower distance means higher similarity


# Define the vectorizer globally to avoid reloading it each time
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))  # Bi-gram & Tri-gram

def is_tfidf_match(query: str, candidates: list, threshold: float = 0.4) -> list:
    """
    Uses TF-IDF vectorization and Cosine Similarity to find best matches.
    Returns matches with similarity scores above the threshold.
    """
    if not candidates:
        return []

    corpus = [query] + candidates  # Query + Candidate List
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:]).flatten()

    # Return matches above threshold
    return [candidates[i] for i in range(len(candidates)) if similarity_scores[i] >= threshold]


def is_levenshtein_match(query: str, candidate: str, threshold: float = 0.9) -> bool:
    """
    Checks if the candidate word is similar to the query using Levenshtein similarity.
    The threshold defines the minimum similarity required (default: 80% match).
    """
    similarity = levenshtein_similarity(query.lower(), candidate.lower())
    return similarity >= threshold  # Returns boolean match


def is_jaro_winkler_match(query: str, candidate: str, threshold: float = 0.7) -> tuple:
    """
    Checks if the candidate word is similar to the query using Jaro-Winkler similarity.
    Returns a tuple: (boolean match, similarity score).
    """
    similarity = JaroWinkler.similarity(query.lower(), candidate.lower())
    return similarity >= threshold, similarity  # Boolean match and similarity score

def is_ngram_partial_match(query: str, candidate: str, n: int = 3) -> bool:
    """
    Uses N-gram (substrings) to check if the query is a partial match in candidate.
    """
    query_ngrams = {query[i:i+n] for i in range(len(query) - n + 1)}
    candidate_ngrams = {candidate[i:i+n] for i in range(len(candidate) - n + 1)}

    return bool(query_ngrams & candidate_ngrams)  # Returns True if any common n-gram