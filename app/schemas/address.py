from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AddressBase(BaseModel):
    country: str
    state: str
    city: str
    zipcode: str
    street: str
    number: str
    complement: Optional[str] = None

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    id: Optional[int]
    pass

class AddressResponse(AddressBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
