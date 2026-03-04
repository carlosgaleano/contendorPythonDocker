# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 16:57:09
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-03-04 15:44:04
# app/models.py
# -*- coding: utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .db import Base

# ---- Modelo de usuario (como ya lo tenías) ----
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[int] = mapped_column(Integer, default=0)  # 0: user, 1: admin


# ---- Modelo de Tracking (ORM) ----
class TrackingInfo3(Base):
    __tablename__ = "tracking_info_3"

    # Clave primaria compuesta (ajústalo si corresponde)
    id_despacho: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_guia: Mapped[str] = mapped_column(String(255), primary_key=True)

    ode: Mapped[str | None] = mapped_column(String(255), nullable=True)
    cliente: Mapped[str | None] = mapped_column(String(255), nullable=True)
    direccion: Mapped[str | None] = mapped_column(String(255), nullable=True)
    fecha_creacion: Mapped[str | None] = mapped_column(String(255), nullable=True)
    fecha_inicio: Mapped[str | None] = mapped_column(String(255), nullable=True)
    transporte: Mapped[str | None] = mapped_column(String(255), nullable=True)
    observacion: Mapped[str | None] = mapped_column(String(255), nullable=True)
    comentario: Mapped[str | None] = mapped_column(String(255), nullable=True)
    fecha_estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    estado_penultimo: Mapped[str | None] = mapped_column(String(255), nullable=True)
    estado_penultimo_1: Mapped[str | None] = mapped_column(String(255), nullable=True)
    quarto_estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    quinto_estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    sexto_estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    septimo_estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    octavo_estado: Mapped[str | None] = mapped_column(String(255), nullable=True)
    peso: Mapped[str | None] = mapped_column(String(255), nullable=True)