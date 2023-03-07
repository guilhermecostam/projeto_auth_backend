from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from app.models.user import User
from app.repositories.user_repository import UserRepository

def check_unique_fields(db: Session, user: User) -> None:
    if UserRepository.find_by_username(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        )
    elif UserRepository.find_by_username(db, user.cpf):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this CPF already exists.",
    )
    elif UserRepository.find_by_username(db, user.pis):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this PIS already exists.",
    )