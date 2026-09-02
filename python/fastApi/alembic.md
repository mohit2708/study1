|  No.  | Alembic Questions                            |
| :---: | -------------------------------------------- |
|       | [What is Alembic?](#what-is-alembic)         |
|       | [Why is Alembic used?](#why-is-alembic-used) |


### **What is Alembic?**
- Alembic is a database migration tool for SQLAlchemy.
- It helps you manage changes in your database schema (tables, columns, indexes, constraints) without manually writing SQL every time.
- It helps you:
  - ✔ Add new columns
  - ✔ Modify tables
  - ✔ Track schema versions
  - ✔ Avoid deleting DB ❌

### Why is Alembic used?
1. **Version Control for Database:-** Just like Git tracks code changes, Alembic tracks database changes.
```python
versions/
    001_create_users.py
    002_add_email_to_users.py
    003_create_roles.py
```
2. **Team Collaboration**
* If one developer creates a new table:
```python
alembic upgrade head
```
* Other developers can apply the same changes without manually updating their databases.
3. **Database Upgrade & Rollback**
```python
alembic upgrade head

# Rollback one version:
alembic downgrade -1

# Rollback to a specific version:
alembic downgrade abc123
```
4. **Automatic Migration Generation**
* Alembic compares SQLAlchemy models with the database and generates migration scripts.
```python
alembic revision --autogenerate -m "create roles table"
```


### Install alembic
* install package
```python
pip install alembic
```

### Initialize Alembic:
```python
alembic init alembic
```

### Change the code in env.py file
```python
from database.connection import Base
from database.connection import SQLALCHEMY_DATABASE_URL


from database.models import *
target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url",SQLALCHEMY_DATABASE_URL)
```
* **OR** alembi.ini file
```python
# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = mysql+pymysql://root:@localhost/profile_fastapi
```

### create Model
* Create init.py file
```python
from .user import *
from .role import *
```
```python
# User table
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from database.connection import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))  # Define foreign key relationship
    role = relationship("Role", back_populates="users")  # Define relationship with Role model
    first_name = Column(String(255))
    last_name = Column(String(255))
    user_name = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    zip_code = Column(String(255))
    is_active = Column(Boolean(), default=True)
    address = Column(String(255))
    country = Column(Integer)
    state = Column(Integer)
    city = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# role table
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from database.connection import Base

class Role(Base):
    __tablename__ = "roles"

    id          = Column(Integer, primary_key=True, index=True)
    slug        = Column(String(255), nullable=True)
    name        = Column(String(255), nullable=True)
    created_at  = Column(DateTime, default=datetime.utcnow)
    updated_at  = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    users = relationship("User", back_populates="role")  # Define reverse relationship with User model
```


### Sava data in two table
```python
# user table
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, Session
from database.connection import Base
from passlib.context import CryptContext

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))  # Define foreign key relationship
    role = relationship("Role", back_populates="users")  # Define relationship with Role model
    first_name = Column(String(255), nullable = True)
    last_name = Column(String(255))
    user_name = Column(String(255), unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255))
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_details = relationship("UserDetails", back_populates="user", uselist=False, cascade="all, delete") # Define relationship with UserDetails
```
```python
# user details table
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, Session
from database.connection import Base
from passlib.context import CryptContext

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))  # Define foreign key relationship
    role = relationship("Role", back_populates="users")  # Define relationship with Role model
    first_name = Column(String(255), nullable = True)
    last_name = Column(String(255))
    user_name = Column(String(255), unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255))
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_details = relationship("UserDetails", back_populates="user", uselist=False, cascade="all, delete") # Define relationship with UserDetails
```



### Genrate alembic
```python
alembic revision --autogenerate -m "create user and blog table migrations"  #analyzes tables and creates a migration file
```
```python
alembic upgrade head  #executes the migration files to make actual changes in db
```
