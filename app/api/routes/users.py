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

@router.get("/{id}", response_model=UserResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    user = UserRepository.find_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )

    return UserResponse.from_orm(user)
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )
    UserRepository.delete_by_id(db, id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)