

### Core Workflow & Commands
- Creating Revisions
  - Manual: **alembic revision -m "message"**.
  - Autogenerate: **alembic revision --autogenerate -m "message"**. This compares your SQLAlchemy models to the database and writes the migration script for you.
- Applying Changes:
  - **alembic upgrade head**: Applies all pending migrations to reach the latest version.
  - **alembic upgrade <revision_id>**: Upgrades to a specific version.
- Rolling Back:
  - **alembic downgrade -1**: Reverts the last migration.
  - **alembic downgrade base**: Reverts all migrations back to the beginning.

#### Configure alembic.ini
- Find:- sqlalchemy.url = driver://user:pass@localhost/dbname
- Change to: sqlalchemy.url = sqlite:///./database/app.db

#### Configure alembic/env.py
- find:- target_metadata = None
- Replace with:
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

### Create Model
- models/user.py
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

#### Create first migration
```python
alembic revision --autogenerate -m "create_table"
```
- executes the migration files to make actual changes in db
```python
alembic upgrade head  
```

#### Add the field in model
- Update your model 📁 models/user.py
```python
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    phone_number = Column(String(20))   # ✅ new
    age = Column(Integer)               # ✅ new

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```
```python
alembic revision --autogenerate -m "add phone and age to users"
```
- executes the migration files to make actual changes in db
```python
alembic upgrade head  
```

#### Change field name
- Update your model 📁 models/user.py
```python
ages = Column(Integer)
```
```python
alembic revision --autogenerate -m "rename age to ages"
```
- executes the migration files to make actual changes in db
```python
alembic upgrade head  
```

#### delete the age column
- Update your model 📁 models/user.py
```python
# Remove this line:
ages = Column(Integer)
```
- Generate migration
```python
alembic revision --autogenerate -m "drop ages column"
```
```python
alembic upgrade head
```

### Check current version
```python
alembic current

# Output:- 7c2d3e4f (head)
```

### To go back:
```python
alembic downgrade -1
```
#### How to work alembic downgrade -1
- initial
  - Created users table
- add phone_number
  - Added phone_number column
- add user_name
  - Added user_name column
- **Current DB = head (migration 3)**
- Check current version
  - 7c2d3e4f (head)
- Now run rollback
  - alembic downgrade -1
- Result in DB
```python
# before
id | name | email | phone_number | user_name

# after
id | name | email | phone_number

# user_name column removed
# Data inside it lost ❌
```
```python
# delete this line from model
ages = Column(Integer)

alembic revision --autogenerate -m "remove ages column"

alembic upgrade head
```

### View migration history
```python
alembic history
```


### Alembic for Database Migrations
* This will create a directory named **alembic** in **your project directory** with a configuration file named **alembic.ini**.
* Open the alembic.ini file and configure the sqlalchemy.url parameter to point to your database connection URI.
* Create a Migration Script: 
```python
alembic revision --autogenerate -m "create_table"
```

### Genrate alembic
```python
# Genrate alembic
alembic revision --autogenerate -m "create user and blog table migrations"  #analyzes tables and creates a migration file
```
```python
alembic upgrade head  #executes the migration files to make actual changes in db
```

### Soft delte with alembic?
- Soft delete Alembic se directly nahi hota,
- Alembic sirf schema change karta hai (column add/remove).
- Soft delete ka logic model + query level par hota hai.

#### Soft Delete Concept
1. Model update
```python
from sqlalchemy import Column, Boolean, DateTime
from datetime import datetime

is_deleted = Column(Boolean, default=False)
deleted_at = Column(DateTime, nullable=True)
```
- in cmd
```python
alembic revision --autogenerate -m "add soft delete fields"
alembic upgrade head
```
#### in code
- in view
```python
user.is_deleted = True
user.deleted_at = datetime.utcnow()
db.commit()
```
- Always filter active users
```python
db.query(User).filter(User.is_deleted == False).all()
```
- kabhi hard delete karna ho to
```python
db.query(User).filter(User.is_deleted == True).delete()
db.commit()
```

### Foreign key migration (User → Profile)
- update user mode
```python
profile = relationship("Profile", back_populates="user", uselist=False)
# for cascade
profile = relationship(
    "Profile",
    back_populates="user",
    uselist=False,
    cascade="all, delete"
)
```
- add Profile model
```python
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    # for cascade
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True 
)

    user = relationship("User", back_populates="profile")
```
- Alembic revision generate
```python
alembic revision --autogenerate -m "create profiles table with fk"
alembic upgrade head
```

### SQLite Important Note (VERY IMPORTANT)
- SQLite me foreign keys by default OFF hoti hain
- Replit + SQLite me FK enforce karne ke liye engine me enable karo:
```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

from sqlalchemy import event

@event.listens_for(engine, "connect")
def enable_sqlite_fk(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
```




```
🚀 Next I can teach you

Pick one:

1️⃣ Foreign key migration (User → Profile)
2️⃣ Soft delete with Alembic
3️⃣ Many-to-many table migration
4️⃣ Seed default admin user via migration
5️⃣ Environment-based DB config


🧠 1️⃣3️⃣ Interview questions you can now answer

✔ Difference between create_all vs Alembic
✔ What is revision ID
✔ What is head
✔ What is downgrade
✔ What is batch mode in SQLite
✔ How to do data migration
```