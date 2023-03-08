from fastapi.testclient import TestClient
from app.core.settings import settings

route_prefix = "/api/v1/users"

def test_unauthenticated_user_cant_update(client: TestClient):
    response = client.put(route_prefix+"/update")
    assert response.status_code == 401
    assert 'detail' in response.json()

def test_unauthenticated_user_cant_delete(client: TestClient):
    response = client.delete(route_prefix+"/delete")
    assert response.status_code == 401
    assert 'detail' in response.json()

def test_unauthenticated_user_cant_see_profile(client: TestClient):
    response = client.get(route_prefix+"/me")
    assert response.status_code == 401
    assert 'detail' in response.json()
