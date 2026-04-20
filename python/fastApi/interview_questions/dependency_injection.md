### What is dependency injection in FastAPI? How does it work?
- Dependency injection in FastAPI allows you to manage dependencies that can be injected into your endpoints. These dependencies can be things like database connections, authentication services, or other reusable services.
```python
from fastapi import Depends

def get_db():
    db = DatabaseConnection()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
async def read_items(db: DatabaseConnection = Depends(get_db)):
    items = db.fetch_items()
    return items
```
- In this example, the **get_db** function provides a database connection that is automatically injected into the read_items endpoint.



### what is Dependency Injection in FastAPI?
* Dependency Injection is a design pattern where components receive their dependencies from external sources rather than creating them internally. FastAPI has a powerful dependency injection system.
```python
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Assume this is your database setup
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# 1. Define the dependency: A function that provides a database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Use `yield` to allow for cleanup after the request
    finally:
        db.close() # The session is closed automatically after the endpoint completes

@app.get("/users/")
# 2. Declare the dependency in your endpoint
def read_users(db: Session = Depends(get_db)):
    # 3. FastAPI injects the 'db' session, which you can now use
    users = db.query(User).all()
    return users
```

#### Benefits:
* Code reusability
* Easy testing
* Separation of concerns
* Automatic validation