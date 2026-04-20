### Create schema file
- main.py
```python
from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv
import os

from database.connection import engine, Base
import models  # 👈 this loads all models

from database.connection import SessionLocal
from database.seeders.role_seeder import seed_roles

from routes import genral_router, role_router, auth_router

load_dotenv()

# app = FastAPI()  # This is the default configuration
app = FastAPI(
    title=os.getenv("PROJECT_NAME"),
    version=os.getenv("PROJECT_VERSION"))  # This is the custom configuration


@app.on_event("startup")
def run_seeders():
    db = SessionLocal()
    try:
        seed_roles(db)
    finally:
        db.close()


# Base.metadata.create_all(bind=engine)
app.include_router(genral_router)
app.include_router(role_router)
app.include_router(auth_router)
```