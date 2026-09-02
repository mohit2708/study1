|  No.  | FastAPI Questions                                                     |
| :---: | --------------------------------------------------------------------- |
|       | [What is Fastapi](#what-is-fastapi)                                   |
|       | [Fastapi:- Main Features](#main-features)                             |
|       | [FAstapi:- Advantages](#fastapi-advantages)                           |
|       | [FAstapi:- Disadvantages](#fastapi-disadvantages)                     |
|       | [FAstapi:- Example](#simple-example)                                  |
|       | [Describe Fastapi code](#describe-fastapi-code)                       |
|       | [Starlette](#starlette)                                               |
|       | [ASGI](#asgi)                                                         |
|       | [WSGI](#what-is-wsgi)                                                 |
|       | [uvicorn](#uvicorn)                                                   |
|       | [Gunicorn](#gunicorn)                                                 |
|       | [Gunicorn और Uvicorn में Difference](#gunicorn-और-uvicorn-में-difference) |
|       | [FastAPI vs Flask](#fastapi-vs-flask)                                 |
<div style="page-break-before: always;"></div>

### 🎯**What is Fastapi**
- **FastAPI is a modern, high-performance Python web framework used for building RESTful APIs.**
- It is based on **Starlette** for the web framework and **Pydantic** for data validation.
- It automatically generates interactive API documentation using **OpenAPI (Swagger UI)**.
- Hindi: FastAPI ek modern Python web framework hai jo **API (Application Programming Interface)** banane ke liye use hota hai.

#### Main Features
* High Performance (ASGI + Starlette ki wajah se)
* Automatic API Documentation (/docs aur /redoc)
* Data Validation using Pydantic
* Easy JWT Authentication support
* Async programming support (async def)

#### Fastapi Advantages

| Advantage              | Explanation                                                                       |
| ---------------------- | --------------------------------------------------------------------------------- |
| **High Performance**   | ASGI aur Starlette ki wajah se bahut fast hai.                                    |
| **Automatic API Docs** | `/docs` par Swagger UI automatically milta hai.                                   |
| **Data Validation**    | Pydantic automatically request data validate karta hai.                           |
| **Async Support**      | `async/await` support karta hai, isliye concurrent requests handle kar sakta hai. |
| **Easy to Learn**      | Flask jaisa simple syntax hai.                                                    |
| **Type Hint Support**  | Python type hints se IDE auto-completion aur fewer bugs milte hain.               |
| **OpenAPI Support**    | Client SDK aur API testing tools ke saath easily integrate hota hai.              |


#### Fastapi Disadvantages

| Disadvantage                                              | Explanation                                                               |
| --------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Smaller Ecosystem**                                     | Django ke comparison me packages aur plugins kam hain.                    |
| **Built-in Admin Panel Nahi**                             | Django ki tarah ready-made admin interface nahi milta.                    |
| **Authentication Setup Manual Ho Sakta Hai**              | JWT, OAuth, permissions wagaira khud configure karne padte hain.          |
| **Async Concepts Thode Difficult**                        | Beginners ko `async`, `await`, event loop samajhne me time lag sakta hai. |
| **Large Monolithic Apps Ke Liye Extra Structure Chahiye** | Bahut bade projects me architecture manually organize karna padta hai.    |
| **Rapid Changes**                                         | Kuch libraries aur versions frequently update hote rehte hain.            |


#### Simple Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

# Run server
uvicorn main:app --reload

# Output:-
{
  "message": "Hello FastAPI"
}
```

#### Describe Fastapi code 
```python
from fastapi import FastAPI # This imports the **FastAPI** class which is used to create a web application instance.

app = FastAPI() # This creates an application instance of FastAPI.

@app.get("/")   # decorator is a function that modifies another function. “When someone calls / with GET request, execute this function.”
def home():
    return {"message": "Hello World"} # FastAPI automatically converts Python dictionary into JSON response.
```

<div style="page-break-before: always;"></div>

### 🎯**Starlette**
* Starlette is a lightweight **ASGI web framework and toolkit** for building asynchronous web applications in Python.
* FastAPI Starlette ke upar built hai.
* Hindi:- Starlette ek lightweight ASGI web framework hai, jiske upar FastAPI bana hua hai.
* It uses Starlette internally for features such as:
  * Routing
  * Request handling
  * Response handling
  * Middleware
  * Background tasks
  * WebSockets
  * Static files
  * Session support

#### Example
```python
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse({"message": "Hello"})

# Here, JSONResponse comes from Starlette.
```
* Car chalti hai engine ki wajah se, lekin car me extra features hote hain. Usi tarah FastAPI, Starlette ke upar extra features provide karta hai.
<div style="page-break-before: always;"></div>


### 🎯**ASGI**
* ASGI allows a Python web app (FastAPI, Starlette, Django async, etc.) to **communicate** with an asynchronous server (Uvicorn, Hypercorn, Daphne) and handle many requests concurrently using async/await.
* ASGI (Asynchronous Server Gateway Interface) is a specification that allows Python web applications (FastAPI, Starlette, Django async, etc.) to **communicate** with asynchronous servers such as Uvicorn, Hypercorn, and Daphne.
It supports **async/await**, **concurrent requests**, **WebSockets**, and **long-lived connections**.

#### ASGI Application Signature
* ASGI app ka basic structure:
```python
async def app(scope, receive, send):
    pass
```

| Parameter | Purpose                                           |
| --------- | ------------------------------------------------- |
| scope     | Request information (path, method, headers, etc.) |
| receive   | Incoming messages receive karta hai               |
| send      | Response bhejta hai                               |

#### ASGI is Used?
* Handle Multiple requests concurrently
* Support WebSockets
* Support Long-lived connections
* Perform asynchronous operations using async/await

#### ASGI server
| ASGI Server                | Use                                            |
| -------------------------- | ---------------------------------------------- |
| Uvicorn                    | FastAPI में सबसे ज्यादा इस्तेमाल होता है                   |
| Hypercorn                  | HTTP/2 और QUIC जैसी features support करता है       |
| Daphne                     | Django Channels के साथ popular है                 |
| Granian                    | High-performance modern ASGI server            |
| Gunicorn + Uvicorn Workers | Production deployment में बहुत common combination |
<div style="page-break-before: always;"></div>

### **What is WSGI?**
* WSGI (Web Server Gateway Interface) is a standard interface between Python web applications and web servers. Frameworks like Flask and Django use WSGI to communicate with servers such as Gunicorn and uWSGI. WSGI is synchronous and handles one request per worker at a time.
* WSGI (Web Server Gateway Interface) Python web applications aur web servers ke beech communication ka standard interface hai.
* **HINDI:** WSGI web server (Apache, Nginx, Gunicorn) aur Python application (Flask, Django) ke beech bridge ka kaam karta hai.

#### WSGI ki Limitation
* Agar ek request ko 5 seconds lagte hain, to worker us request ke complete hone tak busy rahega.

<div style="page-break-before: always;"></div>

### 🎯**uvicorn**
* Uvicorn is an ASGI server used to run FastAPI applications.
* Uvicorn is a lightweight, high-performance ASGI server used to run FastAPI applications.
* Uvicorn एक ASGI server है जो FastAPI application को run करने के लिए इस्तेमाल किया जाता है।

#### What does Uvicorn do?
* HTTP requests को receive करता है
* ASGI protocol के अनुसार FastAPI से communicate करता है
* Response वापस client को भेजता है
* Async requests को efficiently handle करता है
* WebSocket support भी देता है

#### Note
* ASGI = एक protocol / specification है (rules/नियम)
* Uvicorn = उन नियमों पर काम करने वाला server
* FastAPI = application/ASGI-compatible framework
<div style="page-break-before: always;"></div>

### 🎯**Gunicorn**
* Gunicorn (Green Unicorn) is a Python **WSGI HTTP server** used to run Python web applications such as Django and Flask in production environments. 
* It works by creating a master process and multiple worker processes to handle concurrent HTTP requests efficiently. For ASGI frameworks like FastAPI, Gunicorn is commonly used together with Uvicorn workers.
* **Hindi:-** यह एक Python WSGI HTTP Server है जिसका उपयोग Python web applications (जैसे Django, Flask) को production में चलाने के लिए किया जाता है।

#### Gunicorn कैसे काम करता है?
* Gunicorn एक master process बनाता है और उसके अंदर कई worker processes चलाता है।
```python
Browser
   |
HTTP Request
   |
Gunicorn (Master)
   |
-----------------
|       |       |
Worker1 Worker2 Worker3
   |
Python App
```
* इससे एक साथ कई requests handle हो सकती हैं।

#### FastAPI में Gunicorn क्यों?
* Production में जब ज़्यादा traffic हो, तब केवल एक Uvicorn process कम पड़ सकता है।
* इसलिए हम Gunicorn को **process manager** की तरह उपयोग करते हैं।
* Process Manager का मतलब है ऐसा software जो application के processes को manage करता है।

```python
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

[🔝 Back to Top](#back-to-top)

### 🎯**Gunicorn और Uvicorn में Difference**
| Feature       | Gunicorn                    | Uvicorn            |
| :------------ | :-------------------------- | :----------------- |
| Interface     | WSGI                        | ASGI               |
| Frameworks    | Django, Flask               | FastAPI, Starlette |
| Async support | नहीं (native)                 | हाँ                  |
| Use case      | Traditional Python web apps | Modern async apps  |
<div style="page-break-before: always;"></div>


### 🎯**FastAPI vs Flask**
* Flask is a lightweight web framework, while FastAPI is a modern high-performance API framework with built-in validation, documentation, and async support.
| Feature              | FastAPI                         | Flask                         |
| -------------------- | ------------------------------- | ----------------------------- |
| Release Year         | 2018                            | 2010                          |
| Performance          | Very Fast (ASGI)                | Slower than FastAPI (WSGI)    |
| Async Support        | Built-in (`async/await`)        | Limited, requires extra setup |
| Data Validation      | Automatic with Pydantic         | Manual validation             |
| API Documentation    | Auto-generates Swagger & ReDoc  | Requires extra libraries      |
| Type Hints           | Strongly uses Python type hints | Optional                      |
| Learning Curve       | Slightly higher                 | Easier for beginners          |
| Best For             | REST APIs, Microservices        | Small to Medium Web Apps      |
| Dependency Injection | Built-in                        | Not available by default      |
| WebSocket Support    | Built-in                        | Requires extensions           |

#### Example
* Flask
```python
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"message": "Hello World"}
```

* Fastapi
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}
```