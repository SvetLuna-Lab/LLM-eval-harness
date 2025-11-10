from __future__ import annotations

from collections import defaultdict
from typing import Dict, List


def keyword_hit_rate(answer: str, expected_keywords: List[str]) -> float:
    """
    Compute a simple keyword hit rate metric.

    Parameters
    ----------
    answer : str
        Model-generated answer.
    expected_keywords : List[str]
        List of keywords we expect to see in a good answer.

    Returns
    -------
    float
        Fraction of expected keywords that appear in the answer
        (case-insensitive, whitespace tokenization).
    """
    if not expected_keywords:
        return 0.0

    tokens = [t.lower() for t in answer.split()]
    token_set = set(tokens)
    exp = [k.lower() for k in expected_keywords]

    hits = sum(1 for k in exp if k in token_set)
    return hits / len(exp)


def aggregate_results(results: List[Dict]) -> Dict[str, float]:
    """
    Aggregate per-item scores into overall and per-category averages.

    Parameters
    ----------
    results : List[Dict]
        A list of dicts with keys: 'id', 'category', 'score'.

    Returns
    -------
    Dict[str, float]
        Dictionary with:
        - 'overall_mean'
        - 'mean_<category>' for each category in results.
    """
    if not results:
        return {"overall_mean": 0.0}

    by_cat: Dict[str, List[float]] = defaultdict(list)
    for r in results:
        by_cat[r["category"]].append(float(r["score"]))

    overall_mean = sum(float(r["score"]) for r in results) / len(results)

    summary: Dict[str, float] = {"overall_mean": overall_mean}
    for cat, scores in by_cat.items():
        summary[f"mean_{cat}"] = sum(scores) / len(scores)

    return summary
