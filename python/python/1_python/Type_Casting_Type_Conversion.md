### **Ques. Type Casting/Type Conversion?**
* The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. 
* When we convert the value of one data type to the value of another data type, we call this type conversion.

* Integers
```python
x = int(1)
y = int(2.8)
z = int("3")
print(x)    # Output:- 1
print(y)    # Output:- 2
print(z)    # Output:- 3
```
* Floats
```python
# Floats
x = float(1)
y = float(2.8)
z = float("3")
print(x)    # Output:- 1.0
print(y)    # Output:- 2.8
print(z)    # Output:- 3.0
```
* Strings
```python
x = str("s1")
y = str(2)
z = str(3.0)
print(x)    # Output:- s1
print(y)    # Output:- 2
print(z)    # Output:- 3.0
```
<div style="page-break-before: always;"></div>

Python has **two** types of type conversion.
1. **Implicit Type Conversion: -** In Implicit type conversion, Python **automatically converts** one data type to another data type. This process doesn't need any user involvement.
```python
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print(type(num_int))    # Output:- <class 'int'>
print(type(num_flo))    # Output:- <class 'float'>
print(num_new)          # Output:- 124.23
print(type(num_new))    # Output:- <class 'float'>
```
   
2. **Explicit Type Conversion: -** In Explicit Type Conversion, **users convert** the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
```python
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

Output:-
Data type of num_int: <class 'int'>
Data type of num_str before Type Casting: <class 'str'>
Data type of num_str after Type Casting: <class 'int'>
Sum of num_int and num_str: 579
Data type of the sum: <class 'int'>
```

##### Note:- 
* If you try to **combine** a **string** and a **number**, Python will give you an **error**:
```python
x = 5
y = "John"
print(x + y)
output:- TypeError: unsupported operand type(s) for +: 'int' and 'str'
```