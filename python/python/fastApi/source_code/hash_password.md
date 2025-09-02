### Hash Password
#### Using bcrypt
```python
import bcrypt # for hashed password

@router.post("/users/add")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": "Email already registered",
            },
            status_code=400
        )

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    hash_password = hashed_password.decode('utf-8')

    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        user_name=user.user_name,
        email=user.email,
        password=hash_password  # Store the hashed password as string
    )

    # db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

#### Using passlib
```python
from passlib.context import CryptContext

@router.post("/users/add")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": "Email already registered",
            },
            status_code=400
        )
    # Hash the password before storing it
    pwd_hashed = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_hashed.hash(user.password)
    

    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        user_name=user.user_name,
        email=user.email,
        password=hashed_password  # Store the hashed password as string
    )

    # db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```
