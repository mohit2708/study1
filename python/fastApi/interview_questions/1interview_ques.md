### What is FastAPI, and how does it differ from other web frameworks?
* FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
* It was created by **Sebastian Ramirez** in **December 5, 2018**.

#### Key features
* **High performance:** FastAPI is one of the fastest Python frameworks available, built on Starlette for its web parts and Pydantic for its data parts. This architecture allows it to deliver very high throughput comparable to frameworks written in Go or Node.js.
* **Fast to code:** The framework's design can significantly increase the speed of feature development. It is easy to learn, with minimal code duplication.
* **Automatic data validation:** By leveraging standard Python type hints, FastAPI can automatically validate data for incoming requests. If the data is invalid, it returns clear and automatic error messages.
* **Automatic interactive documentation:** Based on OpenAPI standards (formerly Swagger), FastAPI automatically generates interactive API documentation. This includes two user interfaces, Swagger UI (/docs) and ReDoc (/redoc), for exploring and testing API endpoints directly in the browser.
* **Asynchronous support:** Built on the ASGI standard, FastAPI supports async and await syntax, allowing it to handle numerous concurrent requests efficiently, particularly for I/O-bound tasks.
* **Dependency injection:** It features a powerful and easy-to-use dependency injection system that allows for creating modular and testable code. Dependencies, such as database sessions or authentication logic, can be defined as function parameters and are automatically managed.
* **Built-in security:** The framework includes features for implementing security and authentication, such as OAuth2 with JSON Web Tokens (JWT).

#### Core components
* FastAPI is built on top of several high-performance Python libraries:
  * **Pydantic:** Used for data validation and serialization. It utilizes Python type hints to define data models, ensuring that data conforms to the expected structure and types.
  * **Starlette:** A lightweight ASGI framework that provides FastAPI with its core web functionality, including WebSocket support, background tasks, and CORS handling.
  * **Uvicorn:** A high-performance ASGI server used to run FastAPI applications. 


### Here are the key differences between FastAPI and Flask?
|       Aspect        | FastAPI                                                                                                                                          | Flask                                                                                                            |
| :-----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Architectural Model | Built on ASGI (Asynchronous Server Gateway Interface), enabling high-performance asynchronous (non-blocking) request handling.                   | Built on WSGI (Web Server Gateway Interface), a synchronous model that handles one request at a time per worker. |
|     Performance     | Significantly faster, especially for I/O-bound tasks that benefit from asynchronous capabilities like database lookups or calling external APIs. | Slower for concurrent, I/O-heavy applications because its synchronous nature can cause requests to block.        |
|   Data Validation   | Has automatic, built-in data validation and serialization using Pydantic, which leverages Python type hints to reduce bugs.                      | Requires developers to manually perform validation or install external libraries like Marshmallow or WTForms.    |
|Documentation|Automatically generates interactive API documentation (Swagger UI and ReDoc) from your code.|Does not have built-in automatic documentation, requiring manual configuration or extensions.|
|Async Support|Offers first-class support for async and await syntax, making it efficient for high-concurrency and real-time applications.|Is fundamentally synchronous, though newer versions have added limited async support that is less performant than FastAPI's native approach.|


### How FastAPI Handles Requests and Responses?
* FastAPI uses ASGI (Asynchronous Server Gateway Interface) to handle requests asynchronously.
1. **Request Processing:** Incoming requests are parsed and validated against type hints.
2. **Path Operation:** Routes requests to appropriate path operation functions
3. **Dependency Injection:** Resolves dependencies before executing the handler
4. **Data Validation:** Automatically validates request data using Pydantic models
5. **Response Generation:** Serializes response data and generates appropriate HTTP responses


### Route Definition Syntax
```python
from fastapi import FastAPI
```
```python
app = FastAPI()
# Basic GET route
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Route with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST route with request body
@app.post("/items/")
def create_item(item: Item):
    return item
```

### Types of Request Parameters
* Path Parameters
* Query Parameters
* Request Body
* Header Parameters
* Cookie Parameters

#### Basic route syntax
```python
from fastapi import FastAPI

app = FastAPI()

# Define an endpoint for GET requests to the root URL "/"
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# Define an endpoint for POST requests to "/items/"
@app.post("/items/")
async def create_item():
    return {"message": "Item created"}
```

#### Path parameters 
* Path parameters with types
  * We can capture dynamic parts of the URL (called path parameters) by enclosing them in **curly braces {}** in the path string. FastAPI automatically passes these values to the decorated function as keyword arguments.
