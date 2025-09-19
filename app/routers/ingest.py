# =============================
# app/routers/ingest.py
# =============================
from __future__ import annotations
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_db
from ..schemas import IngestRequest, WeatherOut
# from ..services.ingest import fetch_weather, save_reading  # ← delete
from ..services import ingest as svc

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.post("/ingest/weather", response_model=WeatherOut)
async def ingest_weather(payload: IngestRequest, db: AsyncSession = Depends(get_db)):
    temp = await svc.fetch_weather(payload.lat, payload.lon)
    rec = await svc.save_reading(
        db, lat=payload.lat, lon=payload.lon, temp_c=temp, location_name=payload.location_name
    )
    return rec