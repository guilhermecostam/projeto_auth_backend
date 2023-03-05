from pydantic import BaseModel, SecretStr

class User(BaseModel):
    id: int
    name: str
    email: str
    cpf: str
    pis: str
    password: SecretStr
    address_id: int

    class Config:
        orm_mode = True