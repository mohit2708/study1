### Create schema file
- databse/models/__init__.py
```python
from .user import User
from .role import Role
from .customer import Customer
```

- databse/models/role.py
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