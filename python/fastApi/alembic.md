|  No.  | Alembic Questions                            |
| :---: | -------------------------------------------- |
|       | [What is Alembic?](#what-is-alembic)         |
|       | [Why is Alembic used?](#why-is-alembic-used) |


### 🎯**What is Alembic?**
- Alembic is a **database migration tool** for SQLAlchemy.
- It helps you manage changes in your database schema (tables, columns, indexes, constraints) without manually writing SQL every time.
- It helps you:
  - ✔ Add new columns
  - ✔ Modify tables
  - ✔ Track schema versions
  - ✔ Avoid deleting DB ❌
- It helps manage and version-control database schema changes such as creating tables, adding columns, modifying columns, or deleting tables without manually writing SQL scripts.

### Why is Alembic used?
#### 1. **Version Control for Database:-** Just like Git tracks code changes, Alembic tracks database changes.
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
#### 3. **Database Upgrade & Rollback**
```python
alembic upgrade head

# Rollback one version:
alembic downgrade -1

# Rollback to a specific version:
alembic downgrade abc123
```
#### 4. **Automatic Migration Generation**
* Alembic compares SQLAlchemy models with the database and generates migration scripts.
```python
alembic revision --autogenerate -m "create roles table"
```


### **Install alembic**
* install package
```python
pip install alembic
```

### **Initialize Alembic:**
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


#### Why do we use Alembic?
* Without Alembic:
  * You have to manually run SQL queries to change the database schema.
  * Keeping schema changes synchronized across environments becomes difficult.
* With Alembic:
  * Tracks schema changes as migration files.
  * Supports version control for the database.
  * Makes deployments easier and safer.

### 🎯**Setup/install Alembic**
* Steps
```python
# Install Alembic
pip install alembic

# Initialize Alembic
alembic init alembic

# IN your folder
project/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│
├── alembic.ini
```
<div style="page-break-before: always;"></div>

#### Configure Alembic
* Open **alembic.ini** file
  * Find:- sqlalchemy.url = driver://user:pass@localhost/dbname
  * Change to: sqlalchemy.url = mysql+pymysql://root:password@localhost:3306/fastapi_db

* open **alembic/env.py** file
  * find:- target_metadata = None
  * Replace with:
```python
from database.connection import Base
import models

target_metadata = Base.metadata
```

- change one line
```python
# before
with connectable.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


# after
with connectable.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True   # ✅ add this line
    )

    with context.begin_transaction():
        context.run_migrations()
```
<div style="page-break-before: always;"></div>

#### What is alembic.ini?
* alembic.ini is the main configuration file of Alembic. It stores database connection settings and migration-related configurations that Alembic uses when generating and applying migrations.

#### What is env.py in Alembic?
* env.py is the core Alembic configuration script **that controls how migrations are generated and executed**. It connects Alembic with your SQLAlchemy models and database.
* When you run:
  * alembic revision --autogenerate -m "message"
  * OR - alembic upgrade head
  * Alembic first executes env.py.

#### Main Responsibilities of env.py
1. Load Database Configuration
2. Connect Alembic to Models
3. Create Database Connection
4. Run Migrations

#### What is the versions folder in Alembic?
* The versions folder stores all Alembic migration files. Each migration file represents a specific database schema change and allows Alembic to track database versions over time.
* **HINDI:-** versions folder me Alembic ki sari migration files store hoti hain. Har file database schema me kiye gaye ek change ko represent karti hai, jaise table create karna, column add karna ya column remove karna.
```python
alembic/
│
├── env.py
├── versions/
│   ├── 1a2b3c4d_initial_migration.py
│   ├── 5e6f7g8h_add_email_column.py
│   └── 9i0j1k2l_create_roles_table.py
```

#### Why is the versions Folder Important?
* Maintains migration history.
* Enables schema version control.
* Supports rollback (downgrade).
* Keeps development, staging, and production databases in sync.

#### Example
* Suppose your User model is:
```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
```
* Later you add:-
```python
email = Column(String)
```

#### Common Alembic Commands
* Initialize Alembic
```python
alembic init alembic
```

* Create Migration
```python
alembic revision --autogenerate -m "add email column"
```

* Apply Migration
```python
alembic upgrade head
```

* Roll Back One Version
```python
alembic downgrade -1
```

* Check Current Version
```
alembic current
```