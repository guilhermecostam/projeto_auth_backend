import logging
from typing import Callable, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.database.base_model import Base
from app.core.settings import settings

__factory: Optional[Callable[[], Session]] = None
log = logging.getLogger("uvicorn")

def get_db() -> Session:
    db = create_session()
    try:
        yield db
    finally:
        db.close()

def global_init() -> None:
    global __factory

    if __factory:
        return

    log.info("Connecting to the database...")
    engine = create_engine(settings.SQLALCHEMY_URI_CONN, echo=False)
    __factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    from app.models.user import User
    from app.models.address import Address

    Base.metadata.create_all(engine)

def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method")

    session: Session = __factory()
    session.expire_on_commit = False

    return session
