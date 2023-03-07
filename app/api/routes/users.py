from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.models.user import User
from app.models.address import Address
from app.database.session import get_db
from app.database.base_model import Base
from app.core.security import get_password_hash
from app.core.validations import check_unique_fields
from app.repositories.user_repository import UserRepository
from app.repositories.address_repository import AddressRepository
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.schemas.address import AddressResponse, AddressCreate, AddressUpdate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, address: AddressCreate, db: Session = Depends(get_db)):
    check_unique_fields(db, user)
    address = AddressRepository.save(db, Address(**address.dict()))
    user.address_id = address.id
    user.password = get_password_hash(user.password)
    user = UserRepository.save(db, User(**user.dict()))

    return UserResponse.from_orm(user)

@router.get("/me")
def find_by_id(current_user: User = Depends(get_current_user)):
    results = {
        "user": UserResponse.from_orm(current_user),
        "address": AddressResponse.from_orm(current_user.address),
    }

    return results

@router.put("/update", response_model=UserResponse)
def update(
    user: UserUpdate,
    address: AddressUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not UserRepository.exists_by_id(db, current_user.id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )
    user = UserRepository.save(db, User(id=current_user.id, **user.dict()))
    address.id = user.address_id
    AddressRepository.save(db, Address(**address.dict()))

    return UserResponse.from_orm(user)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not UserRepository.exists_by_id(db, current_user.id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't found"
        )
    UserRepository.delete_by_id(db, current_user.id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)