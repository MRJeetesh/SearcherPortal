from Levenshtein import distance as levenshtein_distance
from rapidfuzz.distance import JaroWinkler

def is_levenshtein_match(query: str, candidate: str, max_distance: int = 2) -> bool:
    """
    Checks if the candidate word is within a max Levenshtein edit distance from the query.
    """
    return levenshtein_distance(query.lower(), candidate.lower()) <= max_distance


def is_jaro_winkler_match(query: str, candidate: str, threshold: float = 0.85) -> bool:
    """
    Checks if the candidate word is similar to query using Jaro-Winkler similarity.
    """
    return JaroWinkler.similarity(query.lower(), candidate.lower()) >= threshold


