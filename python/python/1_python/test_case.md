### What is a test case in Python?
* A test case is a set of inputs, execution conditions, and expected results used to verify that a Python program behaves correctly. Python **provides modules like unittest** and **frameworks like pytest** to write and execute test cases automatically.
* Test Case ek aisa scenario hota hai jisse hum verify karte hain ki code expected output de raha hai ya nahi.

### What is Unit Testing?
* Unit testing is the process of testing individual units of code, such as functions, methods, or classes, independently to verify that they work as expected. In Python, we commonly use unittest or pytest for unit testing.
* **Important**: Unit testing mein external dependencies jaise database, third-party API, payment service ko often mock kiya jata hai, taaki hum sirf apne unit ka behavior test karein.

#### unittest Module Example
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()


# Output:-
python test.py

#
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

### pytest Example
* Industry mein bahut popular
```python
pip install pytest
```

```python
# File: test_add.py
def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

# Run pytest
```


### What is assert?
* assert is a debugging statement used to verify that a condition is true. If the condition evaluates to false, Python raises an AssertionError. It is commonly used in testing frameworks such as pytest to validate expected results.
* assert Python ka ek debugging statement hai jo check karta hai ki condition True hai ya nahi.
  * Agar condition True hai → program normal chalega.
  * Agar condition False hai → AssertionError aayega.


#### Common Assertions
* assertEqual(a, b)
* assertTrue(x)
* assertFalse(x)
* assertIn(a, b)
* assertIsNone(x)
* assertRaises(Exception)

| Assertion              | Meaning                            |
| ---------------------- | ---------------------------------- |
| `assertEqual(a, b)`    | `a == b`                           |
| `assertNotEqual(a, b)` | `a != b`                           |
| `assertTrue(x)`        | x True hona chahiye                |
| `assertFalse(x)`       | x False hona chahiye               |
| `assertIsNone(x)`      | x `None` hona chahiye              |
| `assertIsNotNone(x)`   | x `None` nahi hona chahiye         |
| `assertIn(a, b)`       | `a` should be in `b`               |
| `assertNotIn(a, b)`    | `a` should not be in `b`           |
| `assertRaises()`       | Expected exception check karta hai |


#### Example of assert
```python
age = 20

assert age >= 18

print("Eligible")   # Output:- Eligible
# Kyuki condition True hai.


# =======================================
age = 15

assert age >= 18

print("Eligible")   # Output:- AssertionError
# Kyuki condition False hai.


# Cutome error mesage========================
age = 15

assert age >= 18, "Age must be 18 or above"

# Output:- AssertionError: Age must be 18 or above
```

### What is setUp() and tearDown()?
* setUp() is executed before every test method and is used to prepare test data or resources. tearDown() is executed after every test method and is used to clean up resources such as database connections, files, or objects. They help avoid code duplication and ensure tests run independently.
* Ye unittest framework ke methods hain jo har test case ke pehle aur baad automatically run hote hain.

| Method       | Kab Chalta Hai?          | Use                                                   |
| ------------ | ------------------------ | ----------------------------------------------------- |
| `setUp()`    | Har test method se pehle | Test ke liye data/object create karna                 |
| `tearDown()` | Har test method ke baad  | Cleanup karna (file close, DB connection close, etc.) |

```python
import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        print("Setup Running")
        self.name = "Mohit"

    def test_name(self):
        self.assertEqual(self.name, "Mohit")

    def test_length(self):
        self.assertEqual(len(self.name), 5)

    def tearDown(self):
        print("Cleanup Running")

if __name__ == "__main__":
    unittest.main()

# Output:-
Setup Running
Cleanup Running

Setup Running
Cleanup Running
```

```python
# Real Example (Database)
class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = connect_database()    # setUp() → DB connection open

    def test_user(self):
        pass

    def tearDown(self):
        self.db.close() # tearDown() → DB connection close
```

### What is Integration Testing?
* Integration testing is the **process of testing multiple components or modules together to verify** that they interact and communicate correctly. For example, in a FastAPI application, we can test the interaction between an API endpoint, service layer, and database.
* Integration Testing mein hum check karte hain ki 2 ya usse zyada components/modules ek saath properly kaam kar rahe hain ya nahi.
```python
def test_login():
    response = client.post(
        "/login",
        json={
            "email": "mohit@gmail.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200
```
* Yahan hum sirf login() function ko test nahi kar rahe.
* API → Service → Database → Response is poore interaction ko.

### Unit vs Integration Testing
| Unit Testing                 | Integration Testing                |
| ---------------------------- | ---------------------------------- |
| Individual component         | Multiple components                |
| Function/method/class        | API + Service + DB                 |
| Dependencies often mocked    | Real/test dependencies may be used |
| Fast                         | Comparatively slower               |
| Example: `calculate_total()` | Example: Login API + Database      |





### What is Mock API?
* A Mock API is a simulated API that mimics the behavior of a real API and returns predefined responses. It is used in testing and development to avoid dependency on external services, improve test reliability, and enable testing even when the actual API is unavailable.
* Mocking is a technique used in testing to replace real dependencies such as APIs, databases, or external services with fake objects that return controlled responses. It allows us to test our code independently without making actual external calls.
* Mock API ek fake API/service hoti hai jo real API ki tarah response deti hai, lekin actual external API ko call nahi karti.
* Iska use testing ke liye kiya jata hai jab:
  * Real API abhi bani nahi ho.
  * Real API down ho.
  * External API ko call nahi karna ho.
  * Unit testing karni ho.

