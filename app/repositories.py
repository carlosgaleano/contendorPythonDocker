# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-03-04 15:15:33
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-03-04 15:15:47

# app/repositories.py
from typing import Any, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from .models import TrackingInfo3

class TrackingInfo3Repository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any]):
        obj = TrackingInfo3(**data)
        self.session.add(obj)
        return obj

    async def get(self, id_despacho: int, numero_guia: str):
        stmt = (
            select(TrackingInfo3)
            .where(TrackingInfo3.id_despacho == id_despacho)
            .where(TrackingInfo3.numero_guia == numero_guia)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def list(self, limit: int = 100, offset: int = 0):
        stmt = select(TrackingInfo3).limit(limit).offset(offset)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def update(self, id_despacho: int, numero_guia: str, data: Dict[str, Any]):
        stmt = (
            update(TrackingInfo3)
            .where(TrackingInfo3.id_despacho == id_despacho)
            .where(TrackingInfo3.numero_guia == numero_guia)
            .values(**data)
        )
        result = await self.session.execute(stmt)
        return result.rowcount

    async def delete(self, id_despacho: int, numero_guia: str):
        stmt = (
            delete(TrackingInfo3)
            .where(TrackingInfo3.id_despacho == id_despacho)
            .where(TrackingInfo3.numero_guia == numero_guia)
        )
        result = await self.session.execute(stmt)
        return result.rowcount
