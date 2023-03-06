from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.models.user import User
from app.database.session import get_db
from app.database.base_model import Base
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserResponse, UserCreate, UserUpdate

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/login")
def login():
    return {
        "success": True
    }
