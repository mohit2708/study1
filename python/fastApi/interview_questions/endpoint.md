### How do you define an endpoint in FastAPI?
- We can define an endpoint in FastAPI using the @app.get(), @app.post(), @app.put(), @app.delete() decorators. Here’s an example:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
```
- In this example, the root endpoint (/) responds with a JSON message when accessed via a GET request.

### We can use summary, description and tag
```python
@app.get("/", summary="Path parameters", description="Path parameters api", tags=["Path parameters"])
def first_page_function():
    return {"msg":"Hello FastAPI🚀"}
```

#### Basic route syntax
```python
from fastapi import FastAPI

app = FastAPI()

# Handles GET requests
@app.get("/")
def first_page_function():
    return {"msg":"Hello FastAPI🚀 to read data"}

# Handles POST requests
@app.post("/post_route")
def post_function():
    return {"msg":"calling post routes🚀 for create data"}

@app.post("create_product")
async def create_product(new_product: dict):
    return {"response": "product create succesfully!", "new product": new_product}

# Handles PUT requests
@app.put("/put_route")
def put_function():
    return {"msg":"calling put routes🚀 to update data"}

@app.put("/product/{product_id}")
async def update_product(product_id: int, update_product: dict):
    return {"response": "Product updated successfully!", "new_update_product": update_product, "product_id": product_id}

# Handles PATCH requests
@app.patch("/patch_route")
def patch_function():
    return {"msg":"calling patch routes🚀"}

@app.patch("/product/{product_id}")
async def partial_product(product_id: int, update_product: dict):
    return {"response": "partial updated successfully!", "new_update_product": update_product, "product_id": product_id}    

# Handles DELETE requests
@app.delete("/delete_route")
def delete_function():
    return {"msg":"calling delete routes🚀 to delete data"}

@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {"response": "delete updated successfully!","product_id": product_id}

# Handles HEAD requests
@app.head("/items/{item_id}")
def head_item(item_id: int):
    # This will return the headers without a body
    pass
```