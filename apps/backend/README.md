# UV Python Template

A web-first starter template for Python projects. Pre-configured with `uv`, FastAPI, Ruff, and modern tooling.
Clone it and start building.

## Disclaimer

This is opinionated. Use what works for you, ignore the rest, and stay consistent with your own choices.

## What's Included

### Core Stack

- **Python 3.14+**
- **uv** for blazing fast package management
- **FastAPI** for the web framework

### Testing

- **pytest** for unit and integration tests
- **pytest-cov** for coverage reporting

### Code Quality

- **Ruff**: Replaces Flake8, Black, and Isort for linting and formatting
- **MyPy**: Strict static type checking
- **Gitleaks**: Scans for secrets before committing

### Dev Experience

- **Just**: Command runner for common tasks
- **Pre-commit**: Automates checks on git commit
- **VS Code**: Pre-configured settings and extensions

## Quick Start

```bash
git clone <your-repo-url> my-project
cd my-project
uv sync
uv run pre-commit install
```

## Scripts

We use `just` to run commands.

```bash
just dev            # Start development server (hot reload)
just test           # Run tests with verbose output
just lint           # Lint code with Ruff and MyPy
just format         # Format code
just clean          # Remove cache and artifacts
just preview        # Build and run Docker image for local testing
```

*Note: If you don't use `just`, you can use `uv run <command>` directly.*

## Project Conventions

### Dependency Management

We use `uv` exclusively. Do not use `pip` manually.

- **Add lib:** `uv add <package>`
- **Add dev lib:** `uv add --dev <package>`
- **Sync:** `uv sync`

### File Structure

- `app/`: Application source code
- `tests/`: Test files (mirrors app structure)

### Commit Convention

Uses [Conventional Commits](https://www.conventionalcommits.org/).

- `feat: add health check endpoint`
- `fix: resolve typing error in main`
- `chore: update uv lockfile`
