### what is CROS?
* Cross-Origin Resource Sharing (CORS) is a security mechanism in web browsers that prevents a web page from making requests to a different "origin" than its own. In FastAPI.
* CORS is handled via the **CORSMiddleware**, which allows you to configure specific, trusted origins that can interact with your API.
* Handling CORS (Cross-Origin Resource Sharing) is the process of configuring your web server to allow web browsers to access resources from a different "origin" than the one that served the original webpage. In FastAPI, this is done with the **CORSMiddleware**.

### What is an "origin"?
*  An origin is defined by the combination of its protocol, domain, and port. For example, https://www.example.com, https://api.example.com, and http://www.example.com:8080 are all considered different origins. 
  
#### You can configure it in your FastAPI application using the CORSMiddleware.
* You can configure it in your FastAPI application using the CORSMiddleware.
  * Import CORSMiddleware.
  * Create a list of allowed origins (as strings).
  * Add it as a "middleware" to your FastAPI application.
* You can also specify whether your backend allows:
  * Credentials (Authorization headers, Cookies, etc).
  * Specific HTTP methods (POST, PUT) or all of them with the wildcard "*".
  * Specific HTTP headers or all of them with the wildcard "*".
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
```

#### The following arguments are supported:
* allow_origins - A list of origins that should be permitted to make cross-origin requests. E.g. ['https://example.org', 'https://www.example.org']. You can use ['*'] to allow any origin.
* allow_origin_regex - A regex string to match against origins that should be permitted to make cross-origin requests. e.g. 'https://.*\.example\.org'.
* allow_methods - A list of HTTP methods that should be allowed for cross-origin requests. Defaults to ['GET']. You can use ['*'] to allow all standard methods.
* allow_headers - A list of HTTP request headers that should be supported for cross-origin requests. Defaults to []. You can use ['*'] to allow all headers. The Accept, Accept-Language, 
* ontent-Language and Content-Type headers are always allowed for simple CORS requests.
* allow_credentials - Indicate that cookies should be supported for cross-origin requests. Defaults to False.
* None of allow_origins, allow_methods and allow_headers can be set to ['*'] if allow_credentials is set to True. All of them must be explicitly specified.
* expose_headers - Indicate any response headers that should be made accessible to the browser. Defaults to [].
* max_age - Sets a maximum time in seconds for browsers to cache CORS responses. Defaults to 600.