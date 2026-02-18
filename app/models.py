# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 16:57:09
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-02-16 17:18:01
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .db import Base

from typing import Optional
from pydantic import BaseModel, Field

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[int]= mapped_column(Integer, default=0)  # 0: user, 1: admin



class TrackingInfo3Base(BaseModel):
    id_despacho: Optional[int] = Field(None)
    numero_guia: Optional[str] = None
    ode: Optional[str] = None
    numero_guia: Optional[str] = None
    cliente: Optional[str] = None
    direccion: Optional[str] = None
    fecha_creacion: Optional[str] = None
    fecha_inicio: Optional[str] = None
    transporte: Optional[str] = None
    observacion: Optional[str] = None
    comentario: Optional[str] = None
    fecha_estado: Optional[str] = None
    estado: Optional[str] = None
    estado_penultimo: Optional[str] = None
    estado_penultimo_1: Optional[str] = None
    quarto_estado: Optional[str] = None
    quinto_estado: Optional[str] = None
    sexto_estado: Optional[str] = None
    septimo_estado: Optional[str] = None
    octavo_estado: Optional[str] = None
    peso: Optional[str] = None

    # Las columnas de tiempo/fecha reales las puedes manejar como strings ISO
    # o como datetime/time con validación. Aquí las dejo opcionales como str.
    # Si luego migras a tipos reales, ajustamos los tipos Pydantic.

class TrackingInfo3Create(TrackingInfo3Base):
    # Si la PK compuesta es obligatoria al crear:
    id_despacho: int
    numero_guia: str

class TrackingInfo3Update(TrackingInfo3Base):
    pass

class TrackingInfo3Out(TrackingInfo3Base):
    class Config:
        from_attributes = True  # pydantic v2: permite model -> schema
