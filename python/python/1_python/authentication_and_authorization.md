### What is the difference between authentication and authorization?
- Authentication verifies the identity of the user (e.g., username/password, token), 
- While authorization determines what actions or resources the authenticated user is allowed to access (e.g., roles, permissions)


### Key Differences:
- Authentication answers the question "Who are you?"
  - Example: Verifying user credentials (username and password).
  - This is typically done using methods like JWT tokens, OAuth2, or Basic Authentication.
- Authorization answers the question "What are you allowed to do?"
    - Example: Checking if a user has a specific role or permission to access an endpoint.
    - This often involves checking user roles, access control lists (ACLs), or permission levels.

### How does FastAPI handle authentication?
- FastAPI provides utilities like **OAuth2PasswordBearer**, **OAuth2PasswordRequestForm**, and **Depends** for extracting and validating tokens for authentication. 
- We can also integrate **JWT tokens** for stateless authentication.

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    expiration = timedelta(hours=1)
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expiration})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)

@app.get("/secure-endpoint")
def read_secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": "Secure data", "user": current_user}

```