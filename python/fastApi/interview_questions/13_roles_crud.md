### Roles Crud
- routes/role_routes.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_db
from app.models.role import Role

router = APIRouter(prefix="/roles", tags=["Roles"])

# 1. Create Role (Insert)
@router.post("/")
def create_role(name: str, slug: str, db: Session = Depends(get_db)):
    existing = db.query(Role).filter(Role.slug == slug).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")

    role = Role(name=name, slug=slug)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

# 2. Get Role by ID
@router.get("/{role_id}")
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

# 3. Update Role
@router.put("/{role_id}")
def update_role(role_id: int, name: str, slug: str, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    role.name = name
    role.slug = slug

    db.commit()
    db.refresh(role)
    return role

# 4. Delete Role
@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    db.delete(role)
    db.commit()

    return {"message": "Role deleted successfully"}

# Soft Delete Reminder
db.delete(role) ki jagah: -> role.deleted_at = datetime.utcnow()
```

### Manual response (simple)
```python
from fastapi.responses import JSONResponse

@router.get("/{role_id}")
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        return JSONResponse(
            status_code=404,
            content={
                "status": False,
                "code": 404,
                "message": "Role id does not exist!",
            },
        )

    return {
        "status": True,
        "code": 200,
        "message": "Role fetched successfully",
        "data": role,
    }
```

### Reusable response helper (Best practice)
- create folder -> utils/response.py
```python
from fastapi.responses import JSONResponse

def success_response(message: str, data=None, code: int = 200):
    return {
        "status": True,
        "code": code,
        "message": message,
        "data": data,
    }

def error_response(message: str, code: int = 400):
    return JSONResponse(
        status_code=code,
        content={
            "status": False,
            "code": code,
            "message": message,
        },
    )
```
- Use in routes
```python
from utils.response import success_response, error_response
```

```python
if not role:
    return error_response("Role id does not exist!", 404)

return success_response("Role fetched successfully", role)
```


### Kabhi kabhi TypeError: Object of type Role is not JSON serializable aati hai 
- Solution 1 – Manual dict (quick fix)
  - ✔ Works
  - ❌ Repetitive
  - ❌ Scalable nahi
- Solution 2 – Pydantic schema (BEST PRACTICE)

####  Solution 1 – Manual dict (quick fix)
```python
return {
    "status": True,
    "data": {
        "id": role.id,
        "name": role.name,
        "slug": role.slug,
        "created_at": role.created_at,
        "updated_at": role.updated_at,
    }
}
```
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.deps import get_db
from app.models.role import Role

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()

    # ❌ Role not found
    if not role:
        return JSONResponse(
            status_code=404,
            content={
                "status": False,
                "code": 404,
                "message": "Role id does not exist!",
            },
        )

    # ✅ Delete role
    db.delete(role)
    db.commit()

    return {
        "status": True,
        "code": 200,
        "message": "Role deleted successfully",
        "data": {
            "id": role.id,
            "name": role.name,
            "slug": role.slug,
        },
    }
```

#### Solution 2 – Pydantic schema (BEST PRACTICE)
- schemas/role_schema.py
```python
from pydantic import BaseModel
from datetime import datetime

class RoleResponse(BaseModel):
    id: int
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True   # SQLAlchemy support Pydantic v2 me:
        # orm_mode = True # Pydantic v1 me:
```
```python
from schemas.role_schema import RoleResponse

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        return error_response("Role id does not exist!", 404)

    return role
```


### Update scheme
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

- in role_route.py
```python
from database.schemas.role_schema import RoleResponse, RoleData

@router.delete("/scheme/{role_id}", response_model=RoleResponse)
def delete_role_using_scheme(role_id: int, db: Session = Depends(get_db)):
  role = db.query(Role).filter(Role.id == role_id).first()

  if not role:
    return JSONResponse(
        status_code=404,
        content={
            "status": False,
            "code": 404,
            "message": "Role id does not exist!",
        },
    )

  # Extract data before delete
  role_data = RoleData.from_orm(role)

  db.delete(role)
  db.commit()

  return {
      "status": True,
      "code": 200,
      "message": "Role deleted successfully",
      "data": role_data,
  }
```