# =============================
# app/schemas.py
# =============================
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional

class IngestRequest(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    location_name: Optional[str] = None

class WeatherOut(BaseModel):
    id: int
    location_name: Optional[str]
    lat: float
    lon: float
    temp_c: Optional[float]

    class Config:
        from_attributes = True