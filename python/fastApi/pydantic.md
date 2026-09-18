### 🎯**What is Pydantic?**
* Pydantic is a Python library **used for data validation**, parsing, and serialization using Python type hints.
* FastAPI **uses** Pydantic models to:
  * validate incoming request data,
  * convert data into Python objects,
  * and generate JSON responses automatically.
* Pydantic is a Python library that validates and parses data using type annotations. In FastAPI, it is mainly used to define request and response schemas.

#### Example
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user

# Request
{
  "name": "Mohit",
  "age": 25
}

# Response
{
  "name": "Mohit",
  "age": 25
}
```
<div style="page-break-before: always;"></div>

* If the client sends wrong value then showing error:
```python
# Request

{
  "name": "Mohit",
  "age": "abc"
}

# response
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "Input should be a valid integer",
      "type": "int_parsing"
    }
  ]
}
```

### 🎯**How do you make a field optional?**
* To make a field optional in Pydantic, we use **Optional[type]** from the typing module and assign a default value of None.
* Hindi:- Pydantic में किसी field को optional बनाने के लिए Optional और default value None का उपयोग किया जाता है। इससे वह field request में भेजना आवश्यक नहीं रहता।
```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: Optional[str] = None
    phone: str | None = None    # Python 3.10+ Shortcut
```

### 🎯**What is a Pydantic Model?**
* A Pydantic model is a Python class that inherits from BaseModel and is used to define the structure, validation rules, and data types for data.
* FastAPI में इसे request body, response body, और data validation के लिए use किया जाता है।

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str   # string होना चाहिए
    age: int    # integer होना चाहिए
```
* यह पूरा User class ही Pydantic model कहलाता है।


### 🎯**What is BaseModel?**
* BaseModel Pydantic की मुख्य (core) class है।
* BaseModel is the base class provided by Pydantic that enables automatic data validation, parsing, and serialization using Python type hints.
* जब हम कोई class BaseModel को inherit करके बनाते हैं, तो वह class Pydantic model बन जाती है और उसमें automatic:
  * data validation
  * type checking
  * type conversion
  * JSON serialization
  * error handling

### 🎯**How do you validate request data?**
```python
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, lt=120)
    email: EmailStr # Email validation
    username: str = Field(min_length=3, max_length=20)
```

#### String validation
```python
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
```

#### validate numeric values
```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    quantity: int = Field(gt=0, le=100) # Integer Validation
    price: float = Field(gt=0, lt=10000)    # float validation
```

#### How do you validate email?
* In Pydantic, email validation is done using the **EmailStr** type. When a field is declared as EmailStr, Pydantic automatically checks whether the provided value is a valid email address and raises a validation error if the format is incorrect.
* Hindi:- FastAPI / Pydantic में email validate करने के लिए EmailStr का उपयोग किया जाता है।
* EmailStr use करने के लिए package install होना चाहिए:
  
```python
pip install email-validator
```

* Example
```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr # Email validation
    optional_email: Optional[EmailStr] = None   # optional email
```

### 🎯**Custom Validation**
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError("Name should contain only letters")
        return value
```

### 🎯**How do you define default values in Pydantic?**
* In Pydantic, default values are defined by assigning a value to the **field directly** or by **using Field(default=value)**. If the client does not provide that field, Pydantic automatically uses the default value.
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    active: bool = True
    age: int = 18
```

* Using Field()
```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(default=18, gt=0, lt=120)
```

* Optional Field with Default
```python
from typing import Optional

class User(BaseModel):
    city: Optional[str] = "Delhi"
```


### 🎯**What is Pydantic serialization?**
* Pydantic serialization is the process of **converting** a **Pydantic model (Python object)** into a **JSON-compatible** format such as a dictionary or JSON string. It is commonly done **using model_dump()** and **model_dump_json()**. FastAPI automatically uses Pydantic serialization when returning API responses.
* Hindi:- Pydantic serialization वह प्रक्रिया है जिसमें Pydantic model (Python object) को JSON-compatible format जैसे dictionary या JSON string में convert किया जाता है। इसके लिए model_dump() और model_dump_json() methods का उपयोग किया जाता है। FastAPI response भेजते समय इसे automatically use करता है।
* Pydantic models internally Python objects होते हैं, लेकिन API response भेजने के लिए उन्हें JSON में बदलना पड़ता है। यही process Pydantic serialization कहलाती है।


