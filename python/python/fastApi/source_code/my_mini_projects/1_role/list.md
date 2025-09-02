|  No.  | Crud Role Steps                                                     |
| :---: | ------------------------------------------------------------------- |
|       | [Get Role list from the database](#get-role-list-from-the-database) |
|       | [Get role data by ID](#get-role-data-by-id)                         |

### Get Role list from the database
```python
from fastapi import FastAPI, APIRouter, Depends # include Depends
from sqlalchemy.orm import Session # Include this line
from database.connection import get_db  # Include this line

from database.models.roles import Role # include Role model

from fastapi.responses import JSONResponse  # Include for message response.

router = APIRouter()

@router.get("/role-list/")
def get_roles_list(db: Session = Depends(get_db)):
    roles = db.query(Role.id, Role.slug, Role.name).all()
    
    '''
    Check Role list is empty or not
    '''
    if not roles:  # Check if the roles list is empty
        return JSONResponse(
            content={
                "success": True,
                "code": 200,
                "message": "Role list is empty",
            },
            status_code=200
        )
    '''
    Get Role Data
    '''
    roles_list = []
    for role in roles:
        role_dict = {
            "id": role.id,
            "slug": role.slug,
            "name": role.name
        }
        roles_list.append(role_dict)
    return JSONResponse(
        content={
            "success": True,
            "code": 200,
            "message": "Roles list retrieved successfully",
            "data": roles_list
        },
        status_code=200  # You can change this to any valid HTTP status code
    )
    # return {
    #     "success": True,
    #     "code": 200,
    #     "message": "Roles list retrieved successfully",
    #     "data": roles_list
    # }

```

### Get role data by ID

```python
'''
Get role List by id
'''
@router.get("/role/{role_id}")
def get_role_list_by_id(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    # if not role:
    if role is None:
        # raise HTTPException(status_code=404, detail="Role not found")
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": f"Role id {role_id} does not exists!!"
            },
            status_code=400
        )
    return JSONResponse(
        content={
            "status": True,
            "code": 200,
            "message": "Role retrieved successfully!",
            "data": {
                "id": role.id,
                "slug": role.slug,
                "name": role.name
            }
        },
        status_code=200
    )
```

### Extra
* you can see also code
```python
@router.get("/role-list/", response_model=List[RoleList])
def get_roles_list(db: Session = Depends(get_db)):
    roles = get_roles(db)  # Function call
    # return roles
    role_data = {
        "success": True,
        "code": 200,
        "message":"hello",
        "roles": roles
    }
    response_data= RoleList(**role_data)
    return ORJSONResponse(content=response_data.dict(), status_code=200)

def get_roles(db: Session) -> List[dict]:
    roles = db.query(Role.id, Role.slug, Role.name).all()
    roles_list = []
    for role in roles:
        role_dict = {
            "id": role.id,
            "slug": role.slug,
            "name": role.name
        }
        roles_list.append(role_dict)
    return roles_list
```