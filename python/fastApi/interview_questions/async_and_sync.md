### What is the difference between async and sync views in FastAPI?
- async views are asynchronous and allow FastAPI to handle multiple requests concurrently, making them ideal for I/O-bound operations like network calls or database queries.
- sync views are synchronous and execute each request one at a time. FastAPI supports both, but async views are preferred when working with I/O-bound operations for better performance.
```python
# Async view
@app.get("/async-endpoint")
async def async_view():
    await some_async_function()
    return {"message": "Async Response"}

# Sync view
@app.get("/sync-endpoint")
def sync_view():
    some_sync_function()
    return {"message": "Sync Response"}
```