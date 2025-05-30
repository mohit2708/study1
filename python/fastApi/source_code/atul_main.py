from fastapi import FastAPI,Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, ORJSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, validator, ValidationError, model_validator, EmailStr
from enum import Enum
from passlib.context import CryptContext
from typing import Optional

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost/profile_fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    country = Column(Integer)
    state = Column(Integer)
    city = Column(Integer)
    role = Column(Integer)
    zeep_code = Column(String(255))
    address = Column(String(255))

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String(255))

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String(255))
    country_id = Column(Integer)

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String(255))
    state_id = Column(Integer)
    country_id = Column(Integer)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(255))


class BaseUserSchema(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    username:Optional[str] = None
    role: int
    country: int
    state: int
    city: int
    address: Optional[str] = None
    zeep_code:Optional[str] = None


class UserSchemaIn(BaseUserSchema):
    password: str
    confirm_password:str

    @model_validator(mode='after')
    def check_passwords_match(self):
        pw1 = self.password
        pw2 = self.confirm_password
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self

class UserSchemaOut(BaseUserSchema):
    status_code:int
    status:bool


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashData():
    @staticmethod
    def create_password_hash(password):
        return pwd_context.hash(password)


def create_new_user(db, user):
    db_user = User(first_name=user.first_name,last_name=user.last_name,username=user.username,email=user.email,hashed_password=HashData.create_password_hash(user.password),country=user.country,state=user.state,city=user.city,role=user.role,zeep_code=user.zeep_code,address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/save-user",response_model=UserSchemaOut,response_class=JSONResponse,name="saveuser")
def save_user(user: UserSchemaIn, db:Session = Depends(get_db)):
    try:
        inserted_user = create_new_user(db=db, user=user)
        http_status_code = 200
        user_data = {
            "status_code": http_status_code,
            "status":True,
            "first_name": inserted_user.first_name,
            "email": inserted_user.email,
            "role": inserted_user.role,
            "country":inserted_user.country,
            "state":inserted_user.state,
            "city":inserted_user.city
        }
        response_data = UserSchemaOut(**user_data)
        response = JSONResponse(content=response_data.dict(),status_code=http_status_code)
    except ValueError as e:
        http_status_code = 500
        error_detail = f"Invalid response data: {e}"
        response_data = {
            "status_code": http_status_code,
            "status": False,
            "detail": error_detail
        }
        response = JSONResponse(content=response_data, status_code=http_status_code)
    return response