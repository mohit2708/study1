|  No.  | Endpoint Questions                    |
| :---: | ------------------------------------- |
|       | [GET endpoint](#what-is-get-endpoint) |
|       | [POST endpoint](#post-endpoint)       |
|       | [PUT vs PATCH](#put-vs-patch)         |

<div style="page-break-before: always;"></div>

### 🎯**What is GET endpoint?**
* In FastAPI, a GET endpoint is created using the **@app.get() decorator**. The decorator defines the URL path, and the function below it handles the incoming GET request and returns the response, usually as a Python dictionary which FastAPI automatically converts to JSON.
* Hindi:- FastAPI में GET endpoint बनाने के लिए @app.get() decorator का उपयोग किया जाता है।
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

# Output:-
{
  "message": "Hello FastAPI"
}
```

### 🎯**POST endpoint**
* In FastAPI, a POST endpoint is created using the **@app.post() decorator**. 
* We usually define a Pydantic model to validate the request body, and FastAPI automatically converts the incoming JSON into a Python object.

```python
@app.post("/items")
def create_item():
    return {"message": "Item created successfully"}
```

### 🎯**PUT vs PATCH**
* PUT → Entire resource ko update karta hai.
* PATCH → Sirf specified fields ko update karta hai.