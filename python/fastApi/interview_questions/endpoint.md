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

