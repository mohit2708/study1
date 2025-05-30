### User list with particular data
```python
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models.users import User
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/user-list/")
def get_user_list(db: Session = Depends(get_db)):
    # return {"msg":"get user list🚀"}
    users = db.query(User.id,User.first_name,User.last_name).all()
    
    '''
    Check user list is empty or not
    '''
    if not users:  # Check if the users list is empty
        return JSONResponse(
            content={
                "success": True,
                "code": 200,
                "message": "User list is empty",
            },
            status_code=200
        )
    '''
    Get User Data
    '''
    users_list = []
    for user in users:
        user_dict = {
            "id": user.id,
            "slug": user.first_name,
            "name": user.last_name
        }
        users_list.append(user_dict)
    return JSONResponse(
        content={
            "success": True,
            "code": 200,
            "message": "Users list retrieved successfully",
            "data": users_list
        },
        status_code=200  # You can change this to any valid HTTP status code
    )
```

### User list with full data
```python
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models.users import User
from fastapi.responses import JSONResponse
from datetime import datetime

router = APIRouter()

@router.get("/user-list-with-all-data/")
def get_user_list(db: Session = Depends(get_db)):
    # Query all user records
    users = db.query(User).all()
        
    '''
    Check user list is empty or not
    '''
    if not users:  # Check if the users list is empty
        return JSONResponse(
            content={
                "success": True,
                "code": 200,
                "message": "User list is empty",
            },
            status_code=200
        )

    '''
    Get User Data
    '''
    users_list = []
    for user in users:
        user_dict = user.__dict__.copy()  # Copy the dictionary to avoid modifying the original object
        user_dict.pop("_sa_instance_state", None)  # Remove SQLAlchemy's internal field
        user_dict.pop("password", None)  # Remove the password field

    # Convert datetime fields to strings
    for key, value in user_dict.items():
        if isinstance(value, datetime):
            user_dict[key] = value.isoformat()  # Convert to ISO 8601 string

    users_list.append(user_dict)

    return JSONResponse(
        content={
            "success": True,
            "code": 200,
            "message": "Users list retrieved successfully",
            "data": users_list
        },
        status_code=200  # You can change this to any valid HTTP status code
    )
```