```python
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


### Path Parameters vs Query Parameters
#### Path Parameters
* Part of the URL path
* Required by default
* Declared in the path string with {parameter_name}
* Example: /users/{user_id} → user_id is a path parameter
#### Query Parameters
* Come after ? in the URL
* Optional by default (can be made required)
* Declared as function parameters
* Example: /users?skip=0&limit=10 → skip and limit are query parameters


### Response Model Syntax
```python
from pydantic import BaseModel
```
```python
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

class ItemResponse(BaseModel):
    name: str
    price: float

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    return item

# Response model with list
from typing import List
@app.get("/items/", response_model=List[ItemResponse])
def read_items():
    return items
```

### what is Dependency Injection in FastAPI?
* Dependency Injection is a design pattern where components receive their dependencies from external sources rather than creating them internally. FastAPI has a powerful dependency injection system.
```python
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Assume this is your database setup
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# 1. Define the dependency: A function that provides a database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Use `yield` to allow for cleanup after the request
    finally:
        db.close() # The session is closed automatically after the endpoint completes

@app.get("/users/")
# 2. Declare the dependency in your endpoint
def read_users(db: Session = Depends(get_db)):
    # 3. FastAPI injects the 'db' session, which you can now use
    users = db.query(User).all()
    return users
```

#### Benefits:
* Code reusability
* Easy testing
* Separation of concerns
* Automatic validation


### Exception and Error Handling


### what is Handling CORS
* Handling CORS (Cross-Origin Resource Sharing) is the process of configuring your web server to allow web browsers to access resources from a different "origin" than the one that served the original webpage. In FastAPI, this is done with the CORSMiddleware.

### What is an "origin"?
*  An origin is defined by the combination of its protocol, domain, and port. For example, https://www.example.com, https://api.example.com, and http://www.example.com:8080 are all considered different origins. 
*  

### Pydantic in FastAPI
* Pydantic is a Python library that provides data validation and settings management using Python type annotations.
* Usage in FastAPI:
  * Request body validation
  * Response model definition
  * Configuration management
  * Data serialization/deserialization

```python
from pydantic import BaseModel, validator
from typing import Optional
class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    
    @validator('email')
    def email_must_contain_at(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
```

### Background Tasks
* Background tasks allow you to run functions after returning a response, useful for operations that don’t need to complete before returning the response.
  * Sending emails
  * Processing files
  * Logging
  * Cache warming
```python
from fastapi import BackgroundTasks
```
```python
def write_log(message: str):
    with open("log.txt", "a") as log:
        log.write(message)
@app.post("/send-notification/")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification sent in the background"}
# Multiple background tasks
@app.post("/process-items/")
async def process_items(background_tasks: BackgroundTasks):
    background_tasks.add_task(task_one, "arg1")
    background_tasks.add_task(task_two, "arg2", keyword="value")
    return {"message": "Tasks started"}
```

### How do you handle errors in a FastAPI application?
- FastAPI provides several ways to handle errors. 
  - We can use try-except blocks to catch exceptions and return custom error responses. 
  - Additionally, FastAPI has built-in support for error handling using the **@app.exception_handler** decorator. This allows you to define custom handlers for specific exception types.

### How do you implement authentication and authorization in a FastAPI application?
- FastAPI provides several options for implementing authentication and authorization, including:
  - Using **OAuth2** with libraries like **fastapi-security**
  - Implementing JWT (JSON Web Tokens) using libraries like **python-jose**
  - Using session-based authentication with libraries like **fastapi-session**
- You can also use external services like **Auth0** or **Okta** to handle authentication.


### How do you optimize the performance of a FastAPI application?
- To optimize the performance of a FastAPI application, you can:
  - Use async/await syntax to write non-blocking code
  - Use caching mechanisms like Redis or Memcached to reduce database queries
  - Optimize database queries using indexing and efficient query methods
  - Use a load balancer to distribute traffic across multiple instances
  - Monitor performance metrics using tools like Prometheus and Grafana

### How do you deploy a FastAPI application?
- FastAPI applications can be deployed in several ways, including:
  - Using a **WSGI** server like **Gunicorn** or uWSGI
  - Using an **ASGI** server like **uvicorn** or hypercorn
  - Deploying to a cloud platform like AWS Elastic Beanstalk or Google Cloud App Engine
  - Using a containerization tool like Docker

### Can you explain the concept of async/await in FastAPI?
- Async/await is a syntax for writing non-blocking code that allows your application to handle multiple requests concurrently. In FastAPI, async/await is used to define coroutines that can be executed asynchronously. This allows your application to handle multiple requests without blocking, improving performance and scalability.

### How do you validate user input in a FastAPI application?
- FastAPI provides several ways to validate user input, including:
  - Using Pydantic models to define validation rules for incoming data
  - Using the @app.validator decorator to define custom validation logic
  - Using external libraries like **marshmallow** or **cerberus** for validation


### Can you explain the difference between a route and an endpoint in FastAPI?
- In FastAPI, a route is a path that maps to a specific handler function. An endpoint is a specific URL that can be used to interact with the application. 
- For example, /users might be a route that maps to a handler function that returns a list of users, while /users/123 might be an endpoint that returns a specific user.


### How do you handle file uploads in a FastAPI application?
- FastAPI provides support for handling file uploads using the Request object and the File class from the fastapi.datastructures module. You can also use external libraries like python-magic to handle file uploads.

### Can you explain how to use WebSockets in a FastAPI application?
- FastAPI provides support for WebSockets using the **WebSocket class** from the **fastapi.websockets module**. You can use this to establish real-time communication between the client and server, allowing for bidirectional messaging and event-driven programming.

### How do you handle CORS (Cross-Origin Resource Sharing) in a FastAPI application?
- FastAPI provides built-in support for handling CORS using the CORSMiddleware class from the fastapi.middleware.cors module. You can configure this middleware to allow specific origins, methods, and headers.

12. Can you explain how to use background tasks in a FastAPI application?

Background tasks are used to run tasks asynchronously in the background. In FastAPI, you can use libraries like background_tasks or celery to handle background tasks. These tasks can be used to perform long-running operations without blocking the main thread.

13. How do you implement logging in a FastAPI application?

FastAPI provides support for logging using the logging module from Python's standard library. You can also use external libraries like loguru or structlog to handle logging. It's recommended to configure logging at the start of your application and use it throughout.

14. Can you explain how to use FastAPI with a database?

FastAPI supports several databases, including relational databases like PostgreSQL and MySQL, as well as NoSQL databases like MongoDB and Cassandra. You can use libraries like sqlalchemy or pymongo to interact with your database. FastAPI also provides support for ORMs (Object-Relational Mappers) like pydantic-sqlalchemy.

15. How do you handle pagination in a FastAPI application?

Pagination is used to limit the number of results returned by an API endpoint. In FastAPI, you can use query parameters like limit and offset to implement pagination. You can also use libraries like paginate or sqlalchemy-pagination.

16. Can you explain how to use FastAPI with Docker?

FastAPI applications can be containerized using Docker. To do this, you need to create a Dockerfile that installs the required dependencies and copies your application code into the container. Then, you can build and run the container using Docker.

17. How do you handle authentication with JWT (JSON Web Tokens) in a FastAPI application?

FastAPI provides support for authenticating users with JWT tokens using libraries like python-jose or fastapi-security. You can use these libraries to verify and validate JWT tokens sent by clients.

18. Can you explain how to use FastAPI with GraphQL?

GraphQL is an alternative to traditional REST APIs that allows clients to specify exactly what data they need. In FastAPI, you can use libraries like graphene or ariadne to implement a GraphQL API.

### How do you handle errors and exceptions in a FastAPI application using try-except blocks?
- Try-except blocks are used to catch exceptions that occur during the execution of your code. In FastAPI, you can use these blocks to handle errors and return custom error responses.

20. Can you explain how to use OpenAPI (Swagger) documentation with a FastAPI application?

OpenAPI (formerly Swagger) is an API description standard that allows clients to discover and interact with APIs programmatically. FastAPI provides built-in support for generating OpenAPI documentation using the FastAPI class.

21. How do you handle sensitive data in a FastAPI application?

Sensitive data includes secrets, passwords, and other confidential information. In FastAPI, you can use libraries like python-dotenv or secureconfig to manage sensitive data securely.

22. Can you explain how to implement rate limiting in a FastAPI application?

Rate limiting is used to limit the number of requests an API endpoint receives within a certain time period. In FastAPI, you can use libraries like fastapi-rate-limit or slowApi to implement rate limiting.

23. How do you handle caching in a FastAPI application?

Caching involves storing frequently accessed data in memory or on disk so that subsequent requests for the same data can be served quickly. In FastAPI, you can use libraries like fastapi-caching or redis to implement caching.

24. Can you explain how to use Webhooks with a FastAPI application?

Webhooks involve sending HTTP callbacks from one server to another in response to certain events. In FastAPI, you can use webhooks to send notifications to clients when data changes.
