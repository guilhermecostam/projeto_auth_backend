from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    pis: str
    address_id: int

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
