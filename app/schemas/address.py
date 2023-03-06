from typing import Optional
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
    pass

class AddressResponse(AddressBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
