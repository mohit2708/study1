1. get Docstrings:- using __doc__ and inspect ex:- className.__doc__ , className.funcName.__doc__


## OOPS

### Oops:- Class
- class is a collection of objects/attributes and method.
#### Get Class Variables/attributes
- Using getattr() function
- Using Object
```python
class Student:
    name = 'mohit saxena'
    roll_no = '12845678'
    
print(Student.name)     # mohit saxena
print(Student.roll_no)  # 12845678

# using getattr() function
name = getattr(Student, 'name')
print(name)

# Using object
obj= Student() 
print(obj.name) # mohit saxena
``` 
#### Set/Change values for class variables
- set the value **using class**
- using **setattr()** built-in function
- using **object**
```python
class Student:
    name = 'mohit saxena'
    roll_no = 12845678

# set the value using class
Student.roll_no = 10     
print(Student.roll_no)    # output:- 10

# using setattr() built-in function
setattr(Student, 'roll_no', 10)
print(Student.roll_no)  # output:- 10

# using **object**
obj= Student() 
obj.name = 'saxena mohit' 
print(obj.name) # Output:- saxena mohit
```

#### Delete class variables
- using **delattr()** function:
- using del keyword
```python
class Student:
    name = 'mohit saxena'
    roll_no = '12845678'
    
print(Student.name)     # mohit saxena
print(Student.roll_no)  # 12845678

# using **delattr()** function:
delattr(Student, 'roll_no') # Output:- AttributeError: type object 'Student' has no attribute 'roll_no'

# using del keyword
del Student.roll_no
print(Student.roll_no)  # Output:- AttributeError: type object 'Student' has no attribute 'roll_no'
```

### Object

##