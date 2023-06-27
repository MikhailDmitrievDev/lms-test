from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: Enum


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
