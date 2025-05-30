### Update Role data by ID
```python
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db

from database.models.roles import Role

from fastapi.responses import JSONResponse  # Include for message response.

from database.schemas.role import RoleCreate, RoleUpdate
from sqlalchemy.exc import SQLAlchemyError

'''
Update Role data by id
'''
@router.put("/role/{role_id}/update", response_model=RoleUpdate)
def update_role_handler(role_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):

    '''
    Check Role id exist or not
    '''
    get_role_id = db.query(Role).filter(Role.id == role_id).first()
    if not get_role_id:
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": "Role Id does not exists"
            },
            status_code=400
        )
    '''
    role exist or not
    '''
    existing_role = db.query(Role).filter(Role.slug == role_data.slug).first()
    if existing_role:
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": "Role with this slug already exists"
            },
            status_code=400
        )
    '''
    Role Data Update
    '''
    get_role_id.slug = role_data.slug
    get_role_id.name = role_data.name

    # Commit the changes
    db.commit()
    db.refresh(get_role_id)
    return JSONResponse(
        content={
            "status": True,
            "code": 200,
            "message": "Role has been update successfully!",
        },
        status_code=200
    )
```

### Extra
```python
'''
Update role
validation exsting role
role id does not exist
'''
@router.put("/role/{role_id}/update", response_model=RoleUpdate)
def update_role_handler(role_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):
    existing_role = db.query(Role).filter(Role.slug == role_data.slug).first()
    if existing_role:
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": "Role with the same slug already exists!",
            },
            status_code=400
        )
    updated_role = update_role(db, role_id, role_data)
    if isinstance(updated_role, Role):
        return JSONResponse(
                    content={
                        "status": True,
                        "code": 200,
                        "message": "Role has been update successfully!",
                        "data": {
                            "id": updated_role.id,
                            "slug": updated_role.slug,
                            "name": updated_role.name,
                            "created_at": updated_role.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
                            "updated_at": updated_role.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
                        }
                    },
                    status_code=200
                )
    if updated_role is None:
        return JSONResponse(
                content={
                    "status": False,
                    "code": 404,
                    "message": "Role id does not exist!",
                },
                status_code=404
            )
    return updated_role

def update_role(db: Session, role_id: int, role_data: RoleUpdate):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        for key, value in role_data.dict().items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
        return db_role
    return None

```

```python
# ================================================================================ router


# @router.put("/role/{role_id}/update", response_model=RoleUpdate)
# def update_role_handler(role_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):
#     # updated_role = update_role(db, role_id, role_data)
#     db_role = db.query(Role).filter(Role.id == role_id).first()
#     if db_role:
#         for key, value in role_data.dict().items():
#             setattr(db_role, key, value)
#         db.commit()
#         db.refresh(db_role)

#         # return db_role
#         db_role_dict = {
#             "id": db_role.id,
#             "slug": db_role.slug,
#             "name": db_role.name,
#             # Add other attributes as needed
#         }
        
#         response_data = {
#             "success": True,
#             "message": "Role updated successfully",
#             "data": db_role_dict,
#             # "data": db_role.dict(),  # Convert db_role to dictionary # not working this line
#             "status": 200
#         }
#         return JSONResponse(content=response_data, status_code=200)

#     if db_role is None:
#         raise HTTPException(status_code=404, detail="Role not found")
#     return db_role




# @router.put("/role/{role_id}/update", response_model=RoleUpdate)
# def update_role_handler(role_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):
#     db_role = db.query(Role).filter(Role.id == role_id).first()
#     if db_role:
#         if role_data.slug:  # If slug is provided in the request
#             db_role.slug = role_data.slug
#         for key, value in role_data.dict().items():
#             # Skip updating slug as it's already updated if provided
#             if key != 'slug':
#                 setattr(db_role, key, value)
#         db.commit()
#         db.refresh(db_role)
        
#         # Construct dictionary from Role object
#         db_role_dict = {
#             "id": db_role.id,
#             "name": db_role.name,
#             "slug": db_role.slug if hasattr(db_role, 'slug') else None,
#             # Add other attributes as needed
#         }
        
#         response_data = {
#             "success": True,
#             "message": "Role updated successfully",
#             "data": db_role_dict,
#             "status": 200
#         }
#         return JSONResponse(content=response_data, status_code=200)

#     raise HTTPException(status_code=404, detail="Role not found")



#### =================================================================================================
##   json return

# 1st 

# return JSONResponse(
#     content={
#         "status": True,
#         "code": 200,
#         "message": "Role has been Delete successfully!",
#     },
#     status_code=200
# )

# 2nd
# return {
#             "status": True,
#             "code": 200,
#             "message": "Role has been created successfully!",
#             "data": {
#                 "id": db_role.id,
#                 "slug": db_role.slug,
#                 "name": db_role.name,
#                 "created_at": db_role.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
#                 "updated_at": db_role.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
#             }
#         }

# 2nd

# raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Role with this slug already exists",
#             headers={"X-Error": "There goes my error"},
#         )

```