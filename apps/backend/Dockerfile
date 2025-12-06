# Builder stage: install dependencies and build app
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

# Copy dependency files to leverage cache
COPY pyproject.toml uv.lock ./

# Install production dependencies only
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copy application code
COPY . .

# Install project dependencies (production)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Runner stage: minimal image for production
FROM python:3.14-slim-bookworm AS runner

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Create non-root user
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser

WORKDIR /app

# Copy virtualenv and app from builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/src /app/src

# Switch to non-root user
USER appuser

EXPOSE 8000

# Start FastAPI
CMD ["fastapi", "run", "src/app/main.py", "--port", "8000", "--host", "0.0.0.0"]
