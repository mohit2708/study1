### Udeny
```python
from fastapi import FastAPI, status    # import FastAPI

app = FastAPI() # create a FastAPI "instance"

PRODUCTS = [
    {
        "id": 1,
        "title": "Apple Watch",
        "price": 299.99,
        "description": "A sleek and modern smartwatch from Apple, featuring a touchscreen display and fitness tracking capabilities."
    },
    {
        "id": 2,
        "title": "Sony PlayStation 5",
        "price": 399.99,
        "description": "The latest gaming console from Sony, with improved graphics and performance, and a vast library of games to choose from."
    },
    {
        "id": 3,
        "title": "Nike Air Max Shoes",
        "price": 129.99,
        "description": "Comfy and stylish shoes from Nike, featuring the iconic Air Max technology for maximum comfort and support during athletic activities."
    },
    {
        "id": 4,
        "title": "Samsung 4K Smart TV",
        "price": 999.99,
        "description": "A high-end smart TV from Samsung, with stunning 4K resolution and a wide range of streaming apps and features."
    },
    {
        "id": 5,
        "title": "Dell Inspiron Laptop",
        "price": 699.99,
        "description": "A reliable and feature-packed laptop from Dell, perfect for work or play, with a long-lasting battery and a range of configuration options."
    }
]

# GET Request
# Read and fetch all data


@app.get("/product")
async def all_product():
    return PRODUCTS

@app.get("/product/{product_id}")
async def single_product(product_id:int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
        

@app.post("/product")
async def create_product(new_product:dict):
    PRODUCTS.append(new_product)
    return PRODUCTS

        
@app.put("/product/{product_id}")
async def update_product(product_id: int, update_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[index] = update_product  # Update the actual dictionary
            return {"status": "update", "product_id": product_id, "new_product_update": update_product}
        
@app.patch("/product/{product_id}")
async def patch_product(product_id: int, update_product: dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(update_product)
            return {"status": "partialy update", "product_id": product_id, "new_product_update": PRODUCTS[product_id]}

@app.delete("/product/{product_id}")
async def patch_product(product_id: int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"status": "delete product update", "product_id": product_id}
```