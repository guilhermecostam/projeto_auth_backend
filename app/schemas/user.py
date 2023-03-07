from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, ValidationError, validator

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.user_repository import UserRepository

db: Session = Depends(get_db)

class UserBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    pis: str

    @validator('cpf', 'pis')
    def must_be_min_14_length(cls, v):
        if len(v) > 14:
            raise ValueError('must be less than 14')
        return v.title()

class UserCreate(UserBase):
    password: str
    address_id: Optional[int]

class UserUpdate(UserBase):
    address_id: int
    pass

class UserResponse(UserBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
