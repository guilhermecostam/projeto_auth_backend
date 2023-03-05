from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def save(db: Session, user: User) -> none:
        if user.id:
            db.merge(user)
        else:
            db.add(user)
        db.commit()

    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        user = db.query(User).filter(User.id == id).first()
        if user is not None:
            db.delete(user)
            db.commit()