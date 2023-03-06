from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.models.user import User
from app.database.session import get_db
from app.database.base_model import Base
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserResponse, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(request: UserCreate, db: Session = Depends(get_db)):
    user = UserRepository.save(db, User(**request.dict()))
    return UserResponse.from_orm(user)