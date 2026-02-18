# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 16:56:55
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-02-16 15:26:19

from __future__ import annotations

import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import declarative_base

# 1) Cargar variables de entorno ANTES de usarlas
load_dotenv()

PG_USER = os.getenv("POSTGRES_USER", "root")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD", "carlos")
PG_DB = os.getenv("POSTGRES_DB", "tracking")

# Si usas Docker Desktop en Windows/Mac, 'host.docker.internal' funciona.
# En Linux, agrega --add-host=host.docker.internal:host-gateway al 'docker run'
# o cambia a un nombre de servicio de la red docker (p. ej. 'postgres-1').
PG_HOST = os.getenv("POSTGRES_HOST", "host.docker.internal")
PG_PORT = os.getenv("POSTGRES_PORT", "5432")

# 2) URL asíncrona con asyncpg
DATABASE_URL = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

def _mask_url(url: str) -> str:
    # Enmascara la contraseña para logs
    # postgresql+asyncpg://user:*****@host:port/db
    try:
        prefix, rest = url.split("://", 1)
        creds, tail = rest.split("@", 1)
        if ":" in creds:
            user, _pwd = creds.split(":", 1)
            creds_masked = f"{user}:*****"
        else:
            creds_masked = creds
        return f"{prefix}://{creds_masked}@{tail}"
    except Exception:
        return url

print(">>> DATABASE_URL (masked):", _mask_url(DATABASE_URL))

# 3) Engine asíncrono
engine = create_async_engine(
    DATABASE_URL,
    echo=True,            # True para ver SQL; ponlo False en prod
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,   # para validar conexiones del pool
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session