from fastapi.testclient import TestClient
from app.main import app
from app.core.settings import settings

# client = TestClient(app)

def test_if_status_are_ok(client: TestClient):
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "version": settings.APP_VERSION
    }