#### Install packages
```python
pip install python-jose # JWT token create & verify
pip install passlib[bcrypt]  # Password hashing & checking
pip install python-multipart    # Form data handle karne ke liye

# ager password related issue aaye to ye use karo 
# version change
pip uninstall bcrypt passlib -y
pip install bcrypt==4.0.1 passlib==1.7.4
```

#### Model
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base   # your Base import

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```
- Run migration:
```python
alembic revision --autogenerate -m "create users table"
alembic upgrade head
```

### Pydantic Schemas
- schemas/user.py
```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    # email: EmailStr   # Only for email
    login: str  # username OR email
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
```

#### Password Hashing Utils
- utils/init.py
- utils/password_security.py
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
```

- utils/jwt.py
```python
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

#### generate SECRET_KEY
- open cmd
```python
# in window
python -c "import secrets; print(secrets.token_hex(32))"

# in OpenSSL (Linux/Mac)
openssl rand -hex 32

# Output
9f3c1c9a5a6e4c0c8b4e7d9c2f1a6b3e5d8c7a9f0b1c2d3e4f5a6b7c8d9e0f1
```

### Signup
- routes/auth_routes.py
- add in init file
```python
from .auth_routes import router as auth_router
```
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from models.user import User
from database.schemas.user import UserCreate, UserLogin, UserResponse
from utils.password_security import hash_password, verify_password
from utils.jwt import create_access_token

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from utils.jwt import SECRET_KEY, ALGORITHM

from sqlalchemy import or_

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
  print("RAW PASSWORD:", user.password)
  print("TYPE:", type(user.password))
  print("LENGTH:", len(user.password.encode("utf-8")))
  print("hash LENGTH:", hash_password(user.password))

  # 🔹 Check if email already exists
  existing_email = db.query(User).filter(User.email == user.email).first()

  if existing_email:
    raise HTTPException(status_code=400, detail="Email already registered")

  # 🔹 Check if username already exists
  existing_username = db.query(User).filter(
      User.user_name == user.user_name).first()

  if existing_username:
    raise HTTPException(status_code=400, detail="User name already registered")

  # 🔹 Hash password
  hashed_password = hash_password(user.password)

  new_user = User(name=user.name, email=user.email, password=hashed_password)

  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user
```

#### Login
```python
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

  # db_user = db.query(User).filter(User.email == user.email).first()
  db_user = db.query(User).filter(
      or_(User.email == user.login, User.user_name == user.login)).first()

  if not db_user or not verify_password(user.password, db_user.password):
    raise HTTPException(status_code=401, detail="Invalid email or password")

  token = create_access_token({"sub": db_user.email})

  return {"access_token": token, "token_type": "bearer"}
```

### To chack authnticate or not
```python
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)):
  token = credentials.credentials
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
  except JWTError:
    raise HTTPException(status_code=401, detail="Invalid token")

  user = db.query(User).filter(User.email == email).first()

  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  return user
```

### Test Route
```python
@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
  return current_user
```

## Schemas
### user.py
- database/schemas/user.py
```python
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    user_name: str
    password: str


class UserLogin(BaseModel):
    # email: EmailStr   # Only for email
    login: str  # username OR email
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
```
