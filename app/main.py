# =============================
# app/main.py
# =============================
from __future__ import annotations
import asyncio
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from .db import Base, async_engine
from .routers import ingest as ingest_router

app = FastAPI(title="FastAPI ETL Demo")
app.include_router(ingest_router.router)

# Create tables on startup (simple demo; for production use migrations)
@app.on_event("startup")
async def on_startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)