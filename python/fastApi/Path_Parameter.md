|  No.  | Path Parameter                                                                  |
| :---: | ------------------------------------------------------------------------------- |
|       | [Path Parameter](#path-parameter)                                               |
|       | [define multiple path parameters?](#how-do-you-define-multiple-path-parameters) |
|       | [validate path parameters](#how-do-you-validate-path-parameters)                |
|       | [What is Path()](#what-is-path)                                                 |
<div style="page-break-before: always;"></div>


### 🎯**Path Parameter**
* A Path Parameter is a **value that is passed as part of the URL path**. 
* It is used to **identify a specific resource**.
* Path Parameter is a variable that is included in the URL path and it is used to **identify a specific resource**. In FastAPI, path parameters are defined using curly braces {} in the route.
* **Hindi:-** Path Parameter URL ke andar pass kiya jata hai aur kisi specific record ko identify karne ke liye use hota hai.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Request
GET /users/101

# Response
{
    "user_id": 101
}
```

### 🎯**How do you define multiple path parameters?**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```
<div style="page-break-before: always;"></div>

### **How do you validate path parameters?**
* In FastAPI, path parameters can be validated using **Path()** with constraints such as **ge**, **gt**, **le**, and **lt**.
```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(..., ge=1, le=1000) # ... means the parameter is required.
):
    return {"user_id": user_id}
```

### **What is Path()?**
* Path() is a FastAPI function used to validate and add metadata to path parameters.
* It allows you to apply rules such as:
  * ge → Greater than or equal to
  * gt → Greater than
  * le → Less than or equal to
  * lt → Less than
* **...** means the parameter is required.
* **Hindi:-** Path() ka use path parameter validation ke liye hota hai.
```python
user_id: int = Path(..., ge=1)
```