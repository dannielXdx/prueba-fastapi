from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

Base.metadata.create_all(bind=engine)

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
