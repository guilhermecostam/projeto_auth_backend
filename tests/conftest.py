from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.database.session import get_db
from app.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield get_db()

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
