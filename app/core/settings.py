import os
from dotenv import load_dotenv
from functools import lru_cache
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    APP_VERSION: str = os.getenv('APP_VERSION')
    API_V1_PREFIX: str = os.getenv('API_V1_PREFIX')

    DB_URI: str = os.getenv('MYSQL_URI')
    DB_HOST: str = os.getenv('MYSQL_HOSTNAME')
    DB_PORT: str = os.getenv('MYSQL_PORT')
    DB_USER: str = os.getenv('MYSQL_USER')
    DB_PASSWORD: str = os.getenv('MYSQL_PASSWORD')
    DB_NAME: str = os.getenv('MYSQL_DATABASE')

    SQLALCHEMY_URI_CONN: str = "{0}{1}:{2}@{3}:{4}/{5}".format(
        DB_URI,
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )

    class Config:
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()