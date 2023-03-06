from sqlalchemy.orm import Session
from app.models.address import Address

class AddressRepository:
    @staticmethod
    def save(db: Session, address: Address) -> Address:
        if address.id:
            db.merge(address)
        else:
            db.add(address)
        db.commit()

        return address

    @staticmethod
    def find_by_id(db: Session, id: int) -> Address:
        return db.query(Address).filter(Address.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Address).filter(Address.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        address = db.query(Address).filter(Address.id == id).first()
        if address is not None:
            db.delete(address)
            db.commit()