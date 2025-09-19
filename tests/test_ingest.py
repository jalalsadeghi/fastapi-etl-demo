# =============================
# tests/test_ingest.py
# =============================
import pytest
import app.routers.ingest as ingest_router

@pytest.mark.parametrize("lat,lon", [(50.94, 6.96)])
def test_ingest_weather(lat, lon, monkeypatch, client):
    async def fake_fetch_weather(lat: float, lon: float):
        return 21.5
    monkeypatch.setattr(ingest_router.svc, "fetch_weather", fake_fetch_weather)

    payload = {"lat": lat, "lon": lon, "location_name": "Cologne"}
    r = client.post("/ingest/weather", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["temp_c"] == 21.5