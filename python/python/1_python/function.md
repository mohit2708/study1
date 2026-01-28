### What is a function?
- A function is a reusable block of code that performs a specific task.
- Instead of writing the same code again and again, you define it once and call it whenever needed.

#### Why do we use functions?
- Code reusability
- Better readability
- Easy maintenance
- Avoid repetition (DRY principle)
- Modular programming

#### Function in Python (Syntax)
```python
def function_name(parameters):
    # code block
    return value
```
- Example
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)   # Output:- 30
```

#### Types of Functions in Python
1. Built-in Functions
- Provided by Python
```python
print(), len(), type(), range()
```

2. User-defined Functions
- Created by the programmer
```python
def greet(name):
    print("Hello", name)
```

3. Functions with / without parameters
```python
def hello():
    print("Hi")

def square(x):
    return x * x
```

4. Functions with / without return value
```python
def show():
    print("No return")

def get_number():
    return 10
```

5. Lambda (Anonymous) Functions
```python
square = lambda x: x * x
```

#### Function Call
```python
greet("Mohit")
```

#### Advantages of Functions
- Reduces code length
- Improves testing
- Makes debugging easier
- Supports teamwork

