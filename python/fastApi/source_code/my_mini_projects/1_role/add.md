### Role Create

```python
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db

from database.models.roles import Role

from fastapi.responses import JSONResponse  # Include for message response.

from database.schemas.role import RoleCreate
from sqlalchemy.exc import SQLAlchemyError

'''
Create role
validation exsting role
'''
@router.post("/role/create")
# def create_role_handler(slug: str,name:str, db: Session = Depends(get_db)):
def create_role_handler(role: RoleCreate, db: Session = Depends(get_db)):  # input field from the RoleCreate scheme
    try:
        existing_role = db.query(Role).filter(Role.slug == role.slug).first()
        if existing_role:
            return JSONResponse(
                content={
                    "status": False,
                    "code": 400,
                    "message": "Role with this slug already exists"
                },
                status_code=400
            )
        
        new_record = Role(**role.dict())
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return JSONResponse(
            content={
                "status": True,
                "code": 200,
                "message": "Role has been created successfully!",
                "data": {
                    "id": new_record.id,
                    "slug": new_record.slug,
                    "name": new_record.name,
                    "created_at": new_record.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
                    "updated_at": new_record.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
                }
            },
            status_code=200
        )


    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
```


* previeuse code you can see
```python

```