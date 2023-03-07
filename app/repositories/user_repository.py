from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.address_repository import AddressRepository

class UserRepository:
    @staticmethod
    def save(db: Session, user: User) -> User:
        if user.id:
            db.merge(user)
        else:
            db.add(user)
        db.commit()

        return user

    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def find_by_username(db: Session, username: str) -> User:
        return db.query(User).filter(
            (User.email == username) |
            (User.cpf == username) |
            (User.pis == username)
        ).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        user = db.query(User).filter(User.id == id).first()
        if user is not None:
            AddressRepository.delete_by_id(db, user.address_id)
            db.delete(user)
            db.commit()