# interview-tracker

A web app to track job applications and selection processes, built with FastAPI.

## Tech stack

| Tool      | Purpose                                        |
| --------- | ---------------------------------------------- |
| uv        | Python + dependency manager (creates `.venv`)  |
| Python    | 3.12 (pinned in `.python-version`, managed by uv) |
| FastAPI   | Web framework, served by Uvicorn               |
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
uv run interview-tracker
```

Equivalent alternatives:

```sh
uv run python -m interview_tracker
uv run uvicorn interview_tracker.main:app --reload
```

Then open http://127.0.0.1:8000 — the interactive API docs are at `/docs`,
and a health check at `/health`. The dev server auto-reloads on code changes.

## Everyday commands

All commands run through `uv run`, so they always use the project venv.

```sh
uv run pytest                 # run tests
uv run ruff check .           # lint
uv run ruff format .          # format code
uv run mypy                   # type-check src/ and tests/
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
app/documentation/       # domain diagrams (PNGs)
src/interview_tracker/   # application source code
    main.py              # FastAPI app entry point + run() for the server
    __main__.py          # enables `python -m interview_tracker`
templates/               # Jinja2 HTML templates
static/                  # CSS / JS assets
tests/                   # pytest test suite
pyproject.toml           # project metadata, dependencies, tool config
uv.lock                  # locked dependency versions (commit this)
.python-version          # Python version pin used by uv
```

Source code lives under `src/` ([src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)):
the package is installed into the venv in editable mode, so imports work the
same in tests as in production.

## Definitions

Job application: A job application is a formal request and set of documents—such as a digital or paper form, CV, and cover letter—that you submit to an employer to show you want an open position

Selection process: The selection process is a structured hiring method used by organisations to evaluate job applicants, specifically involving screening applications, conducting interviews, and administering tests to choose the most qualified candidate.
