# =============================
# app/models.py
# =============================
from __future__ import annotations
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from .db import Base

class WeatherReading(Base):
    __tablename__ = "weather_readings"

    id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String(100), nullable=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    temp_c = Column(Float, nullable=True)