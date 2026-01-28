### What is the role of Pydantic in FastAPI?
- Pydantic is used for data validation and serialization in FastAPI. It ensures that the data passed to endpoints is of the correct type and structure. FastAPI automatically uses Pydantic models for request body validation and response models.
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

