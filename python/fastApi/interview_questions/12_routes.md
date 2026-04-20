### Create rotes structure
* Create the routes folder
* create the base.py file under the routes folder
* create the other rotes file like auth.py, role.py, user.py etc under the routes folder
```python
# base.py file
from fastapi import APIRouter

from routes import role
from routes import user

api_router = APIRouter()

api_router.include_router(role.router,prefix="",tags=["Role Routes"])
api_router.include_router(user.router,prefix="",tags=["User Routes"])
```

### create roles.py file under the routes folder.
```python
from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/role-list/")
def get_roles_list():
    return {"msg":"get role list🚀"}
```

### create users.py file under the routes folder.
```python
from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/user-list/")
def get_user_list():
    return {"msg":"get user list🚀"}
```

### Change in main.py file
```python
# include file
from routes.base import api_router

# add code for routes
def include_router(app):
	app.include_router(api_router)

def start_application():
    app = FastAPI(title=project_config.PROJECT_NAME,version=project_config.PROJECT_VERSION)
    create_tables()
    include_router(app)         # add this line
    return app

app = start_application()

```



### Folder structure
```python
app/
 ├── main.py
 ├── api/
 │    ├── __init__.py
 │    ├── deps.py              👈 get_db dependency
 │    ├── routes/
 │    │     ├── __init__.py
 │    │     ├── user_routes.py
 │    │     └── role_routes.py
```

- user_routes.py
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

- role_routes.py
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from app.models.role import Role

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()
```

- __init__.py
```python
from .user_routes import router as user_router
from .role_routes import router as role_router
```

- Change in main.py file
```python
from api.routes import user_router, role_router

app = FastAPI(
    title=os.getenv("PROJECT_NAME"),
    version=os.getenv("PROJECT_VERSION")
)

app.include_router(user_router)
app.include_router(role_router)
```

