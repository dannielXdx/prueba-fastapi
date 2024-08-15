from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the JWT Auth API"}
