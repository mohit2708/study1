|  No.  | [Variables]()                                                                   |
| :---: | ------------------------------------------------------------------------------- |
|       | [What is python Variables?](#what-is-python-variables)                          |
|       | [Single Quotes or Double Quotes?](#single-quotes-or-double-quotes-)             |
|       | [what is Global Variables?](#global-variables)                                  |
|       | [what is global Keyword?](#global-keyword)                                      |
|       | [What is None in Python](#what-is-none-in-python)                               |
|       | [Difference between None, NaN, and Null](#difference-between-none-nan-and-null) |
|       | [How is memory managed in Python?](#ques-how-is-memory-managed-in-python)       |
|       | [What is Scope in Python](#what-is-scope-in-python)                             |

### 🎯**What is python Variables?**
* Variables are containers for storing data values.
* A variable name must **start** with a **letter** or the **underscore** character.
* A variable name **cannot** start with a **number**.
* Variable names are **case-sensitive** (age, Age and AGE are three different variables)
```python
#Legal variable names:
myvar = "John"
MYVAR = "John"
my_var = "John"
myVar = "John"
myvar2 = "John"
_my_var = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
```
```python
x = 5
y = "Mohit"
print(x)  # Output:- 5
print(y)  # Output:- Mohit
```

### **Single Quotes or Double Quotes:-** 
* single quotes (' ') and double quotes (" ") are functionally the **same and both are used to create strings**. The choice mainly depends on readability and avoiding unnecessary escaping when the string contains quotes.

```python
x = "John"
print(x)  # Output:- John

# double quotes are the same as single quotes:
x = 'John'
print(x)  # Output:- John

print('He said "Hello"')  # Output:- He said "Hello"
print("It's a beautiful day")
print('It\'s a beautiful day')
print('It's a beautiful day') # Output:- error

```
<div style="page-break-before: always;"></div>

#### **Assign Multiple Values:**
* Python allows you to assign values to multiple variables in one line.
```python
x, y, z = "Orange", "Banana", "Cherry"

print(x)  # Output:- Orange
print(y)  # Output:- Banana
print(z)  # Output:- Cherry
```

#### **One Value to Multiple Variables:** 
* we can assign the same value to multiple variables in one line.
```python
x = y = z = "Orange"

print(x)  # Output:- Orange
print(y)  # Output:- Orange
print(z)  # Output:- Orange
```

* **Variables Casting:** We want to specify the data type of a variable, this can be done with casting. and We can **get the data type** of a variable with the **type()** function.
```python
x = str(3)
y = int(3)
z = float(3)

print(x) # output 3
print(y)  # output 3
print(z)  # output 3.0
```
```python
x = 5
y = "John"
print(type(x))
print(type(y))

Output:-
<class 'int'>
<class 'str'>
```

* **Unpack a Collection:** If we have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

Output:-

apple
banana
cherry
```


__Output Variables(combine both text and a variable)__
```python
x = "awesome"
print("Python is " + x)

output:- Python is awesome

# Example 2
-----------
x = "Python is "
y = "awesome"
z =  x + y
print(z)

output:-Python is awesome
```

```python
x = 5
y = 10
print(x + y)
```
output:- 15<br>

Note:- If you try to combine a string and a number, Python will give you an error:
```python
x = 5
y = "John"
print(x + y)
output:- TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
<div style="page-break-before: always;"></div>

### 🎯**Global Variables?**
 * Variables that are created outside of a function.
 * Global variables can be used by everyone, both inside of functions and outside.
```python
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

output:- Python is awesome
```

```python
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

output:- 
Python is fantastic
Python is awesome
```
<div style="page-break-before: always;"></div>

### 🎯**Global Keyword?**
* To create a global keyword inside a function should be treated as a global variable, you can use the **global keyword**.
```python
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x) # Output:- Python is fantastic
```

* Also, use the global keyword if you want to change a global variable inside a function.
```python
x = 10  # Global variable
def modify_global():
    global x
    x = 20  # Changing the value of the global variable

modify_global()
print(x)  # This will print 20
```

### 🎯**What is None in Python?**
- None in Python **represents the absence of a value** and is commonly used to indicate that a variable has no assigned value or a function returns nothing.
- Important Rule:- Always use is / is not with None.
```python
# Always compare with None using:
if x is None:

# Avoid:
if x == None:
```

### 🎯**Difference between None, NaN, and Null**
1. None
   1. Represents **absence of a value**
   2. An **object** of type NoneType
2. NaN (Not a Number)
   1. Represents invalid or undefined numeric value
   2. Comes from math operations
   3. Used in floating-point calculations
   4. Common in NumPy / Pandas / Data Science
3. Null
   1. NOT used in Python, Used in Java, JavaScript, PHP, C, C++


### 🎯**How is memory managed in Python?**
* Memory management in Python is handled by the **Python Memory Manager**. 
* Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.
* Memory management in python is managed by **Python private heap space**. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
* The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.


### 🎯**What is Scope in Python?**
* Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program.
* Scope means **“WHERE can I use this variable?”**
* scope resolution in python follows the **LEGB rules**.
  * Local(L): Defined inside function/class
  * Enclosed(E): Defined inside enclosing functions(Nested function concept)
  * Global(G): Defined at the uppermost level
  * Built-in(B): Reserved names in Python builtin modules

1. **Global Scope/Global Variables:-** The Variable which can be **read from anywhere** in the program is known as a global scope. These variables can be accessed inside and outside the function. 
```python
x = 300 # global variable
def myfunc():
    print(x)

myfunc() # Outpur:- 300
print(x) # Outpur:- 300
```

2. **Local Variable**
```python
def show():
    y = 5   # local variable
    print(y)

show()  # 5
print(y)   # ❌ Error - y cannot be accessed outside the function
```

3. **NonLocal or Enclosing Scope:-** Nonlocal Variable is the **variable that is defined in the nested function**. It means the variable can be neither in the local scope not in the global scope.
```python
def func_outer():
    x = "local"
    def func_inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    func_inner()
    print("outer:", x)
func_outer()

# Output:-inner: nonlocal
# outer: nonlocal   
```
<div style="page-break-before: always;"></div>

3. **Built-in Scope:-** If a Variable is not defined in local, Enclosed or global scope, then python looks for it in the built-in scope. In the Following Example, 1 from math module pi is imported, and the value of pi is not defined in global, local and enclosed. Python then looks for the pi value in the built-in scope and prints the value. Hence the name which is already present in the built-in scope should not be used as an identifier.
```python
# Built-in Scope 
from math import pi 
# pi = 'Not defined in global pi'
def func_outer(): 
    # pi = 'Not defined in outer pi' 
    def inner(): 
        # pi = 'not defined in inner pi' 
        print(pi) 
    inner() 
func_outer()

Output:- 3.141592
```

#### **Same Variable Name, Different Scope**
```python
x = 10

def test():
    x = 5   # local variable
    print(x)

test()      # 5
print(x)    # 10
```

