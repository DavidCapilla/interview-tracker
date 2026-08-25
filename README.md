# interview-tracker

A web app to track job applications and selection processes, built with FastAPI.

## Tech stack

| Tool      | Purpose                                        |
| --------- | ---------------------------------------------- |
| uv        | Python + dependency manager (creates `.venv`)  |
| Python    | 3.12 (pinned in `.python-version`, managed by uv) |
| FastAPI   | Web framework, served by Uvicorn via FastAPI CLI |
| Jinja2    | HTML templating                                |
| pytest    | Tests                                          |
| ruff      | Linting and formatting                         |
| mypy      | Static type checking                           |

## Getting started

### 1. Install uv

macOS (Homebrew):

```sh
brew install uv
```

Other platforms: see the [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/).

### 2. Set up the project

From the repo root:

```sh
uv sync
```

That single command installs the pinned Python version if needed, creates a
`.venv`, installs all dependencies from `uv.lock` (including dev tools), and
installs this project in editable mode.

### 3. Run the app

```sh
uv run fastapi dev app/main.py
```

This starts the dev server with auto-reload on code changes.

Then open http://127.0.0.1:8000 — the interactive API docs are at `/docs`,
and a health check at `/health`.

## Everyday commands

All commands run through `uv run`, so they always use the project venv.

```sh
uv run pytest                 # run tests
uv run ruff check .           # lint
uv run ruff format .          # format code
uv run mypy                   # type-check app/ and tests/
```

Before pushing: make sure pytest, ruff, and mypy all pass.

### Adding a dependency

```sh
uv add <package>              # runtime dependency
uv add --group dev <package>  # dev-only dependency
```

This updates both `pyproject.toml` and `uv.lock`. Commit both.

## Project layout

```
app/                          # application source code
    main.py                   # FastAPI app definition
    __init__.py               # makes app a package
    documentation/            # domain diagrams (PNGs)
tests/                        # pytest test suite
    test_main.py              # smoke test for /health endpoint
pyproject.toml                # project metadata, dependencies, tool config
uv.lock                       # locked dependency versions (commit this)
.python-version               # Python version pin used by uv
```

Source code lives directly in `app/` — the FastAPI CLI runs it with
`app/main.py` as the entry point. Tests import from `app.main` and use
FastAPI's `TestClient` for verification.

## Definitions

Job application: A job application is a formal request and set of documents—such as a digital or paper form, CV, and cover letter—that you submit to an employer to show you want an open position

Selection process: The selection process is a structured hiring method used by organisations to evaluate job applicants, specifically involving screening applications, conducting interviews, and administering tests to choose the most qualified candidate.
