from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, HttpUrl


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    picture: Optional[HttpUrl] = None


class UserCreate(UserBase):
    google_sub: str


class UserRead(UserBase):
    id: UUID
    google_sub: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
