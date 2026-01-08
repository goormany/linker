FROM python:3.12-alpine AS builder
WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

FROM python:3.12-alpine
WORKDIR /app

COPY --from=builder /app/.venv ./.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY alembic.ini .python-version pytest.ini ./
COPY src/ ./src/
COPY tests/ ./tests/
COPY .env.test ./

RUN find /app/.venv -type d -name "__pycache__" -exec rm -rf {} + \
    && find /app/.venv -type f -name "*.pyc" -delete

EXPOSE 8000

RUN adduser -D -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["sh", "-c", "alembic upgrade head && exec python -m src.main"]