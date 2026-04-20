### Path parameters 
* We can capture dynamic parts of the URL (called path parameters) by enclosing them in **curly braces {}** in the path string. FastAPI automatically passes these values to the decorated function as keyword arguments.
```python

# fetch for single product
@app.get("/item/{id}")
def pathParameters(id):
    return {"get return id": id}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # The item_id is automatically converted to an integer
    return {"item_id": item_id}
```

* Path parameters containing paths
```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```


#### Path parameters with types
* We can declare the type of a path parameter in the function, using standard Python type annotations:
```python
# Path parameters with int types
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": f"Item {item_id}"}

# Path parameters with str types
@app.get("/users/{username}")
async def read_user(username: str):
    return {"username": username, "message": f"Hello, {username}!"}

# Path parameters with float types
@app.get("/products/{price}")
async def read_product(price: float):
    return {"price": price, "message": f"The price is ${price:.2f}"}
```

#### Path parameters order matters
```python
@app.get("/product/{product_title}")
async def single_product(product_title: str):
    return {"response": "single data fetched!", "product_title": product_title}

@app.get("/product/tshirt")
async def single_product():
    return {"response": "single data fetched!"}

```


#### Path parameters with types with validation
```python
from fastapi import FastAPI, HTTPException

@app.get("/itemsvalidation/{item_id}")
async def read_item(item_id: int):
    if item_id <= 5:  # Example of custom validation
        raise HTTPException(status_code=400, detail="Item ID must be greater than five.")
    return {"item_id": item_id, "description": f"Item {item_id}"}
```

#### Predefined values using Enum class

* Accessing enum members
  * Compare directly: if item_id is ItemID.gadget:
  * Access the value: item_id.value (e.g., "gadget")
  * Access the name: item_id.name (e.g., "gadget") 
```python
# add
from enum import Enum

class choice_names(str,Enum):
    one="one"
    two="two"
    three="three"

@app.get("/choice-function/{model_name}")
async def choiceFunction(model_name:choice_names):
    if model_name.value == "one":
        return {"model name": model_name, "message":"this is a one"}
    if model_name is choice_names.two2:
        return {"model name": model_name, "message":"this is a two"}
    if model_name.value == "three":
        return {"model name": model_name, "message":"this is a three"}
    if model_name.name == "four4":
        return {"model name": model_name, "message":"this is a four"}
    return model_name
```

```python
from pydantic import BaseModel

class student_details(BaseModel):
    name:str
    Class:str
    roll_no:int

@app.post("/create-student")
async def createStudent(studentDetails:student_details):
    return studentDetails
```

#### Path convertor
- jab hame pura path capture karna ho to path parameter use karna hoga
```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"your requested file at path": file_path}

# example user/sfsaf/abc.text pass in request
```


```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first_page_function():
    return {"msg":"Hello FastAPI🚀"}

@app.get("/first_page")
def first_page_function():
    return "Hello my first page url"

@app.get("/query")
def queryFunction(name:str, roll_no:int):
    var_name = {"name": name , "roll number":roll_no}
    return (var_name)

@app.get("/query-optional-parameter")
def queryFunction(name:str, roll_no: Union[int, None]=None):
    var_name = {"name": name , "roll number":roll_no}
    return (var_name)
```


#### Path parameters
```python

```