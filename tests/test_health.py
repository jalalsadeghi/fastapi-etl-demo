# =============================
# tests/test_health.py
# =============================
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"