### What is dependency injection in FastAPI? How does it work?
- Dependency injection in FastAPI allows you to manage dependencies that can be injected into your endpoints. These dependencies can be things like database connections, authentication services, or other reusable services.
```python
from fastapi import Depends

def get_db():
    db = DatabaseConnection()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
async def read_items(db: DatabaseConnection = Depends(get_db)):
    items = db.fetch_items()
    return items
```
- In this example, the **get_db** function provides a database connection that is automatically injected into the read_items endpoint.