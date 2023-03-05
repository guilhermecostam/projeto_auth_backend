from pydantic import BaseModel

class Address(BaseModel):
    id: int
    country: str
    state: str
    city: str
    zipcode: str
    street: str
    number: str
    complement: str

    class Config:
        orm_mode = True
