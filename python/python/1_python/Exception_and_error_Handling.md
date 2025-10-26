### What is Exception Handling?
### Try, Except, else and Finally?
* Exception handling is a way to **manage errors** and unusual conditions that occur during the execution of a program. Instead of crashing the program when an error happens, exception handling allows you to respond to the error gracefully, enabling the program to continue running or to end smoothly.
* When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
* **try:-** try block lets you test a block of code for errors.
* **except:-** The except block lets you **handle the error**.
* **else:-** The **else** block lets you **execute** code when there is **no error**.
* **finally:-**  Finally block **always** gets **executed** either **exception** is **generated or not**


```python
# Example_1 for try except
try:
  print(x)
except:
  print("Something went wrong")

Output:-
Something went wrong

# Example_2 for try except else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("execute if no exception")

Output:-
Hello
execute if no exception


# Example_3 for try except else finally
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("execute if no exception")
finally:
  print("always executed")

Output:-
Something went wrong
always executed

# Example_4 for try except else finally
try:
  print("x")
except:
  print("Something went wrong")
else:
  print("execute if no exception")
finally:
  print("always executed")

Output:-
x
execute if no exception
always executed
```
<div style="page-break-before: always;"></div>

#### Types of Errors in Python?
* In Python, errors are generally categorized into two main types: **syntax errors** and **exceptions**. Each of these types can be further divided into more specific categories.
1. Syntax Errors
   1. Missing colons, parentheses, or quotation marks.
   2. Incorrect indentation.
```python
def sample_function()  # Missing colon
    print("Hello, World!")
```

2. Logical Errors:-
   1. Incorrect mathematical operations.
   2. Misused conditional statements.
```python
def add_numbers(a, b):
    return a - b  # Logical error; should be a + b
```

3. Exceptions Handling Error
```python
# ZeroDivisionError
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")      # Output:- You can't divide by zero!


# Index Error
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])  # Accessing an index that doesn't exist
except IndexError:
    print("Index Out of Bound.")    # index is not found


# Name Error
try:
    print(my_variable)
except NameError as e:
    print(f"A NameError occurred: {e}") # A NameError occurred: name 'my_variable' is not defined


# TypeError
try:
    result = "Hello" + 5  # Trying to add a string and an integer
except TypeError as e:
    print(f"A TypeError occurred: {e}") # A TypeError occurred: can only concatenate str (not "int") to str


# Key error
my_dict = {'name': 'Alice'}
try:
    print(my_dict['age'])  # Key 'age' is not in the dictionary
except KeyError:
    print("Error: Key not found in the dictionary.")

# value error
try:
    number = int("abc")  # String is not numeric
except ValueError:
    print("Error: Invalid value for conversion.")


# FileNotFoundError
try:
    with open('non_existent_file.txt') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")

# ImportError
try:
    import non_existent_module
except ImportError:
    print("Error: Module not found.")

# AttributeError
class Sample:
    pass

obj = Sample()
try:
    obj.some_method()  # Method does not exist
except AttributeError:
    print("Error: Attribute not found.")


# EOFError
try:
    input_value = input("Enter something: ")  # Simulate EOF
except EOFError:
    print("Error: End of file reached.")



# Catch Multiple Exceptions in Python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
```



* Python try with else clause
```python
# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

Output:-
Enter a number: 1
Not an even number!

Output:-
Enter a number: 4
0.25

Output:-
Enter a number: 0
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    reciprocal = 1/num
ZeroDivisionError: division by zero
```
* Python try...finally
```python
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")

Output:-
Error: Denominator cannot be 0.
This is finally block.
```


### Errors and Exceptions in Python
1. Syntax Errors:
```python
print("Hello, World!")  # Missing closing parenthesis

#
a = 10000 
if a > 2999
    print("Eligible")

syntax error because there is a missing colon (:) after the if statement.
```

2. Logical Errors:


#### MemoryError
```python
try:
    # Attempting to create a very large list
    large_list = [0] * (10**10)  # Trying to create a list with 10 billion elements
except MemoryError as e:
    print(f"A MemoryError occurred: {e}")
```