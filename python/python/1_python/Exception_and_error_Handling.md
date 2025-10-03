### Try, Except, else and Finally
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

### Handling Error
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
    print(even_numbers[5])
except IndexError:
    print("Index Out of Bound.")    # index is not found


# Name Error
try:
    print(my_variable)
except NameError as e:
    print(f"A NameError occurred: {e}") # A NameError occurred: name 'my_variable' is not defined


# TypeError
try:
    result = "Hello" + 5  # Attempting to add a string and an integer
except TypeError as e:
    print(f"A TypeError occurred: {e}") # A TypeError occurred: can only concatenate str (not "int") to str




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
print("Hello, World!"  # Missing closing parenthesis

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