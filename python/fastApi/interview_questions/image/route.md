### Create route file
- routes/__init__.py
```python
from .image_routes import router as image_router
```
- routes/image_routes.py
```python
# Only upload image 
from fastapi import APIRouter, Depends, FastAPI, File, UploadFile
import shutil
import os

router = APIRouter(prefix="/image_routes", tags=["Image Routes"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-image_only/")
async def upload_image_only(file: UploadFile = File(...)):
    # image validation
    if not file.content_type.startswith("image/"):
        return {"error": "Only image files are allowed"}
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Image uploaded successfully",
    }
```
### Include main.py
```python
from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv
import os

from database.connection import engine, Base
import models  # 👈 this loads all models

from database.connection import SessionLocal
from database.seeders.role_seeder import seed_roles

from routes import genral_router, role_router, auth_router, image_router

load_dotenv()

# app = FastAPI()  # This is the default configuration
app = FastAPI(
    title=os.getenv("PROJECT_NAME"), version=os.getenv("PROJECT_VERSION")
)  # This is the custom configuration


@app.on_event("startup")
def run_seeders():
    db = SessionLocal()
    try:
        seed_roles(db)
    finally:
        db.close()


# Base.metadata.create_all(bind=engine)
app.include_router(genral_router)
app.include_router(role_router)
app.include_router(auth_router)
app.include_router(image_router)
```


### datbase plus image
- now i want to upload image and save data into databse
1. creaet model
```python
from sqlalchemy import Column, Integer, String, DateTime
from database.connection import Base
from datetime import datetime


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)  # 👈 added field
    file_name = Column(String)
    file_path = Column(String)
    file_type = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```
```python
alembic revision --autogenerate -m "create media table"
alembic upgrade head
```

### upload multiapl image
- add this line on top
```python
from typing import List  # 👈 import List in top of file
```
```python
@router.post("/upload-multiple/")
async def upload_multiple(files: List[UploadFile] = File(...)):
    filenames = []

    for file in files:
        path = f"uploads/{file.filename}"
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        filenames.append(file.filename)

    return {"files": filenames}
```

### upload image with database
```python
from fastapi import APIRouter, Depends, FastAPI, File, UploadFile, Form
from sqlalchemy.orm import Session
from database.connection import get_db
import shutil
import time
import os, uuid
from models.media import Media
from typing import List

@router.post("/upload_image_with_database/")
async def upload_image_with_database(
    user_name: str = Form(...),  # 👈 get from form
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    filename = f"{int(time.time())}_{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join("uploads", filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    media = Media(
        user_name=user_name,  # 👈 save here
        file_name=filename,
        file_path=file_path,
        file_type=file.content_type,
    )

    db.add(media)
    db.commit()
    db.refresh(media)

    return {"message": "Uploaded", "user": user_name}
```