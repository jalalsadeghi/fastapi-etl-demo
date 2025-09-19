# tests/conftest.py
import asyncio
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import Base, async_engine

# IMPORTANT: import models so tables are registered on Base.metadata
import app.models  # noqa: F401

@pytest.fixture(scope="session", autouse=True)
def init_db():
    async def _create():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    async def _drop():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    asyncio.get_event_loop().run_until_complete(_create())
    yield
    asyncio.get_event_loop().run_until_complete(_drop())

@pytest.fixture
def client():
    # Context manager triggers FastAPI startup/shutdown too (harmless)
    with TestClient(app) as c:
        yield c
