# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 17:01:27
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-02-16 17:20:34
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select
from .db import engine, Base, get_session
from .models import User
from .schemas import UserIn, UserOut

app = FastAPI(title="FastAPI + Postgres (async)")

@app.on_event("startup")
async def on_startup():
    # Crear tablas si no existen (para demo/bench). En producción usar Alembic.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok1"}

@app.get("/version")
async def version(session: AsyncSession = Depends(get_session)):
    # Devuelve la versión de Postgres para validar conectividad
    result = await session.execute(text("SELECT version()"))
    ver = result.scalar()
    return {"postgres_version": ver}

@app.post("/users", response_model=UserOut, status_code=201)
async def create_user(data: UserIn, session: AsyncSession = Depends(get_session)):
    user = User(email=data.email, name=data.name)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(404, "User not found")
    return user



@app.post("/tracking", response_model=TrackingInfo3Out)
async def create_tracking(
    payload: TrackingInfo3Create,
    session: AsyncSession = Depends(get_session),
):
    repo = TrackingInfo3Repository(session)
    try:
        obj = await repo.create(payload.model_dump(exclude_unset=True))
        await session.commit()
        await session.refresh(obj)
        return obj
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tracking/{id_despacho}/{numero_guia}", response_model=TrackingInfo3Out)
async def get_tracking(
    id_despacho: int,
    numero_guia: str,
    session: AsyncSession = Depends(get_session),
):
    repo = TrackingInfo3Repository(session)
    obj = await repo.get(id_despacho, numero_guia)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj

@app.patch("/tracking/{id_despacho}/{numero_guia}")
async def update_tracking(
    id_despacho: int,
    numero_guia: str,
    payload: TrackingInfo3Update,
    session: AsyncSession = Depends(get_session),
):
    repo = TrackingInfo3Repository(session)
    count = await repo.update(id_despacho, numero_guia, payload.model_dump(exclude_unset=True))
    if count == 0:
        raise HTTPException(status_code=404, detail="No encontrado")
    await session.commit()
    return {"updated": count}

@app.delete("/tracking/{id_despacho}/{numero_guia}")
async def delete_tracking(
    id_despacho: int,
    numero_guia: str,
    session: AsyncSession = Depends(get_session),
):
    repo = TrackingInfo3Repository(session)
    count = await repo.delete(id_despacho, numero_guia)
    if count == 0:
        raise HTTPException(status_code=404, detail="No encontrado")
    await session.commit()
    return {"deleted": count}
