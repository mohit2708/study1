|  No.  | Query Parameter                                                                     |
| :---: | ----------------------------------------------------------------------------------- |
|       | [Query Parameter](#query-parameter)                                                 |
|       | [Query parameters:- define multiple?](#how-do-you-define-multiple-query-parameters) |
|       | [Query parameters:- restrict values](#how-do-you-restrict-query-parameter-values)   |
|       | [What is Query() in FastAPI?](#what-is-query-in-fastapi)                            |
|       | [Path Parameter vs Query Parameter](#path-parameter-vs-query-parameter)             |
|       | [Query parameter optional?](#how-do-query-parameter-optional)                       |

<div style="page-break-before: always;"></div>

### 🎯**Query Parameter?**
* A Query Parameter is a value that is passed in the URL after the ? symbol. It is commonly used for **filtering**, **searching**, **sorting**, and **pagination**.
* Query Parameter URL mein ? ke baad aata hai aur data ko filter ya search karne ke liye use hota hai.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products(category: str = None):
    return {"category": category}

# request
GET /products?category=electronics
```

#### **How do you define multiple query parameters?**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(page: int = 1, limit: int = 10, name: str | None = None):
    return {
        "page": page,
        "limit": limit,
        "name": name
    }

# request :- GET /users?page=2&limit=5&name=Mohit
```
<div style="page-break-before: always;"></div>

#### **How do you restrict query parameter values?**
* In FastAPI, you can restrict query parameter values using **Query validations** such as **min_length**, **max_length**, **ge**, **le**, and **pattern**.
* **Example:-**
* Restrict String Length
```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users")
def get_users(name: str = Query(..., min_length=3, max_length=20)):
    return {"name": name}
```
* Restrict Numeric Range
```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
def get_items(page: int = Query(1, ge=1, le=100)):
    return {"page": page}
```
* Restrict to Specific Values
```python
from typing import Literal

@app.get("/products")
def get_products(category: Literal["mobile", "laptop", "tablet"]):
    return {"category": category}

# Only these values are allowed: mobile, laptop, tablet
```
<div style="page-break-before: always;"></div>

#### **What is Query() in FastAPI?**
* Query() is a FastAPI function used to validate and configure query parameters.
* It allows you to add validation rules such as:
  * ge → Greater than or equal to
  * le → Less than or equal to
  * min_length → Minimum string length
  * max_length → Maximum string length
  * pattern → Regex validation

```python
@app.get("/users")
def get_users(
    page: int = Query(1, ge=1, le=100)
):
    return {"page": page}
```

* **Pehla 1 default value hai.** Matlab agar user page pass nahi karta, to FastAPI automatically page = 1 le lega.
* In Query(1, ge=1, le=100), the **first 1 is the default value.** If the client does not provide the query parameter, FastAPI uses 1 automatically.

* **String Validation Example**
```python
@app.get("/search")
def search(
    name: str = Query(..., min_length=3, max_length=20)
):
    return {"name": name}
```


### 🎯**Path Parameter vs Query Parameter**
| Path Parameter                       | Query Parameter                    |
| ------------------------------------ | ---------------------------------- |
| `/users/101`                         | `/users?id=101`                    |
| Specific resource identify karta hai | Filter/search ke liye use hota hai |
| Required hota hai                    | Usually optional hota hai          |
<div style="page-break-before: always;"></div>

### 🎯**How do query parameter optional?**
* In FastAPI, you can make a parameter optional by giving it a default value, commonly None, and using **Optional** or **| None**.
* **HIndi:-** Parameter ko optional banane ke liye uski default value None set kar dete hain.

#### Using None
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name: str | None = None):
    return {"name": name}
```

#### Using Optional
```python
from typing import Optional

@app.get("/users")
def get_users(name: Optional[str] = None):
    return {"name": name}
```