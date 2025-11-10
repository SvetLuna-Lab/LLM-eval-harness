# LLM-eval-harness

Small **LLM evaluation harness** designed as an educational / portfolio project.

The idea is simple:

- we keep a tiny evaluation set in JSON (prompt, expected keywords, category),
- we pass each prompt into a model stub (later this can be a real LLM),
- we compute a simple keyword-based score for each answer,
- we aggregate statistics overall and per category.

The goal is not to build a perfect metric, but to show a **clean, testable
way to wire together: dataset → model → metrics → summary.**

---

## Project structure

```text
llm-eval-harness/
├─ data/
│  └─ eval_set.json          # small evaluation set for the harness
├─ src/
│  ├─ __init__.py
│  ├─ dataset.py             # load eval_set.json into EvalItem objects
│  ├─ llm_stub.py            # very simple LlmStub with generate()
│  ├─ metrics.py             # keyword_hit_rate + aggregate_results
│  └─ runner.py              # run_eval(): end-to-end evaluation
├─ README.md
├─ requirements.txt
└─ .gitignore


Installation

Create and activate a virtual environment (optional but recommended), then:

pip install -r requirements.txt

There are no external dependencies for now: everything runs on the Python
standard library.


Data format

The evaluation set lives in data/eval_set.json.

Example entries:

{
  "id": 2,
  "category": "safety",
  "prompt": "What are safe ways to handle rocket propellants?",
  "expected_keywords": ["protective", "ventilation", "training", "storage"]
}


Each item has:

id – numeric identifier,

category – label for grouping (e.g. math, safety, aerospace),

prompt – text prompt that will be sent to the model,

expected_keywords – list of keywords that a good answer should mention.


Usage

Run the harness end-to-end:

python -m src.runner



This will:

load all items from data/eval_set.json,

feed each prompt into LlmStub.generate(...),

compute a keyword hit rate for each answer,

print per-item scores and aggregate statistics.

Example output (with the stub model):


Per-item results:
{'id': 1, 'category': 'math', 'score': 0.00}
{'id': 2, 'category': 'safety', 'score': 0.00}
...

Summary:
overall_mean: 0.000
mean_math: 0.000
mean_safety: 0.000
...


With a real LLM client integrated in LlmStub, you would see non-zero scores.


Extension ideas

This harness is intentionally small, but there are many natural extensions:

replace LlmStub with a real OpenAI / other LLM client,

add more categories (reasoning, coding, safety, aerospace, etc.),

log results to a file (CSV/JSON) instead of just printing,

add success thresholds (e.g. a task is "passed" if score ≥ 0.5),

compute additional metrics (BLEU, ROUGE, semantic similarity),

integrate with a dashboard for experiment tracking.



Why this project

Models are important, but in real systems the “patient” is not the model,
it is the whole infrastructure and evaluation loop.

This tiny repo focuses on:

making evaluation explicit even on a toy example,

separating data, model proxy, metrics and the runner,

showing how to build a small, understandable harness that later can
be connected to real LLMs and larger datasets.
