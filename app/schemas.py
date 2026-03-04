# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 16:57:28
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-03-04 15:44:56
# app/schemas.py
# -*- coding: utf-8 -*-
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

# ----- Users -----
class UserIn(BaseModel):
    email: EmailStr
    name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    model_config = {"from_attributes": True}


# ----- Tracking -----
class TrackingInfo3(BaseModel):
    id_despacho: Optional[int] = Field(default=None)
    numero_guia: Optional[str] = Field(default=None)
    ode: Optional[str] = None
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

class TrackingInfo3Create(TrackingInfo3):
    id_despacho: int
    numero_guia: str

class TrackingInfo3Update(TrackingInfo3):
    pass

class TrackingInfo3Out(TrackingInfo3):
    model_config = {"from_attributes": True}