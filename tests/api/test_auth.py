from fastapi import status
from fastapi.testclient import TestClient
from tests.utils.utils import random_email, random_lower_string

users_prefix = "/api/v1/users"
auth_prefix = "/api/v1/auth"

def test_unauthenticated_user_cant_update(client: TestClient):
    response = client.put(users_prefix+"/update")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'detail' in response.json()

def test_unauthenticated_user_cant_delete(client: TestClient):
    response = client.delete(users_prefix+"/delete")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'detail' in response.json()

def test_unauthenticated_user_cant_see_profile(client: TestClient):
    response = client.get(users_prefix+"/me")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'detail' in response.json()

def test_incorrect_credentials(client: TestClient):
    email = random_email()
    password = random_lower_string()
    data = {"username": email, "password": password}
    response = client.post(auth_prefix+"/login", json=data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'detail' in response.json()
