from fastapi.testclient import TestClient

def test_if_status_are_ok(client: TestClient):
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert 'success' in response.json()
    assert 'version' in response.json()
