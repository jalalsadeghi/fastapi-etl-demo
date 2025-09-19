# FastAPI ETL Demo

Small demo aligned with API integration + data processing interviews.

## What it does
- POST `/ingest/weather` → fetches current temperature from Open‑Meteo for the given coordinates, stores a row in DB, and returns it.
- GET `/health` → health check.

## Run locally (Docker)
```bash
docker compose up --build
# open http://localhost:8000/docs
```

## Run tests (locally)
```bash
pip install -r requirements.txt
pytest -q
```

## CI (GitHub Actions)
- Runs pytest on Python 3.11 (sqlite).
- Builds Docker image.

## Notes
- Uses async SQLAlchemy and aiosqlite by default to keep CI simple.
- Switch to Postgres by setting `DATABASE_URL=postgresql+asyncpg://...` and adding `asyncpg`.