| Python Object              | JSON Response             |
| -------------------------- | ------------------------- |
| User(name="Mohit", age=25) | {"name":"Mohit","age":25} |

1. model_dump():-
2. model_dump_json():-

#### model_dump():-
* model_dump() is a Pydantic v2 method used to convert a Pydantic model into a Python dictionary.
* model_dump() Pydantic v2 का method है जो Pydantic model को Python dictionary में convert करता है। यह serialization के लिए उपयोग किया जाता है और Pydantic v1 के dict() method का replacement है। इसका उपयोग API response, database save, और data processing में किया जाता है।

1. simple example Real life example
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Mohit", age=25)

print(user.model_dump())

# Output:-
{
  "name": "Mohit",
  "age": 25
}
```

#### Why is it Used?
* जब हमें:
  * database में save करना हो,
  * custom JSON response बनाना हो,
  * logging करनी हो,
  * या data को manipulate करना हो,
* तब model_dump() उपयोग करते हैं।

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    data = user.model_dump()
    return {
        "message": "User created",
        "data": data
    }
```

2. Exclude a Field 
```python
user.model_dump(exclude={"age"})

# Output:-
{
  "name": "Mohit"
}
```

3. user.model_dump(include={"name"})
```python

```

### **What is model_validate() in Pydantic?**
* model_validate() is used to validate data and create a Pydantic model instance from a dictionary or other input data.
* In Pydantic v2, model_validate() replaces many uses of parse_obj() from v1.
* **HINDI:-** model_validate() ka use dictionary ya input data ko validate karke Pydantic object banane ke liye hota hai.
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

data = {
    "name": "Mohit",
    "age": 25
}

user = User.model_validate(data)

print(user) # Output:- name='Mohit' age=25
```

### Difference: model_validate() vs model_dump()
| Method             | Purpose               |
| ------------------ | --------------------- |
| `model_validate()` | Dict → Pydantic Model |
| `model_dump()`     | Pydantic Model → Dict |



### 🎯**What is Pydantic deserialization?**
* Pydantic deserialization is the process of converting incoming JSON or dictionary data into a Pydantic model (Python object). During this process, Pydantic automatically validates the data, performs type conversion, and raises validation errors if the input is invalid. FastAPI uses Pydantic deserialization automatically for request bodies.
* Pydantic deserialization वह प्रक्रिया है जिसमें incoming JSON या dictionary data को Pydantic model (Python object) में convert किया जाता है। इस दौरान Pydantic automatically data validation और type conversion करता है। FastAPI request body को handle करने के लिए इसी deserialization process का उपयोग करता है।
* Deserialization is the process of **converting** **JSON or dictionary data** into a **Pydantic model (Python object)**.
* Hindi:- जब client API को JSON भेजता है, तो Pydantic उस JSON को Python object में बदल देता है। इसी को Pydantic deserialization कहते हैं।

### 🎯**What is Field()?**
* Field() is a Pydantic function used to define additional validation rules, default values, and metadata for model fields. It allows us to apply constraints such as min_length, max_length, gt, lt, and also provide descriptions and examples for FastAPI documentation.
* Hindi:- Field() Pydantic का helper function है जिसका उपयोग model की fields पर extra validation, default values, constraints और Swagger documentation metadata लगाने के लिए किया जाता है। इससे हम min_length, max_length, gt, ge जैसी validations आसानी से define कर सकते हैं।

### **How do you create nested Pydantic models?**
* A nested Pydantic model means **one Pydantic model is used inside another model**.
* Nested Pydantic models are created by using one Pydantic model as a field inside another model. This helps validate complex and hierarchical JSON data.
* Agar ek model ke andar doosra model use kiya jaye, to use Nested Pydantic Model kehte hain.
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):  # yaha eke model ke andar dusra model call kara hai
    name: str
    age: int
    address: Address

@app.post("/users")
def create_user(user: User):
    return user

    # How to call   
    user = User.model_validate(data)
    print(user.address.city)   # Noida
```

#### Why Use Nested Models?
* Organize complex data
* Better validation
* Cleaner API schema
* Reusable models

### **How do you validate nested objects?**
* **Nested objects** are **validated** by defining **nested Pydantic models**. Pydantic automatically validates all nested fields and raises a validation error if any required field is missing or has the wrong type.
* Pydantic automatically check karega ki address ke andar city aur state sahi hain ya nahi.