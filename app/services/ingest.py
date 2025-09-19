# =============================
# app/services/ingest.py
# =============================
from __future__ import annotations
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models import WeatherReading

OPEN_METEO_URL = (
    "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
)

async def fetch_weather(lat: float, lon: float) -> float | None:
    url = OPEN_METEO_URL.format(lat=lat, lon=lon)
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url)
        r.raise_for_status()
        data = r.json()
        return data.get("current", {}).get("temperature_2m")

async def save_reading(db: AsyncSession, *, lat: float, lon: float, temp_c: float | None, location_name: str | None):
    rec = WeatherReading(lat=lat, lon=lon, temp_c=temp_c, location_name=location_name)
    db.add(rec)
    await db.commit()
    await db.refresh(rec)
    return rec