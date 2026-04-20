### Create schema file
- routes/__init__.py
```python
from .genral_routes import router as genral_router
from .role_routes import router as role_router
from .auth_routes import router as auth_router
```
- routes/role_routes.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from models.role import Role
from fastapi.responses import JSONResponse

from database.schemas.role_schema import RoleResponse, RoleData

router = APIRouter(prefix="/roles", tags=["Roles Routes"])


@router.get("/list")
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()


@router.get("/{role_id}")
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.get("/get_role_by_schema/{role_id}", response_model=RoleResponse)
def get_role_by_schema(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        return RoleResponse(
            status=False, code=404, message="Role id does not exist!", data=None
        )
    return RoleResponse(
        status=True, code=200, message="Role fetched successfully", data=role
    )


@router.post("/add")
def create_role(name: str, slug: str, db: Session = Depends(get_db)):
    existing = db.query(Role).filter(Role.slug == slug).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")

    role = Role(name=name, slug=slug)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


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