### 🎯**How do you connect MySQL with FastAPI?**
* I connect FastAPI to MySQL using **SQLAlchemy ORM** with a MySQL driver such as **PyMySQL**, create an engine and session factory, and inject the database session into API routes using FastAPI's Depends().
  
#### Steps
```python
# 1. Install packages
pip install fastapi uvicorn sqlalchemy pymysql

# 2. Create database URL
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/fastapi_db"

# 3. Create SQLAlchemy engine
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

# 4. Create session
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 5. Create FastAPI database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 6. Use it in an API
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```
<div style="page-break-before: always;"></div>

### 🎯**How do you connect PostgreSQL with FastAPI?**
* I connect PostgreSQL with FastAPI using SQLAlchemy and the Psycopg2/Psycopg driver, create an engine and session, and inject the database session into routes using FastAPI's dependency injection.

#### Steps
```python
# 1. Install packages
pip install fastapi uvicorn sqlalchemy psycopg2-binary

# 2. Create database URL
DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"

# 3. Create SQLAlchemy engine
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

# 4. Create session
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 5. Create FastAPI database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 6. Use it in an API
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return {"message": "Connected to PostgreSQL"}
```

### **What is a Database Session?**
* A database session is a temporary connection between the application and the database that is used to perform database operations such as Create, Read, Update, and Delete (CRUD). It manages transactions and ensures proper communication with the database.

#### Why do we need a Session?
* Executes database queries.
* Tracks changes to objects.
* Manages transactions (commit, rollback).
* Closes the connection after use.
* Prevents connection leaks.

#### Session Lifecycle
```python
Create Session
      ↓
Execute Queries
      ↓
Commit / Rollback
      ↓
Close Session
```

### What is ORM?
* **ORM (Object-Relational Mapping)** is a technique that allows us to **interact with a database using programming language objects** instead of writing SQL queries directly.
* ORM Python objects/classes ko database tables ke saath map karta hai.
* FastAPI khud ORM nahi hai.:- SQLAlchemy, Django ORM, Tortoise ORM.

#### Example
* Without ORM
```python
# Aap directly SQL likhte ho:
cursor.execute(
    "SELECT * FROM users WHERE id = 1"
)
```
* With ORM — SQLAlchemy
```python
user = db.query(User).filter(User.id == 1).first()
```

#### Benefits of ORM
* SQL queries kam likhni padti hain
* Python objects ke through database access
* Code more maintainable/readable
* Relationships handle karna easier
* Database operations abstract ho jaate hain