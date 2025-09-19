# =============================
# tests/test_ingest.py
# =============================
import pytest
from fastapi.testclient import TestClient
from app.main import app
import app.routers.ingest as ingest_router

client = TestClient(app)

@pytest.mark.parametrize("lat,lon", [(50.94, 6.96)])  # Cologne
def test_ingest_weather(lat, lon, monkeypatch):
    async def fake_fetch_weather(lat: float, lon: float):
        return 21.5

    # Patch the symbol actually used by the router
    monkeypatch.setattr(ingest_router.svc, "fetch_weather", fake_fetch_weather)

    payload = {"lat": lat, "lon": lon, "location_name": "Cologne"}
    r = client.post("/ingest/weather", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["lat"] == lat
    assert data["lon"] == lon
    assert data["temp_c"] == 21.5