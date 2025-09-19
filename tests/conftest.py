# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    # Using context manager triggers startup/shutdown events
    with TestClient(app) as c:
        yield c
