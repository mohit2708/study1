### Install the packages.
* Install package **pyjwt**
```python
pip install pyjwt
(OR) install pyjwt[crypto]
```
* Install passlib
```python
pip install "passlib[bcrypt]"
(OR)
install passlib
```

### full code
* Create a random secret key that will be used to sign the JWT tokens
```python
# open git bash and run this command
openssl rand -hex 32
```
* add code in env
```python
# jwt info
SECRET_KEY=22aee8e00d5a1ee78abe3c28bba80a824a59c2ea1ffbdf433d979b8f4d1fbc4b
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TOKEN_TYPE=bearer
API_KEY_HEADER_NAME=ACCESS-TOKEN
```
* Create the config.py file and core folder
```python
from dotenv import load_dotenv
from typing import Dict
import os
load_dotenv()

class JWTConfig:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM =  os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    TOKEN_TYPE: str = "bearer"
    AUTH_HEADER: Dict[str,str] = {"WWW-Authenticate": "Bearer"}
    API_KEY_HEADER_NAME="ACCESS-TOKEN"

jwt_config = JWTConfig()
```
* and code in user model folder
```python
"""
check plain_password or hashed_password are same
"""
# Verify password(Match password) 
@staticmethod
def verify_password(plain_password, hashed_password):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.verify(plain_password, hashed_password)

# get email
def get_user_by_email(db: Session, requestemail):
    return db.query(User).filter(User.email == requestemail).first()
```


```python
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, APIKeyHeader
from fastapi.responses import JSONResponse
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from database.connection import get_db
from sqlalchemy.orm import Session
from database.models.users import User
from core.config import jwt_config


router = APIRouter()

@router.post("/login")
async def login(email:str, password:str, db:Session = Depends(get_db)):
    get_user_data = User.get_user_by_email(db, email)
    if not get_user_data:
        return JSONResponse(
            content={
                "status": False,
                "code": 404,
                "message": "Email ID does not exist",
            },
            status_code=404
        )
    if not User.verify_password(password, get_user_data.password):
        # raise HTTPException(status_code=401, detail="Incorrect password")
        return JSONResponse(
            content={
                "status": False,
                "code": 404,
                "message": "Password is incorrect",
            },
            status_code=404
        )

    # Here you can generate and return a JWT token for authentication if needed
    access_token_expires = timedelta(minutes=int(jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES))

    access_token = create_access_token(
        data={"email": get_user_data.email}, expires_delta=access_token_expires
    )

    return JSONResponse(
        content={
            "status": True,
            "code": 200,
            "message": "User login successfully!",
            "token":{
                "access_token": access_token,
                "token_type": "bearer",
            },
            "user_data": {
                "id": get_user_data.id,
                "first_name": get_user_data.first_name,
                "last_name": get_user_data.last_name,
                "created_at": get_user_data.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": get_user_data.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        },
        status_code=200
    )
    # print(get_user_data)



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_config.SECRET_KEY, algorithm=jwt_config.ALGORITHM)
    return encoded_jwt



header_scheme = APIKeyHeader(name="jwt_config.API_KEY_HEADER_NAME")

def verify_token(token: str = Depends(header_scheme)):
    try:
        payload = jwt.decode(token, jwt_config.SECRET_KEY, algorithms=[jwt_config.ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/users/")
async def get_users(email: str = Depends(verify_token), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_token(token: str = Depends(header_scheme)):
#     try:
#         payload = jwt.decode(token, jwt_config.SECRET_KEY, algorithms=[jwt_config.ALGORITHM])
#         email: str = payload.get("email")
#         if email is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return email
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")


# @router.get("/users/")
# async def get_users(email: str = Depends(verify_token), db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     return users

```