from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello there big man"}

def test_read_apis_router():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Fetch working :-)"}
