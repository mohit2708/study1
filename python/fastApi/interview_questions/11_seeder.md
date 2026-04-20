### Create Seeder
* Create folder seeder->seed_roles.py
* seed_roles.py file
```python
# seed_roles.py file as data delete then insert
from database.models.roles import Role

def seed_roles(db):
    # Retrieve all existing slugs from the database
    existing_slugs = {role.slug for role in db.query(Role).all()}
    
    # Define roles to insert
    roles = [
        {"id": 1, "slug": "super_admin", "name": "Super Admin"},
        {"id": 2, "slug": "admin", "name": "Admin"},
        {"id": 3, "slug": "customer", "name": "Customer"},
        {"id": 4, "slug": "staff", "name": "Staff"},
        {"id": 5, "slug": "sample", "name": "Sample"},
    ]
    
    # Filter roles to only those not already in the database
    roles_to_insert = [role_data for role_data in roles if role_data["slug"] not in existing_slugs]

    if roles_to_insert:
        for role_data in roles_to_insert:
            role = Role(**role_data)
            db.add(role)
        db.commit()
        print("New roles seeded successfully.")
    else:
        print("Roles already seeded, no new roles to add.")
```

### Change in main.py file for seeder
```python
from database.connection import engine, Base, SessionLocal # add SessionLocal

# add code after:- app = start_application()
@app.on_event("startup")
def add_seed_roles():
    db = SessionLocal()
    seed_roles(db)
    db.close()
```

### Run command
```python
Run the project 
```

### For seeder in alembic
- cretae role model models/role.py
```python
from sqlalchemy import Column, Integer, String, DateTime
from database.connection import Base
from datetime import datetime


class Role(Base):
  __tablename__ = "roles"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, nullable=False)
  slug = Column(String, unique=True, nullable=False)

  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime,
                      default=datetime.utcnow,
                      onupdate=datetime.utcnow)

```
- register role in models.init.py file
```python
from .user import User
from .role import Role
```

- Alembic migration
```python
alembic revision --autogenerate -m "create roles table"
alembic upgrade head
```

- create folder database/seeders/role_seeder.py
```python
from sqlalchemy.orm import Session
from models.role import Role

def seed_roles(db: Session):
    roles = [
        {
            "name": "admin",
            "slug": "admin"
        },
        {
            "name": "customer",
            "slug": "customer"
        },
        {
            "name": "student",
            "slug": "student"
        },
        {
            "name": "m",
            "slug": "m"
        },
    ]

    for r in roles:
        role = db.query(Role).filter(Role.slug == r["slug"]).first()
        if not role:
            db.add(Role(name=r["name"], slug=r["slug"]))

    # when name only
    # roles = ["admin", "customer", "student"]

    # for role_name in roles:
    #     role = db.query(Role).filter(Role.name == role_name).first()
    #     if not role:
    #         db.add(Role(name=role_name))

    db.commit()
```
- in main.py file
```python
from database.connection import SessionLocal
from database.seeders.role_seeder import seed_roles

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
```


### More than seeder
- Recommended Folder Structure
```python
app/
 ├── database/
 │    ├── connection.py
 │    ├── seeders/
 │    │     ├── __init__.py
 │    │     ├── role_seeder.py
 │    │     ├── user_seeder.py
 │    │     └── run_seeders.py   👈 main runner
```

- role_seeder.py
```python
from sqlalchemy.orm import Session
from app.models.role import Role

def seed_roles(db: Session):
    roles = [
        {"name": "admin", "slug": "admin"},
        {"name": "customer", "slug": "customer"},
        {"name": "student", "slug": "student"},
    ]

    for r in roles:
        role = db.query(Role).filter(Role.slug == r["slug"]).first()
        if not role:
            db.add(Role(name=r["name"], slug=r["slug"]))

    db.commit()
```

- user_seeder.py
```python
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role

def seed_users(db: Session):
    admin_role = db.query(Role).filter(Role.slug == "admin").first()

    if not admin_role:
        return  # roles must exist first

    user = db.query(User).filter(User.email == "admin@example.com").first()

    if not user:
        db.add(
            User(
                name="Admin",
                email="admin@example.com",
                role_id=admin_role.id
            )
        )
        db.commit()
```

- run_seeders.py
```python
from sqlalchemy.orm import Session
from .role_seeder import seed_roles
from .user_seeder import seed_users

def run_all_seeders(db: Session):
    seed_roles(db)   # first roles
    seed_users(db)   # then users (depends on roles)
```

- __init__.py
```python
from .run_seeders import run_all_seeders
```

- main.py mai call
```python
from database.seeders import run_all_seeders

@app.on_event("startup")
def run_seeders():
    db = SessionLocal()
    try:
        run_all_seeders(db)
    finally:
        db.close()
```

### Database > schemas > user.py
#### Create email validation
* insatll package for **duplicate email** exist
```python
pip install pydantic[email]
```

```python
# Database > schemas > user.py
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=255, description="The first name of the user")
    last_name: str = Field(..., min_length=1, max_length=255, description="The last name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., min_length=1, description="The password of the user")
```