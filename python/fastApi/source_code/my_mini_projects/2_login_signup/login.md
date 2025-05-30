### Login logic
```python
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models.users import User
from database.models.roles import Role
from database.models.user_details import UserDetails

from fastapi.responses import JSONResponse  # Include for message response.
from sqlalchemy.exc import SQLAlchemyError

from database.schemas.user import UserCreate, UserLogin

import bcrypt # for hashed password 

router = APIRouter()


'''
login user
email or password is valid or not
password hash check
'''
@router.post("/login")
def login_user(request: UserLogin, db: Session = Depends(get_db)):

    # Check if the user exists with the provided email
    db_user = db.query(User).filter(User.email == request.email).first()
    if not db_user:
        return JSONResponse(
            content={
                "status": False,
                "code": 404,
                "message": "User not found",
            },
            status_code=404
        )
    
    # Verify the provided password with the stored hashed password
    if not bcrypt.checkpw(request.password.encode('utf-8'), db_user.password.encode('utf-8')):
        return JSONResponse(
            content={
                "status": False,
                "code": 401,
                "message": "Invalid password",
            },
            status_code=401
        )

    # Retrieve the UserDetails associated with this user
    db_user_details = db.query(UserDetails).filter(UserDetails.user_id == db_user.id).first()

    # If login is successful
    return JSONResponse(
        content={
            "status": True,
            "code": 200,
            "message": "Login successful",
            "data": {
                "id": db_user.id,
                "first_name": db_user.first_name,
                "last_name": db_user.last_name,
                "user_name": db_user.user_name,
                "email": db_user.email,
                "user_details": {
                    "address": db_user_details.address if db_user_details else None,
                    "state": db_user_details.state if db_user_details else None,
                    "city": db_user_details.city if db_user_details else None,
                    "zip_code": db_user_details.zip_code if db_user_details else None,
                },
                "created_at": db_user.created_at.strftime("%Y-%m-%dT%H:%M:%S") if db_user_details else None,
                "updated_at": db_user.updated_at.strftime("%Y-%m-%dT%H:%M:%S") if db_user_details else None,
            }
        },
        status_code=200
    )
```