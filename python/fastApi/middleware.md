### What is Middleware?
* Middleware is a component that executes before and after a request reaches the FastAPI route handler. It is commonly used for logging, authentication, request tracking, rate limiting, and modifying requests or responses.
* Middleware ek aisa component hai jo request aur response ke beech mein intercept karta hai.

#### Middleware ka use kahan hota hai?
* Request Logging
* Authentication / Authorization
* Rate Limiting
* Request Processing Time Calculate Karna
* Custom Headers Add Karna
* CORS Handling
* Exception Handling

### How does Middleware work in FastAPI?
* Middleware request aur response ke beech mein layer ki tarah kaam karta hai.
* Jab client request bhejta hai:
  * Request pehle middleware ke paas aati hai.
  * Middleware request ko inspect/modify kar sakta hai.
  * call_next(request) request ko endpoint tak bhejta hai.
  * Endpoint response return karta hai.
  * Response wapas middleware ke paas aata hai.
  * Middleware response ko inspect/modify kar sakta hai.
  * Final response client ko bhej diya jata hai.
* 👉 Last registered middleware first execute hota hai request ke time, aur response ke time reverse order mein return hota hai.

### What is the purpose of call_next() in FastAPI?
* call_next() ka kaam request ko next middleware ya actual endpoint (route handler) tak bhejna hota hai.
* Agar call_next() nahi call karoge, to request endpoint tak pahunch hi nahi paayegi.

### Can multiple middlewares be used in FastAPI?
* Yes, FastAPI supports multiple middlewares. Requests pass through each middleware before reaching the endpoint, and responses pass back through the middlewares in reverse order. This allows separation of concerns such as logging, authentication, rate limiting, and monitoring.
* Yes, FastAPI mein multiple middlewares use kar sakte hain.
* Har request ek middleware chain se guzarti hai. Request endpoint tak jaane se pehle sab middlewares execute hote hain, aur response aate waqt reverse order mein execute hote hain.

### What is the execution order of middlewares?
* FastAPI executes middlewares in reverse order for incoming requests (last registered middleware runs first). For outgoing responses, the execution order is reversed again, so the first registered middleware processes the response first. This follows the LIFO (Last In, First Out) pattern.
* FastAPI mein middleware execution stack (LIFO - Last In, First Out) ki tarah hota hai.
  * **Request ke time:** Last registered middleware pehle execute hota hai.
  * **Response ke time:** First registered middleware pehle response receive karta hai

### What is CORS Middleware in FastAPI?
* CORS middleware in FastAPI is used to control cross-origin requests. It allows the backend to specify which origins, HTTP methods, headers, and credentials are permitted when a browser-based frontend accesses the API.
* **HINDI**
* CORS = Cross-Origin Resource Sharing
* CORS Middleware ka use tab hota hai jab frontend aur backend different origins par run kar rahe hote hain.
```python
Frontend → http://localhost:3000
Backend  → http://localhost:8000
```
* Yahan port different hai, isliye ye different origins hain.
* Browser by default frontend ko kisi different origin par API request karne se restrict kar sakta hai. CORS middleware browser ko batata hai ki kaunse origins, methods aur headers allowed hain.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

| Option              | Meaning                                           |
| ------------------- | ------------------------------------------------- |
| `allow_origins`     | Kaunse origins allowed hain                       |
| `allow_methods`     | Kaunse HTTP methods allowed hain                  |
| `allow_headers`     | Kaunse request headers allowed hain               |
| `allow_credentials` | Cookies/auth credentials allow karne hain ya nahi |

#### Why is CORS required?
* CORS is required to securely allow communication between a frontend and backend running on different origins. It lets the server define which origins, methods, and headers are allowed for browser-based requests.
* CORS required hota hai because browser security reasons ki wajah se ek origin ka frontend normally kisi different origin ke backend ko freely access nahi kar sakta.