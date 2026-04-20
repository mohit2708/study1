### Create connection file
- databse/connection.py
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