#### Python Example using unittest.mock
* using **unittest.mock**
```python
from unittest.mock import patch

@patch("requests.get")
def test_get_user(mock_get):

    mock_get.return_value.json.return_value = {
        "id": 1,
        "name": "Mohit"
    }

    data = get_user()

    assert data["name"] == "Mohit"
```

### Mock API ka use kyu karte hain?
| Reason                 | Explanation                             |
| ---------------------- | --------------------------------------- |
| Fast testing           | Network call nahi hoti                  |
| No external dependency | Real API available hona zaroori nahi    |
| Avoid cost             | Payment/SMS/Email APIs ke charges avoid |
| Predictable response   | Fixed response de sakte hain            |
| Error testing          | 400/500 errors simulate kar sakte hain  |
| Isolated testing       | Sirf apna code test karte hain          |

### Error response bhi mock kar sakte hain
```python
mock_get.return_value.status_code = 500
mock_get.return_value.json.return_value = {
    "error": "Internal Server Error"
}
```



### Mock vs Stub
| Mock                                               | Stub                        |
| -------------------------------------------------- | --------------------------- |
| Behavior verify karta hai                          | Fixed data return karta hai |
| Kis function ko call kiya gaya check kar sakta hai | Sirf response deta hai      |
| `unittest.mock`                                    | Manual fake object          |

### Difference Between unittest and pytest
* Dono Python testing frameworks hain, lekin pytest zyada simple aur popular mana jata hai.
* unittest is Python's built-in testing framework based on xUnit architecture, while pytest is a third-party testing framework that provides simpler syntax, powerful fixtures, parameterized testing, and rich plugin support. Pytest is generally preferred in modern Python projects because it requires less boilerplate code and is easier to maintain.

| Feature             | unittest                            | pytest                            |
| ------------------- | ----------------------------------- | --------------------------------- |
| Built-in            | ✅ Python ke saath aata hai          | ❌ Install karna padta hai         |
| Syntax              | Thoda verbose                       | Simple aur short                  |
| Assertions          | `self.assertEqual()`                | `assert`                          |
| Test Discovery      | Naming rules follow karni hoti hain | Automatic discovery better        |
| Fixtures            | `setUp()` / `tearDown()`            | `@pytest.fixture`                 |
| Parameterized Tests | Complex                             | Easy (`@pytest.mark.parametrize`) |
| Plugins Support     | Limited                             | Bahut saare plugins               |
| Popularity          | Old & standard                      | Modern projects mein zyada use    |


### What is code coverage?
* Code coverage is a metric that measures how much of the application's source code is executed by automated tests. It helps identify untested parts of the code and improves test quality. Common coverage types include line coverage, branch coverage, and function coverage. In Python, code coverage is commonly measured using the coverage.py tool.
* Code Coverage batata hai ki aapke test cases ne application ke kitne code ko execute (cover) kiya hai.
* Code Coverage = (Test se execute hua code / Total code) × 100

#### Example of code coverage?
```python
# Function
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Test
def test_adult():
    assert check_age(20) == "Adult"

yaha sirf return "Adult" wala path test hua.


Lekin: return "Minor" wala path test nahi hua.
Isliye coverage 100% nahi hogi.
```

```python
# Better test
def test_adult():
    assert check_age(20) == "Adult"

def test_minor():
    assert check_age(15) == "Minor"

# * Ab dono paths execute ho gaye. Coverage improve ho jayegi.
```

#### Types of Coverage
| Type               | Meaning                              |
| ------------------ | ------------------------------------ |
| Line Coverage      | Kitni lines execute hui              |
| Statement Coverage | Kitne statements execute hue         |
| Branch Coverage    | Kitne `if-else` branches execute hue |
| Function Coverage  | Kitne functions call hue             |



### How do you test FastAPI endpoints using TestClient?
* FastAPI endpoints are tested using fastapi.testclient.TestClient. It allows sending HTTP requests (GET, POST, PUT, DELETE) to the application without running a live server. We can verify status codes, response bodies, headers, authentication, and database interactions using assertions.
* FastAPI mein API endpoints test karne ke liye TestClient use kiya jata hai.
* TestClient actual server start kiye bina API requests bhejne ki facility deta hai.

```python
# Step 1: FastAPI App
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello Mohit"}

# Step 2: Test File
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Mohit"
    }

# Run Test
pytest

# Output:- 1 passed
```

* POST API Example
```python
# API
from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user(user: dict):
    return {
        "name": user["name"]
    }


# Test
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():

    payload = {
        "name": "Mohit"
    }

    response = client.post(
        "/users",
        json=payload
    )

    assert response.status_code == 200
    assert response.json() == {
        "name": "Mohit"
    }


```
*  Testing Query Parameters
```python
# API
@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}

# Test
def test_add():
    response = client.get(
        "/add?a=10&b=20"
    )

    assert response.status_code == 200
    assert response.json() == {
        "sum": 30
    }
```

* Testing Path Parameters
```python
# API
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# TEst
def test_get_user():
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1
    }
```

* Testing Authentication (JWT Later)
```python
headers = {
    "Authorization": "Bearer test_token"
}

response = client.get(
    "/profile",
    headers=headers
)
```



What is TestClient?
How do you test POST APIs?
How do you mock database dependencies?
What is dependency override in FastAPI?
How do you test authenticated endpoints?
How do you test async endpoints in FastAPI?