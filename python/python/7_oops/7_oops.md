<!-- 🧰 🧱 🪵 🧪 🧯 📜 🔎 🧹 💣 🛑 ❌ 👉 👈 🧠 ✅ 📌 🔧 🧪 🔍 -->

|  No.  | [Python Oops Interview Questions](./7_oops/1_oops.md)                                            |
| :---: | ------------------------------------------------------------------------------------------------ |
|       | [Object-Oriented Programming (OOPS)?](#object-oriented-programming-oops)                         |
|       | [What is the use of self in Python?](#ques-what-is-the-use-of-self-in-python)                    |
|       | [What is break, continue and pass in Python?](#ques-what-is-break-continue-and-pass-in-python)   |
|       | [What is __str_ _ and __repr_ _?](#ques-what-is-str-and-repr)                                    |
|       | ------------------------------------------------------------------------------------------------ |
|       | [What is class meta?](#what-is-class-meta)                                                       |
|       | ------------------------------------------------------------------------------------------------ |
|       | [private attributes and method?](#private-attributes-and-method)                                 |
|       | [Built-In Class Attributes?](#built-in-class-attributes)                                         |


<div style="page-break-before: always;"></div>


### **Object-Oriented Programming (OOPS)**
* Object-oriented programming (OOP) is a programming style that organizes code around objects, rather than functions and logic.
* Main Concepts of Object-Oriented Programming (OOPs) 
* [Class](#ques-What-is-Class)
* [Objects](#ques-What-is-Object)
* Polymorphism
* Encapsulation
* Inheritance
* Data Abstraction
<div style="page-break-before: always;"></div>  

### **What is Python Enumeration?**
* In Python, an enumeration (or "enum") is a class that defines a set of symbolic names (constants) that are bound to unique, constant values. Enums are created using the enum module and are typically used to represent groups of related constants, making code more readable and maintainable.
```python
from enum import Enum

class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

# Accessing enum members by name:
print(TrafficLight.RED.name)  # Output: RED
print(TrafficLight.GREEN.value) # Output: 3

# Accessing enum members by value:
print(TrafficLight(1).name) # Output: RED
print(TrafficLight(3).value) # Output: 3
```
<div style="page-break-before: always;"></div>


### **Ques. What is Method?**
* The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods.

#### **Ques. Types Of Methods In Python?**
There are three types of methods in Python.
1. Instance Methods.
2. Class Methods.
3. Static Methods.

* **Instance Method**
* when we create classes in python. If we want to print an instance variable or instance method we must create an object of that required class.
* If we are using self as a function parameter or in front of a variable, that is nothing but the calling instance itself.
* As we are working with instance variables we use self keyword.
* __Note:-__ Instance variables are used with instance methods.
```python
class Student: 
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def avg(self):
        return (self.a + self.b) / 2

s1 = Student(10, 20)
print( s1.avg() )

Output:- 15.0
```
* **Class Method**
* classsmethod() function returns a class method as output for the given function.
* If we want to create a class method we must use __@classmethod__ decorator and __cls__ as a parameter for that function.
```python
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @classmethod
    def info(cls):
        return cls.name

print(Student.info())

Output:- Student
```

* **Static Method**
* A static method can be called without an object for that class, using the class name directly. If you want to do something extra with a class we use static methods.
* A static method in python must be created by decorating it with __@staticmethod__
```python
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info():
        return "This is a student class"

print(Student.info())

Output:- This a student class
```
```python
class MethodTypes:

    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()

Output:-
Ragnar
Lothbrock
Lagertha
This is a static method
```