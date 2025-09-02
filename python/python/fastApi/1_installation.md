### Create a file main.py with:
```python
from fastapi import FastAPI
from typing import Union
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello, welcome to!"}

@app.post("/")
async def post():
    return {"message": f"Hello, from the post route!"}

@app.put("/")
async def put():
    return {"message": f"Hello, from the put route!"}

@app.get("/first_page/", description="This is first api", deprecated=True)
async def first_page_function():
    return "Hello my first page url"


# Enum
# include package - from enum import Enum
class foodEnum(str, Enum):
    fruits = "fruits"
    vagitable = "Vagitable"
    dairy = "Dairy"

@app.get("/foods/{food_name}")
def getFoods(food_name:foodEnum):
    if food_name == foodEnum.vagitable:
        return {"food_name": food_name }
    if food_name == foodEnum.fruits:
        return{
            "food_name": food_name
        }
    else:
        return{
            "food_name": food_name
        }

# Path Parameter    
@app.get("/items")
def list_item():
    return {"message": f"Hello, list item route!"}

@app.get("/items/{item_id}")
def list_item(item_id: int):
    return {"message": f"Hello, list item id {item_id} route!"}


fake_item_db = [{"item_name":"Foo"},{"item_name":"asdgf"},{"item_name":"Foqwro"},{"item_name":"Fozxvo"}]

@app.get("/items/fake_item_db")
def list_items(skip:int = 0, limit:int = 10):
    return fake_item_db[skip : skip + limit]

@app.get("/items/{item_id}")
def get_item(item_id, q: Optional[str]=None, short: bool = False):
# def get_item(item_id, q:str | None = None):
    item = {"item_id": item_id}
    if q:
        item.update( {"item_id":item_id, "q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
    return {"item_id":item_id}


@app.get("/user/{user_id}/items/{item_id}")
async def multipal_parameter(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id":user_id}
    if q:
        item.update( {"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```
* Response Body
```python
class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Union[float, None] = None

@app.post("/items")
async def create_items(item: Item):
    # return item
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```

### Run the server with:
```python
uvicorn main:app --reload

uvicorn main:app --host 127.8.4.8 --port 12   # Difrent port

# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [28720]
# INFO:     Started server process [28722]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
```
```python
Open your browser at http://127.0.0.1:8000/
Open your browser at http://127.0.0.1:8000/docs
Open your browser at http://127.0.0.1:8000/items
```


### Extra code

```python
@app.get("/product/{product_id}/")
def item_function(product_id):
    return {"product id":product_id}

@app.get("/product/{product_id}/")
def item_function(product_id:int):      #product id for type casting 
    return {"product id":product_id}   

# query parameter
@app.get("/queryp")
def query_parameter_function(q:int=8):
    return {"product id":q}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```





### FastApi Templates
```python
pip install jinja2
```

* add some important librariry
```python
# Main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

```