from __future__ import annotations

from typing import Dict, List

from .dataset import load_eval_set
from .llm_stub import LlmStub
from .metrics import aggregate_results, keyword_hit_rate


def run_eval() -> None:
    """
    Run the evaluation harness on the current eval_set.json.

    Steps:
    - load all evaluation items,
    - for each item, generate a stub answer,
    - compute keyword hit rate,
    - aggregate statistics and print everything to stdout.
    """
    eval_items = load_eval_set()
    model = LlmStub()

    results: List[Dict] = []

    for item in eval_items:
        answer = model.generate(item.prompt)
        score = keyword_hit_rate(answer, item.expected_keywords)
        results.append(
            {
                "id": item.id,
                "category": item.category,
                "score": score,
            }
        )

    summary = aggregate_results(results)

    print("Per-item results:")
    for r in results:
        print(r)

    print("\nSummary:")
    for k, v in summary.items():
        print(f"{k}: {v:.3f}")


if __name__ == "__main__":
    run_eval()
