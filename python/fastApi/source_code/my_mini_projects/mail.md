### Install the library
* url:-  https://sabuhish.github.io/fastapi-mail/
* url:- https://medium.com/nerd-for-tech/how-to-send-email-using-python-fastapi-947921059f0c
```python
pip install fastapi-mail
```

### add code in .env file
```python
MAIL_USERNAME=<GMAIL_USERNAME>
MAIL_PASSWORD=<GMAIL_PASSWORD>
MAIL_FROM=<SENDER_ADDRESS>
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_FROM_NAME=<TITLE_FOR_MAIL>


MAIL_USERNAME ="janicahanover@gmail.com",
MAIL_PASSWORD = "dwglkfflvxoxzywr",
MAIL_FROM = "janicahanover@gmail.com",
MAIL_PORT = 465,
MAIL_SERVER = "smtp.gmail.com",
MAIL_STARTTLS = False,
MAIL_SSL_TLS = True,
USE_CREDENTIALS = True,
VALIDATE_CERTS = True
```

### Standard way of sending email with FastAPI
```python
from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME = "username",
    MAIL_PASSWORD = "**********",
    MAIL_FROM = "test@email.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "mail server",
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

app = FastAPI()



@app.post("/email")
async def simple_send(email: EmailSchema) -> JSONResponse:
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
```

### Email as background task
```python
from fastapi import FastAPI, BackgroundTasks
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

@app.post("/emailbackground")
async def send_in_background(
    background_tasks: BackgroundTasks,
    email: EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=email.dict().get("email"),
        body="Simple background task",
        subtype=MessageType.plain)

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message,message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})
```

### Registraion with email

```python
'''
Create user
role id exist or not
username or email already exist
password hash
email send
'''
@router.post("/registration_user_with_send_email")
async def registration_user_with_send_email(request: UserCreate, db: Session = Depends(get_db)):

    # Check if the provided role_id exists
    role = db.query(Role).filter(Role.id == request.role_id).first()
    if not role:
        return JSONResponse(
            content={
                "status": False,
                "code": 404,
                "message": "Role ID does not exist",
            },
            status_code=404
        )
    
    # Check user or email already exists or not
    existing_user_email = db.query(User).filter(User.email == request.email).first()
    existing_user_username = db.query(User).filter(User.user_name == request.user_name).first()

    if existing_user_username or existing_user_email:
        message = "User name already registered" if existing_user_username else "Email already registered"
        return JSONResponse(
            content={
                "status": False,
                "code": 400,
                "message": message,
            },
            status_code=400
        )
    # Hash the password before storing it
    hash_password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    db_user = User(
            role_id=request.role_id,
            first_name=request.first_name,
            last_name=request.last_name,
            user_name=request.user_name,
            email=request.email,
            # password=request.password
            password=hash_password  # Store the hashed password as string
        )

    # db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Create and save the user details
    db_user_details = UserDetails(
        user_id=db_user.id,
        address=request.address,
        state=request.state,
        city=request.city,
        zip_code=request.zip_code
    )
    db.add(db_user_details)
    db.commit()

    # Send email to the registered user
    html = f"""
    <p>Hi {request.first_name},</p>
    <p>This is a test mail, thanks for using our service!</p>
    <p>Best regards,</p>
    <p>Your Company Name</p>
    """

    message = MessageSchema(
        subject="Welcome to Our Service",
        recipients=[request.email],  # Use a list of email addresses
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)



    return JSONResponse(
        content={
            "status": True,
            "code": 200,
            "message": "User has been created successfully!",
            "data": {
                "id": db_user.id,
                "first_name": db_user.first_name,
                "last_name": db_user.last_name,
                "user_name": db_user.user_name,
                "email": db_user.email,
                "address": db_user_details.address,
                "state": db_user_details.state,
                "city": db_user_details.city,
                "zip_code": db_user_details.zip_code,
                "created_at": db_user.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
                "updated_at": db_user.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
            }
        },
        status_code=200
    )
```