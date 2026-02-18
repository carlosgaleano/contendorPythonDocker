# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-16 15:39:49
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-02-16 15:56:48
import asyncio
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

def getenv_clean(key: str, default: str = "") -> str:
    val = os.getenv(key, default)
    return val.split("#", 1)[0].strip()  # elimina comentarios inline y espacios

async def main():
    load_dotenv()

    user = getenv_clean("POSTGRES_USER", "root")
    pwd  = getenv_clean("POSTGRES_PASSWORD", "carlos")
    db   = getenv_clean("POSTGRES_DB", "tracking")
    host = getenv_clean("POSTGRES_HOST", "host.docker.internal")
    port = getenv_clean("POSTGRES_PORT", "5432")

    # Loguea valores (repr muestra espacios/ocultos)
    print("HOST (repr):", repr(host))
    print("PORT (repr):", repr(port))

    url = f"postgresql+asyncpg://{user}:{pwd}@{host}:{port}/{db}"
    print("URL (masked):", url.replace(f":{pwd}@", ":*****@"))

    engine = create_async_engine(url, echo=True, pool_pre_ping=True)

    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("SELECT 1 ->", result.scalar())

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())