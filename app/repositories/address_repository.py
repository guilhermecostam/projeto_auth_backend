from sqlalchemy.orm import Session
from app.models.address import Address

class AddressRepository:
    @staticmethod
    def save(db: Session, address: Address) -> None:
        if address.id:
            db.merge(address)
        else:
            db.add(address)
        db.commit()

    @staticmethod
    def find_by_id(db: Session, id: int) -> Address:
        return db.query(Address).filter(Address.id == id).first()
