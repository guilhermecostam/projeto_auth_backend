import os
import logging
from dotenv import load_dotenv
from typing import Callable, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.database.base_model import Base

load_dotenv()

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

    conn_str = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(
        os.getenv('MYSQL_USER'),
        os.getenv('MYSQL_PASSWORD'),
        os.getenv('MYSQL_HOSTNAME'),
        os.getenv('MYSQL_PORT'),
        os.getenv('MYSQL_DATABASE')
    )

    log.info("Connecting to the database...")
    engine = create_engine(conn_str, echo=False)
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
