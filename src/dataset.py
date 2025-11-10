from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class EvalItem:
    """
    Single evaluation item for the LLM harness.

    Attributes
    ----------
    id : int
        Unique identifier of the task.
    category : str
        Category / domain of the task (e.g. 'math', 'safety').
    prompt : str
        Prompt that will be sent to the model.
    expected_keywords : List[str]
        List of keywords that a good answer is expected to contain.
    """

    id: int
    category: str
    prompt: str
    expected_keywords: List[str]


def load_eval_set(path: str | Path = "data/eval_set.json") -> List[EvalItem]:
    """
    Load evaluation set from a JSON file.

    Parameters
    ----------
    path : str or Path
        Path to the JSON file.

    Returns
    -------
    List[EvalItem]
        List of evaluation items.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Eval set file not found: {p}")

    data = json.loads(p.read_text(encoding="utf-8"))
    items: List[EvalItem] = []
    for row in data:
        items.append(
            EvalItem(
                id=int(row["id"]),
                category=str(row["category"]),
                prompt=str(row["prompt"]),
                expected_keywords=list(row["expected_keywords"]),
            )
        )
    return items
