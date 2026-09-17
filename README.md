# mini-inference-engine

A small hand-written inference engine for causal language models, built up one
harness at a time.

## Setup

```bash
uv sync
```

`uv sync` creates `.venv`, installs the dependencies, and installs this project
itself in editable mode. The editable install matters: it puts the project root
on `sys.path`, which makes the top-level packages (`base`, `generate`, `harness`)
importable from anywhere, so a harness can do:

```python
from generate.greedy_generate import generate_greedy
```

even when it is launched by file path.

## Secrets (`HF_TOKEN`)

Secrets live in a git-ignored `.env` file at the project root:

```bash
cp .env.example .env
# then edit .env and paste your token
```

`.env` is loaded automatically — **no import and no flag required** — by
`sitecustomize.py` at the project root. Because the project is installed in
editable mode, Python imports `sitecustomize` at interpreter startup, so every
harness (current and future) runs with the token already in the environment:

```bash
uv run harness/greedy_generation_harness.py   # authenticated
```

Precedence and safety:

- A variable already exported in your shell **wins** over `.env`
  (`load_dotenv(..., override=False)`).
- A missing `.env` (or a missing `python-dotenv`) never prevents Python from
  starting.
- `.env` values are visible to Python only; they do not affect non-Python tools.

If you prefer explicit control instead of the automatic hook, both of these
load the same file:

```bash
uv run --env-file .env harness/greedy_generation_harness.py
UV_ENV_FILE=.env uv run harness/greedy_generation_harness.py
```

You can also load it explicitly in code:

```python
from base.env import load_env, hf_token

load_env()
print("authenticated as:", hf_token())
```

## Running a harness

```bash
uv run harness/greedy_generation_harness.py
```

or, equivalently, as a module:

```bash
uv run python -m harness.greedy_generation_harness
```

## Project layout

```
base/        shared model loading and environment helpers
generate/    generation algorithms (the part you implement)
harness/     runnable checks that compare your code against a reference
```
