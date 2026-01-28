### Difference between arguments and parameters?
#### Parameters
- Variables listed in a **function definition**
- Act as **placeholders** to receive values
```python
def add(a, b):   # a, b → parameters
    return a + b
```

#### Arguments
- Actual **values passed** to the function when calling it
```python
add(10, 20)     # 10, 20 → arguments
```

```python
def greet(name):        # name → parameter
    print("Hello", name)

greet("Mohit")          # "Mohit" → argument
```

#### Types of Arguments in Python
- Positional arguments
- Keyword arguments
- Default arguments
- Variable-length arguments (*args, **kwargs)
  
1. Positional Arguments
- Values are passed in order.
```python
def add(a, b):
    print(a + b)

add(10, 20)

# ❌ Order matters:
add(20, 10)   # Different result if logic depends on order
```
2. Keyword arguments
- Arguments passed using parameter names.
```python
def greet(name, age):
    print(name, age)

greet(age=25, name="Mohit")
```
3. Default arguments
- Parameters with default values.
```python
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25
print(power(5, 3))   # 125

```
4. Variable-length arguments (*args, **kwargs)
- Accepts multiple keyword arguments.
```python
def info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

info(name="Mohit", age=25, city="Delhi")
```