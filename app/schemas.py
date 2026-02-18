# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 16:57:28
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-02-06 17:04:54
from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    email: EmailStr
    name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True