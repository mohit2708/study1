### **Ques. What is Decorators?**
* A decorator is a **design pattern** in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
* Decorators are used to add some design patterns to a function without changing its structure.
* A decorator function is a function that accepts a function as parameter and return a function(decorator ek function hai jo as a argument leta bhi function hai and return bhi function karta hai).
* Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
```python
# A simple decorator function
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator
def greet():
    print("Hello, Mohit!")

greet()

# Output:-
Before calling the function.
Hello, Mohit!
After calling the function.
```
##### Explanation:
* decorator takes the greet function as an argument.
* It returns a new function (wrapper) that first prints a message, calls greet() and then prints another message.
* The @decorator syntax is a shorthand for greet = decorator(greet).

##### Syntax of Decorator Parameters
```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper


@decorator_name
def function_to_decorate():
    # Original function code
    pass
```
###### Explanation of Parameters(Syntax of Decorator Parameters)
1. decorator_name(func):
   1. decorator_name: This is the name of the decorator function.
   2. func: This parameter represents the function being decorated. When you use a decorator, the decorated function is passed to this parameter.

2. wrapper(*args, **kwargs):
   1. wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.
   2. *args: This collects any positional arguments passed to the decorated function into a tuple.
   3. **kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.
   4. The wrapper function allows the decorator to handle functions with any number and types of arguments.
3. @decorator_name:
   1. This syntax applies the decorator to the function_to_decorate function. It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate).


* 2nd Type
```python
def num_decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner

# calling type1
@num_decor
def num():
    return 10

print(num())    # Output:- 15

# ---Calling type2---
def num():
    return 10

result = num_decor(num)
print(result()) # Output:- 15
```

* Upper case decorater
```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

# call decorater
decorate = uppercase_decorator(say_hi)
print(decorate())   # Output:-'HELLO THERE'

# -------2nd Opton call decorater----------
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())     # Output:-'HELLO THERE'
```

#### Why do we use Decorators?
* Decorators are useful when you want to add common functionality to multiple functions.
* For example:
  * Logging
  * Authentication
  * Authorization
  * Permission checking
  * Execution time calculation
  * Caching
  * Validation
  * Exception handling
  * Transaction management
  * Rate limiting

#### Passing Function as an Argument
```python
def hello():
    print("Hello")


def execute(func):
    func()


execute(hello)

# Output:- Hello
```

#### Returning a Function
* A function can also return another function.
```python
def outer():

    def inner():
        print("Hello")

    return inner

result = outer()

result()

# Output:- Hello
```

#### Decorator with Function Arguments
```python
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")

        return result

    return wrapper
```
```python
# calling
@decorator
def add(a, b):
    return a + b


result = add(10, 20)
# result = add(a=10, b=20) 

print(result)

# Output:-
Before function
After function
30
```

* hamne func(*args, **kwargs) ye isliye likha hai kyuki user result = add(10, 20) or result = add(a=10, b=20) value de sakta hai.
* *args:- Stores positional arguments: func(10, 20, 30)
* **kwargs:- Stores keyword arguments: func(name="Mohit", age=30)

#### Decorator with Arguments
```python
def repeat(n):

    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper

    return decorator

# use
@repeat(3)
def hello():
    print("Hello")


hello()

# Output:-
Hello
Hello
Hello
```

#### Practical Example
1. Logging Decorator
```python
from functools import wraps


def log_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function completed: {func.__name__}")

        return result

    return wrapper

# USe
@log_function
def add(a, b):
    return a + b

# call
result = add(10, 20)
print(result)

# Output:-
Calling function: add
Function completed: add
30
```

2. Execution Time
```python
import time
from functools import wraps


def execution_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start)

        return result

    return wrapper


# Use:
@execution_time
def test():
    time.sleep(2)
    print("Hello")

test()


# Output:-
Hello
Execution time: 2.00
```