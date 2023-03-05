import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(100), unique=True, nullable=False, index=True)
    cpf: str = Column(String(14), unique=True, nullable=False)
    pis: str = Column(String(14), unique=True, nullable=False)
    password: int = Column(String(255), nullable=False)
    address_id: int = Column(Integer, ForeignKey("addresses.id"))
    address = relationship("Address", back_populates="users")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )