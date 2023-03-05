from sqlalchemy import Column, Integer, String, Text
from app.database.base_model import Base

class Address(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    country: str = Column(String(255), nullable=False)
    state: str = Column(String(255), nullable=False)
    city: str = Column(String(255), nullable=False)
    zipcode: str = Column(String(255), nullable=False)
    street: int = Column(String(255), nullable=False)
    number: int = Column(String(255), nullable=False)
    complement: int = Column(Text, nullable=True)
