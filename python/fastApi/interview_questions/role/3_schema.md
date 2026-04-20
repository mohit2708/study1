### Create schema file
- databse/schemas/role_schema.py
- databse/schemas/__init__.py
```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Request schema
class RoleCreate(BaseModel):
    name: str


class RoleUpdate(BaseModel):
    name: str


# Data schema
class RoleData(BaseModel):
    id: int
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # SQLAlchemy support


# Common response wrapper
class RoleResponse(BaseModel):
    status: bool
    code: int
    message: str
    data: Optional[RoleData] = None

```