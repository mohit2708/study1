### **What is Rate Limiting?**
* Rate limiting is a mechanism that restricts the number of requests a user can make to an API within a given time period. It helps prevent abuse, protects server resources, and ensures fair usage of the application.
* Rate Limiting is a technique used to control how many requests a user or client can make to an API within a specific period of time.
* If a user sends more than 100 requests in 1 minute, the extra requests will be blocked.
* **HINDI:-** Rate Limiting ka use API ko abuse hone se bachane ke liye kiya jata hai. Ye restrict karta hai ki ek user ya IP address ek certain time period me kitni requests kar sakta hai.

#### FastAPI me Rate Limiting kaise implement karte hain?
* install library
```python
pip install slowapi
```
* Apply limiter for ip addrress
```python
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

app = FastAPI()

# Limiter object create kiya
limiter = Limiter(key_func=get_remote_address)

@app.get("/users")
@limiter.limit("5/minute")
async def get_users(request: Request):
    return {"message": "Success"}
```
* Apply limiter for user based
```python
def get_user_id(request: Request):
    return str(request.state.user.id)

limiter = Limiter(key_func=get_user_id)
```