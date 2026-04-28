# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and Python 3.13.9.

```bash
# Install dependencies
uv sync

# Run the development server
uv run python src/app.py

# Run all tests
uv run python -m unittest discover -s tests

# Run a single test file
uv run python -m unittest tests.test_app

# Run a single test case
uv run python -m unittest tests.test_app.AppTestCase.test_index
```

The app is available at `http://127.0.0.1:5000`.

## Architecture

This is a minimal Flask app with no database — course data lives as in-memory Python objects in `src/models.py`.

- `src/app.py` — creates the Flask app, registers URL rules, entry point
- `src/views.py` — view functions (thin: just render templates)
- `src/models.py` — `Course` dataclass and a hardcoded `courses` list
- `src/templates/` — Jinja2 templates; `layout.html` is the base that others extend via `{% block content %}`
- `src/static/css/styles.css` — all styles in a single file

Routes:
- `GET /` → `index` view → `index.html`
- `GET /course/<course_id>` → `course` view → `course.html`

Tests (`tests/test_app.py`) manually insert `src/` onto `sys.path` so imports resolve without installing the package.

## Development Workflow

### Add Unit Tests

- Whenever you add any changes add unit tests and run and make sure the tests passes.

### Verify Changes with Playwright (MANDATORY)

**After implementing any new feature, you MUST:**

1. Start the Flask application (if not already running - `python src/app.py`)
2. Use the Playwright MCP tool to connect to the application at `http://127.0.0.1:5000`
3. Navigate to and interact with the new feature to verify it works correctly
4. Take a screenshot of the working feature
5. Save the screenshot in the `test-output/` folder with a descriptive filename (e.g., `feature-name-verification-YYYY-MM-DD.png`)

This step ensures that all features are visually verified and provides documentation of the working state of the application.