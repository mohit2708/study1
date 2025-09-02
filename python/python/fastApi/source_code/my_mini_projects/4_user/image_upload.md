


### install libraray
```python
pip install python-multipart
```
* add image field in model/users.py
```python
# in model file
image = Column(String(255), nullable=True)  # Field for image upload
```
* Import File and UploadFile from fastapi

### image upload in folder intial phase
```python
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models.users import User
from fastapi.responses import JSONResponse
from datetime import datetime

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
import shutil
from pathlib import Path

from database.schemas.user import CustomerStore


router = APIRouter()


@router.post("/uploadfile/")

async def create_upload_file(file: UploadFile):
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    file_size = await file.read()
    if len(file_size) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB.")

    # Reset the file pointer to the beginning
    await file.seek(0)


    # validation for image
    '''
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    '''
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed.")


    # Creaet Directory
    # Define the directory for profile images
    UPLOAD_DIR = Path("uploads/image/profile_image")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # Create the directory and parent directories if they don't exist


    # create time stamp and upload file in folder
    '''
    # upload image with file name
    file_path = UPLOAD_DIR / file.filename
    '''
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Create a unique filename with timestamp
    file_extension = file.filename.split(".")[-1]  # Extract file extension
    unique_filename = f"{timestamp}_{file.filename}"
    file_path = UPLOAD_DIR / unique_filename

    db_user = User(
            first_name=first_name,
            image = str(file_path)
        )

    # Save the file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": unique_filename, "file_path": str(file_path)}
```

### image upload in databse and firstname, lastname
```python
# databse->schemas->user
class CustomerStore(BaseModel):
    first_name: str
    last_name: str
```

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


@router.post("/uploadfile/")
# async def create_upload_file(request: CustomerStore, role_id: int, file: UploadFile):
# async def create_upload_file(request: CustomerStore, file: UploadFile):
# async def create_upload_file(request: CustomerStore, file: UploadFile = File(...)):
# async def create_upload_file(file: UploadFile):
async def create_upload_file(first_name: str = Form(...), last_name: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    file_size = await file.read()
    if len(file_size) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB.")

    # Reset the file pointer to the beginning
    await file.seek(0)


    # validation for image
    '''
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    '''
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed.")


    # Creaet Directory
    # Define the directory for profile images
    UPLOAD_DIR = Path("uploads/image/profile_image")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # Create the directory and parent directories if they don't exist


    # create time stamp and upload file in folder
    '''
    # upload image with file name
    file_path = UPLOAD_DIR / file.filename
    '''
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Create a unique filename with timestamp
    file_extension = file.filename.split(".")[-1]  # Extract file extension
    unique_filename = f"{timestamp}_{file.filename}"
    file_path = UPLOAD_DIR / unique_filename

    db_user = User(
            first_name=first_name,
            last_name=last_name,
            image = str(file_path)
        )

    # db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Save the file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": unique_filename, "file_path": str(file_path)}
```
### first name and other data through request
```python
# change in scheme
from fastapi import Form
class CustomerStore(BaseModel):
    first_name: str
    last_name: str

    @classmethod
    def as_form(
        cls,
        first_name: str = Form(...),
        last_name: str = Form(...)
    ) -> "CustomerStore":
        return cls(first_name=first_name, last_name=last_name)

# change function line
from fastapi import FastAPI, File, UploadFile, Form

async def create_upload_file(request: CustomerStore = Depends(CustomerStore.as_form), file: UploadFile = File(...), db: Session = Depends(get_db)):
```


### Get full data with full image url
```python
@router.get("/user-list-with-all-data-with-image-url/")
def get_user_list_with_image_url(db: Session = Depends(get_db)):
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
    
    # Construct the absolute path for the user's profile image
    '''
    1st way to get full directory
    '''
    # profile_image_path = Path("uploads/image/profile_image", user.image).resolve()
    # print("full path", profile_image_path)
    '''
    2nd way current directory
    '''
    current_working_directory = Path.cwd()
    profile_image_path = str(current_working_directory) + "/" + user.image

    user_dict["profile_image_url"] = str(profile_image_path) if profile_image_path else None        

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

### Delete the row with image from the folder
```python
@router.delete("/delte-user-with-image/{user_id}/delete")
def delete_user_with_image(user_id: int, db: Session = Depends(get_db)):
    # Retrieve the user
    get_user = db.query(User).filter(User.id == user_id).first()
    if not get_user:
        raise HTTPException(status_code=404, detail="User not found")

    current_working_directory = Path.cwd()
    profile_image_path = str(current_working_directory) + "/" + get_user.image

    # Delete the image file if it exists
    if(profile_image_path):
        try:
            os.remove(profile_image_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to delete image: {str(e)}")
   
    # Delete the user from the database
    db.delete(get_user)
    db.commit()

    return {"message": "User and image deleted successfully"}
```




