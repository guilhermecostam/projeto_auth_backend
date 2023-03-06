from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    pis: str

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
