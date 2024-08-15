from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "email": "testuser@example.com",
              "password": "password"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_login_user():
    response = client.post(
        "/auth/login",
        data={"username": "testuser", "password": "password"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_verify_token():
    response = client.post("/auth/login", data={"username": "testuser",
                                                "password": "password"})
    access_token = response.json()["access_token"]
    response = client.get("/auth/verify-token", headers={
        "Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json() == {"status": "Token is valid"}


def test_refresh_token():
    response = client.post("/auth/login", data={"username": "testuser",
                                                "password": "password"})
    access_token = response.json()["access_token"]
    response = client.post("/auth/refresh", headers={
        "Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_logout():
    response = client.post("/auth/login", data={"username": "testuser",
                                                "password": "password"})
    access_token = response.json()["access_token"]
    response = client.post("/auth/logout", headers={
        "Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "Logged out"}
