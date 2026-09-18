### 🎯**What is response_model?**
* response_model in FastAPI is used to define, validate, serialize, and filter the structure of the data returned by an API endpoint.
* response_model is used to define and validate the structure of the API response.
* "API se jo response jayega, uska structure is Pydantic model ke according hona chahiye."
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.get("/user", response_model=UserResponse)  # Here UserResponse defines what the client is allowed to receive.
def get_user():
    return {
        "id": 1,
        "name": "Mohit",
        "email": "mohit@example.com",
        "password": "123456"
    }

# Response
{
    "id": 1,
    "name": "Mohit",
    "email": "mohit@example.com"
}
```

#### Why use response_model?
#### Main benefits
| Benefit                 | Meaning                                                                  |
| ----------------------- | ------------------------------------------------------------------------ |
| **Response validation** | Response model ke according validate hota hai                            |
| **Data filtering**      | Extra/unwanted fields response se remove ho sakte hain                   |
| **Serialization**       | Python objects ko proper JSON-compatible response mein convert karta hai |
| **Documentation**       | Swagger/OpenAPI mein response structure show hota hai                    |


### 🎯**What is JSONResponse?**
* JSONResponse is a FastAPI/Starlette response class used when you want to manually control the JSON response, including the status code, headers, and response content.
* **HINDI:-** JSONResponse ka use tab karte hain jab humein API ka JSON response manually control karna ho.
* Yahan JSONResponse useful hai because hum explicitly 404 status code ke saath JSON response return karna chahte hain.
* Use cases:
  * Custom status code
  * Custom headers
  * Manually JSON response create karna
  * Error/special response handling

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/users")
def get_users():
    return JSONResponse(
        content={
            "status": True,
            "message": "Users fetched successfully"
        },
        status_code=200
    )
```

### 🎯**What is ORJSONResponse?**
* ORJSONResponse is a FastAPI response class that uses the orjson library to serialize Python data into JSON.
* It is mainly used when you want faster JSON serialization than the standard JSON encoder.
* Jab aapko high-performance JSON serialization chahiye.
* Use case:
  * **Bahut large JSON responses**
  * High-throughput APIs
  * Performance-sensitive applications
```python
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI()

@app.get("/users")
def get_users():
    return ORJSONResponse(
        content={
            "status": True,
            "message": "Users fetched successfully"
        },
        status_code=200
    )
```

### **Difference between JSONResponse and ORJSONResponse?**
* **NOTE:-** JSONResponse & ORJSONResponse same hi hai, ORJSONResponse tab use karte hai jab large data aata ho api se mtb bada data ho.
| Feature       | `JSONResponse`                     | `ORJSONResponse`                    |
| ------------- | ---------------------------------- | ----------------------------------- |
| Library       | Python's `json`                    | `orjson`                            |
| Performance   | Normal                             | Generally faster                    |
| Serialization | Standard JSON serialization        | High-performance JSON serialization |
| Dependencies  | Built into Starlette/FastAPI stack | Requires `orjson`                   |
| Use case      | General APIs                       | Performance-sensitive APIs          |

### How do you customize API responses?
* In FastAPI, we can customize API responses using Pydantic response_model, response classes such as JSONResponse or ORJSONResponse, custom status codes, headers, and a standard response structure containing fields like status, message, and data.
* FastAPI mein API response customize karne ke multiple ways hain. Interview mein mainly ye points batane chahiye:
1. Custom response structure
2. Custom status code:- JSONResponse use karke:
3. Custom headers
4. JSONResponse
5. ORJSONResponse
6. HTMLResponse
7. PlainTextResponse
8. FileResponse
9. StreamingResponse

### How do you return custom status codes?
* FastAPI mein custom HTTP **status code return karne ke 2 common ways hain**.

1. status_code parameter — recommended for fixed success responses
* Agar endpoint ka status code fixed hai:
```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created successfully"
    }
```

2. JSONResponse — jab runtime par status code decide karna ho
* Agar condition ke according status code change karna hai:
```python
from fastapi.responses import JSONResponse

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id == 1:
        return JSONResponse(
            status_code=200,
            content={"message": "User found"}
        )

    return JSONResponse(
        status_code=404,
        content={"message": "User not found"}
    )
```

* Important: Errors ke liye HTTPException
  * Agar API mein error raise karna hai, generally HTTPException use karte hain:
```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"id": 1, "name": "Mohit"}
```

### What is StreamingResponse in FastAPI?
* StreamingResponse data ko ek saath nahi, balki chunks mein client ko send karta hai.
* StreamingResponse is used when you want to send response data to the client gradually (in chunks) instead of waiting for the entire response to be generated first.
```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

def generate_data():
    for i in range(5):
        yield f"Data {i}\n"

@app.get("/stream")
def stream():
    return StreamingResponse(
        generate_data(),
        media_type="text/plain"
    )
```
#### Why use it?
* The main benefit is that the client can start receiving and processing data immediately, without waiting for the complete response to be generated.

#### Where is it useful?
* Common use cases:
  * Large files
  * Large datasets
  * Video/audio streaming
  * Real-time logs
  * AI/LLM generated responses
* Long-running processes where you want to send partial output