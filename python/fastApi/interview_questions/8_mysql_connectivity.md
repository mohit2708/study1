### Install Packages
* Install sqlalchemy -> sql orm hai
```python
pip install sqlalchemy // it is mandatory for any database
```
* install PyMySQL
```python
pip install PyMySQL
```

### add code in .env file
```python
# Databse Info
MY_SQL_USER=root
MY_SQL_PASSWORD=
MY_SQL_SERVER=localhost
MY_SQL_PORT=
MY_SQL_DATABASE=profile_fastapi
```

### MySql Connection
* create **connection.py** file in created directory like **database folder**
```python
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

MY_SQL_USER     = os.getenv("MY_SQL_USER")
MY_SQL_SERVER   = os.getenv("MY_SQL_SERVER")
MY_SQL_PASSWORD = os.getenv("MY_SQL_PASSWORD")
MY_SQL_PORT     = os.getenv("MY_SQL_PORT")
MY_SQL_DATABASE = os.getenv("MY_SQL_DATABASE")

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/profile_fastapi"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{MY_SQL_USER}:@{MY_SQL_SERVER}/{MY_SQL_DATABASE}"

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator:   #new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
```

### Connect database from mysql
* create database.py file in same directory like databse folder
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession

SQLITEADATABASE_URL = "sqlite:///./sqllite_app.db"
MYSQLDATABASE_URL = "mysql://root:@localhost/fastapi"   # mysql://username:password@host/tablename

engine = create_engine(SQLITEADATABASE_URL, connect_args={"check_same_thread":False})  # its line only, jab sqllite se connectivity ho.
engine = create_engine(MYSQLDATABASE_URL)

# Regular synchronous session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```


### another
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

### Connection with sql lite
- **install the package:-** 
```python
pip install sqlalchemy
```
- stacture
```python
database/
    __init__.py
    connection.py
models/
    __init__.py 👈 import models here
    user.py
main.py
```
- 📁 1️⃣ database/connection.py
  - 📌 This will create the SQLite file inside the database folder
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./database/app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ✅ DB Dependency here
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
- 📁 2️⃣ models/user.py
```python
from sqlalchemy import Column, Integer, String
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
```

- models/init.py ✅ IMPORTANT
```python
from .user import User
from .product import Product
from .order import Order
```

- 📁 3️⃣ main.py
```python
from fastapi import FastAPI
from database.connection import engine, Base
import models   # 👈 this loads all models

app = FastAPI()

Base.metadata.create_all(bind=engine)
```
```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.connection import engine, get_db, Base
from models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DB folder structure working ✅"}

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

### Now add to extra fields
- like created_at &  updated_at
- change in models/user.py
```python
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

```

#### 2 Optional: Reusable Base Model (Best Practice)
- database/base_model.py
```python
from sqlalchemy import Column, DateTime
from datetime import datetime

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```
- models/user.py
```python
from sqlalchemy import Column, Integer, String
from database.connection import Base
from database.base_model import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
```

#### Note
- If created_at and updated_at are not showing in SQLite, it means the table was created before you added those columns.
- SQLite **does not auto-update** schema when you change the model
  - Delete the old DB file **database/app.db** :- rm database/app.db
  - Run the app again:- uvicorn main:app --host 0.0.0.0 --port 8000
  - Now Base.metadata.create_all() will create the table with: ✔ created_at &  ✔ updated_at
  - In real projects ❌ never delete DB Use Alembic migrations to add new columns.

