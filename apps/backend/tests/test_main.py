from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check() -> None:
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok', 'mode': 'web-only'}
