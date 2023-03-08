from fastapi import status
from fastapi.testclient import TestClient

def test_if_status_are_ok(client: TestClient):
    response = client.get("/api/v1/status")
    
    assert response.status_code == status.HTTP_200_OK
    assert 'success' in response.json()
    assert 'version' in response.json()
