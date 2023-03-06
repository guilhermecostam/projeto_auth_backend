from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.address import Address
from app.database.session import get_db
from app.database.base_model import Base
from app.repositories.user_repository import UserRepository
from app.repositories.address_repository import AddressRepository
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.schemas.address import AddressResponse, AddressCreate, AddressUpdate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, address: AddressCreate, db: Session = Depends(get_db)):
    address = AddressRepository.save(db, Address(**address.dict()))
    user.address_id = address.id
    user = UserRepository.save(db, User(**user.dict()))

    return UserResponse.from_orm(user)

@router.get("/{id}")
def find_by_id(id: int, db: Session = Depends(get_db)):
    user = UserRepository.find_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )

    results = {
        "user": UserResponse.from_orm(user),
        "address": AddressResponse.from_orm(user.address),
    }

    return results

@router.put("/{id}", response_model=UserResponse)
def update(
    id: int,
    user: UserUpdate,
    address: AddressUpdate,
    db: Session = Depends(get_db)
):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )
    user = UserRepository.save(db, User(id=id, **user.dict()))
    address.id = user.address_id
    AddressRepository.save(db, Address(**address.dict()))

    return UserResponse.from_orm(user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )
    UserRepository.delete_by_id(db, id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)