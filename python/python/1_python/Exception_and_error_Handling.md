### What is Exception Handling?
* Exception handling is a mechanism in Python used to handle runtime errors gracefully so that the program does not terminate unexpectedly.
* Hindi:- Exception Handling ka use Python program mein **runtime errors ko handle karne ke liye hota hai**, taaki error aane par program abruptly terminate na ho aur hum us situation ko properly handle kar saken.
* Exception ek runtime error hoti hai jo program ke execution ke time occur hoti hai.

#### Common Exceptions
| Exception             | Kab aati hai?                         |
| --------------------- | ------------------------------------- |
| `ZeroDivisionError`   | 0 se divide karne par                 |
| `ValueError`          | Invalid value dene par                |
| `TypeError`           | Wrong data type operation             |
| `IndexError`          | Invalid list index                    |
| `KeyError`            | Dictionary mein key nahi mili         |
| `NameError`           | Variable defined nahi hai             |
| `FileNotFoundError`   | File nahi mili                        |
| `AttributeError`      | Object mein attribute/method nahi hai |
| `ImportError`         | Import related problem                |
| `ModuleNotFoundError` | Module nahi mila                      |


#### Python mein mainly ye keywords use hote hain:
* try
* except
* else
* finally
* raise

### Try, Except, else and Finally?
* Exception handling is a way to **manage errors** and unusual conditions that occur during the execution of a program. Instead of crashing the program when an error happens, exception handling allows you to respond to the error gracefully, enabling the program to continue running or to end smoothly.
* When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
* **try:-** try block lets you test a block of code for errors.
* **except:-** The except block lets you **handle the error**.
* **else:-** The **else** block lets you **execute** code when there is **no error**.
* **finally:-**  Finally block **always** gets **executed** either **exception** is **generated or not**


#### Example of try and except
```python
try:
    a = 10
    b = 0
    print(a / b)

except:
    print("Something went wrong")
```

* Specific Exception Handle Karna
```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:- Cannot divide by zero
```

* Multiple Exceptions
```python
try:
    value = int(input("Enter number: "))
    result = 10 / value

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")

# if we put abc then output Please enter a valid number
# if we put 0 then output Number cannot be zero
```

* Multiple Exceptions in One except
```python
try:
    value = int(input("Enter number: "))
    result = 10 / value

except (ValueError, ZeroDivisionError):
    print("Invalid input")
```


#### else Block
* The else block executes only when no exception occurs in the try block.
* else tab execute hota hai jab try block successfully execute ho jaye aur koi exception na aaye.
```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")

# Output:- Calculation successful    
```

#### finally Block
* Finally block **always** gets **executed** either **exception** is **generated or not**
* finally normally execute hota hi hai, chahe exception aaye ya na aaye.
* Without exception:
```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("Finally executed")

# Output:- Finally executed
```
* With exception:
```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error occurred")

finally:
    print("This will always execute")

# Output:-
Error occurred
This will always execute
```

#### try + except + else + finally
```python
try:
    # risky code

except SomeException:
    # handle exception

else:
    # executes if no exception

finally:
    # executes almost always
```
```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")
```


#### raise Keyword
* raise ka use manually exception generate karne ke liye hota hai.
```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")
```

#### Custom Exception
* A user-defined exception created by inheriting from Exception.
* Hum apni khud ki exception class bana sakte hain.
```python
# create
class InsufficientBalanceError(Exception):
    pass

# use
try:
    balance = 1000
    withdraw = 2000

    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance")

except InsufficientBalanceError as e:
    print(e)
```

#### BaseException


####
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

# Output:-
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