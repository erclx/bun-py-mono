# Bun-Py Backend

The FastAPI backend service for the `bun-py-mono` monorepo. Pre-configured with `uv`, Ruff, and modern tooling.

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
- **Pre-commit**: Automates checks on git commit (linting and commit messages)

## Quick Start

```bash
uv sync
just setup
```

The `just setup` command will install dependencies and configure the git hooks.

## Scripts

We use `just` to run commands.

```bash
just dev        # Start dev server with hot reload
just fix        # Format & fix with Ruff
just lint       # Check style (Ruff) + types (MyPy)
just test       # Run tests
just test-cov   # Run tests with coverage report
just clean      # Remove cache & build files
just setup      # Sync deps & install hooks
```

## Git Hooks & Pre-commit

We use `pre-commit` to enforce code quality and `commit-msg` hooks to enforce conventional commits.

### Manual Setup / Useful Commands:

```bash
# Manually run checks on the entire repo
pre-commit run --all-files

# Update the pre-commit tool itself
uv tool upgrade pre-commit

# Update the versions in .pre-commit-config.yaml
pre-commit autoupdate
```

### Hook Types:
* `pre-commit`: Runs on file changes (linting/formatting).
* `commit-msg`: Runs on the commit message itself.

## Project Conventions

### Dependency Management

We use `uv` exclusively. Do not use `pip` manually.

* Add lib: `uv add <package>`
* Add dev lib: `uv add --dev <package>`
* Sync: `uv sync`

### File Structure

* `src/app/`: Application source code
* `tests/`: Test files (mirrors app structure)

### Commit Convention

Uses Conventional Commits.

* `feat: add health check endpoint`
* `fix: resolve typing error in main`
* `chore: update uv lockfile`
