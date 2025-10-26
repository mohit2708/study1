<!-- 🧰 🧱 🪵 🧪 🧯 📜 🔎 🧹 💣 🛑 ❌ 👉 👈 🧠 ✅ 📌 🔧 🧪 🔍 -->

|  No.  | [Python Oops Interview Questions](./7_oops/1_oops.md)                                                                                           |
| :---: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|       | [Object-Oriented Programming (OOPS)?](#object-oriented-programming-oops)                                                                        |
|       | [What is __init_ _ Method?](#ques-what-is-init-method)                                                                                         |
|       | [What is the use of self in Python?](#ques-what-is-the-use-of-self-in-python)                                                                   |
|       | [What is break, continue and pass in Python?](#ques-what-is-break-continue-and-pass-in-python)                                                  |
|       | [What is issubclass()?](#ques-what-is-issubclass)                                                                                               |
|       | [What is __str_ _ and __repr_ _?](#ques-what-is-str-and-repr)                                                                                   |
|       | [What is Concrete Method?](#ques-what-is-concrete-method)                                                                                       |
|       | [Difference between method and function?](#ques-difference-between-method-and-function)                                                         |
|       | ------------------------------------------------------------------------------------------------                                                |
|       | [What is Class?](#class)                                                                                                                        |
|       | [Python get Class Variables/attributes](#python-get-class-variablesattributes)                                                                  |
|       | [Set/Change values for class variables](#setchange-values-for-class-variables)                                                                  |
|       | [Delete class variables](#delete-class-variables)                                                                                               |
|       | [Built-In Class Functions (getattr, setattr, delattr, hasattr) In Python?](#built-in-class-functions-getattr-setattr-delattr-hasattr-in-python) |
|       | [What is class meta?](#what-is-class-meta)                                                                                                      |
|       | ------------------------------------------------------------------------------------------------                                                |
|       | [What is Object?](#ques-what-is-object)                                                                                                         |
|       | [Delete the Object?](#ques-delete-the-object)                                                                                                   |
|       | [Counting the Number of objects of a Class?](#ques-counting-the-number-of-objects-of-a-class)                                                   |
|       | ----------------------------------------------------------------                                                                                |
|       | [What is Inheritance?](#ques-what-is-inheritance)                                                                                               |
|       | [Single Inheritance](#single-inheritance)                                                                                                       |
|       | [Multiple Inheritance](#multiple-inheritance)                                                                                                   |
|       | [Multi-Level Inheritance](#multi-level-inheritance)                                                                                             |
|       | [Hierarchical Inheritance](#hierarchical-inheritance)                                                                                           |
|       | [Hybrid Inheritance](#hybrid-inheritance)                                                                                                       |
|       | ------------------------------------------------------------------------------------------------                                                |
|       | [What is Encapsulation?](#ques-what-is-encapsulation)                                                                                           |
|       | ------------------------------------------------------------------------------------------------                                                |
|       | [What is Polymorphism?](#ques--what-is-polymorphism)                                                                                            |
|       | ------------------------------------------------------------------------------------------------                                                |
|       | [What is a constructor](#ques-what-is-a-constructor-in-python)                                                                                  |
|       | [Types of Constructors (Default, Non-parametrized, Parameterized)](#types-of-constructors-default-non-parametrized-parameterized)               |
|       | [Constructor With Default Values?](#ques-constructor-with-default-values)                                                                       |
|       | [Constructor Overloading](#ques-constructor-overloading)                                                                                        |
|       | [What is Destructors?](#ques-what-is-destructors)                                                                                               |
|       | ------------------------------------------------------------------------------------------------                                                |
|       | [Python Access Modifiers?](#python-access-modifiers)                                                                                            |
|       | [private attributes and method?](#private-attributes-and-method)                                                                                |
|       | [What is the super() Function](#ques-what-is-the-super-function)                                                                                |
|       | [MRO(Method Resolution Order) / Diamond Problam?](#ques-what-is-mromethod-resolution-order--diamond-problam)                                    |
|       | [What is Abstract Class?](#ques-what-is-abstract-class)                                                                                         |
|       | [When use abstratc class?](#ques-when-use-abstratc-class)                                                                                       |
|       | [How to Create an Abstract Method](#how-to-create-an-abstract-method)                                                                           |
|       | [Built-In Class Attributes?](#built-in-class-attributes)                                                                                        |
|       | [What is Method Overloading?](#ques-what-is-method-overloading)                                                                                 |
|       | [What is Method Overriding?](#ques-what-is-method-overriding)                                                                                   |
|       | [What is Method?](#ques-what-is-method)                                                                                                         |
|       | [What is static method?](#what-is-static-method)                                                                                                |


<div style="page-break-before: always;"></div>

# Oops
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


### **Ques. What is __str__ and __repr__?**
#### ✅ **str Function**
* The __str__ method also known as a **dunder method/double underscore method**, that defines the string representation of an object. 
* It's used to return a **human-readable** string when the built-in functions str() or print() are called on an instance of a class.
```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'I am a {self.name}'
        
obj = Student("mohit")
print(obj)  # Output:- I am a mohit

# Without str
# Without a __str__ method, Python uses the default representation
class Student:
    def __init__(self, name):
        self.name = name
        
obj = Student("mohit")
print(obj)  # Output:- <__main__.Student object at 0x7dc248f35c70>
```

#### ✅ **repr Function**
* The **repr() method** returns a string containing a printable representation of an **object**.
* **__repr__** method returns a string representation of an object that is **machine-readable**.
  
```python
import datetime
today = datetime.datetime.now()
print(str(today))   # 2025-05-11 10:47:08.923663 (Readable end user format)
print(repr(today))  # datetime.datetime(2025, 5, 11, 10, 47, 8, 923663) (official developmrnt format)
```
<div style="page-break-before: always;"></div>
	
### **Ques. What is Concrete Method?**
* A concreate method is a method whose action is defined in the abstract class itself.
```python
from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self): 
        pass                                # method without body
    def show(self):
        print("concrete method")            # concrete Method / method with body
```

```python
class Father:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def show_data(self):
        print(self.first_name)

obj = Father('mohit','saxena')
obj.show_data()
```
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

# Python Access Modifiers
### **Python Access Modifiers**
* **Public Member:** Accessible anywhere from outside the class.
* **Private Member:** private attributes and method Accessible only within the class.
* **Protected Member:** Accessible within the class and it's sub-classes.
```python
#defining class Student
class Student:
    #constructor is defined
    def __init__(self, name, age, salary):
        self.age = age             # public Attribute
        self._name = name          # protected Attribute 
        self.__salary = salary     # private Attribute

    def _funName(self):            # protected method
        pass
 
    def __funName(self):           # private method
        pass

# object creation   
obj = Student('Mohit',53434)
```

#### **Public access modifier:-**
* By default, all the variables and member functions of a class are public in a python program.
```python
class MyClass:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the class
my_object = MyClass("Mohit", 30)

# Access public attributes and call public methods
print(my_object.name)  # Output: Mohit
print(my_object.age)   # Output: 30
my_object.greet()      # Output: Hello, my name is Mohit and I am 30 years old.
```
<div style="page-break-before: always;"></div>

#### **protected access modifier:-**
* **protected Access Modifier:-** Accessible within the class and it's sub-classes.
* adding a prefix _(single underscore) to a variable name makes it protected.
```python
#example1
class MyClass:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def _protected_method(self):  # Protected method
        print(f"Hello, {self._name}!")

    def public_method(self):
        self._protected_method()
        
class SubClass(MyClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def access_protected(self):
        print(f"My name is {self._name} and I am {self.age} years old.")

objsubclass = SubClass("mohit", 30)
# access the Protected variable
print(objsubclass._name) # Output:- Mohit
# access the prProtected method
objsubclass._protected_method() # Output:- Hello, mohit!
objsubclass.access_protected() # Output:- My name is mohit and I am 30 years old.
```
<div style="page-break-before: always;"></div>


#### **private access modifier:-**
* Private attributes are denoted with a double underscore prefix (__) and are intended for internal use within a class, not to be accessed or modified directly from outside.
* Private attributes & method are meant to be used only within the class and are not accessibale from the outside the class.
* agar humne double underscore se kisi ko private kar diya hai to use usi class ke function call kar payenge.
* hum diractly hello function ko call nahi kar sakte hai kyuki hello function private hai agar hame karana hai to usi class mai dusra function banakar welcome banakar usme call karenge phir welcome function ko call karenge to call ho jayega.
  
```python
class MyClass:
    __name = "mohit saxena"
    def __init__(self, public_attr, private_attr):
        self.public_attr = public_attr  # Public attribute
        self.__private_attr = private_attr  # Private attribute

    def public_method(self):
        print(f"Public attribute: {self.public_attr}")
        print(f"Private attribute: {self.__private_attr}")  # Accessing private attribute within the class

    def __private_method(self):
        print("Private method call")

    def get_private_method_result(self):
        # Call the private method from within a public method
        return self.__private_method()
    
    def get_name(self):
        return MyClass.__name


# ++++++ Create an instance ++++
my_object = MyClass("public value", "private value")


# +++++++ access the variable +++++++++++
# access the class variable using mangled
print(MyClass._MyClass__name)   # Output:- Mohit saxena
print(my_object._MyClass__name) # Output:- Mohit saxena

# access the class variable using get method
print(my_object.get_name())

# +++ Accessing public attributes and methods +++++
print(my_object.public_attr)    # Output:- public value
my_object.public_method()   # Output:- Public attribute: public value , Private attribute: private value


# ++++++++ Accessing the private method using get method +++++++++
my_object.get_private_method_result() # Output:- my_object.get_private_method_result()

# Accessing the private method using its mangled name
my_object._MyClass__private_method()  # Private method call

# ++++++++++ Attempting to access a private attribute directly will raise an AttributeError ++++++
# print(my_object.__private_attr) #This will raise an error
```

```python
class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("2582123", "pass@123")
print(acc1.reset_pass())    # Output:- pass@123
```

### **using mangled name**
```python
class MyClass:
    def __init__(self):
        self.name = "mohit"
        self.__private_method()

    def __private_method(self):
        print("This is a private method.")

# Create an instance of MyClass
obj = MyClass()

# Attempting to call the private method directly will raise an AttributeError
# obj.__private_method()  # Uncommenting this line will raise an error

# Accessing the private method using its mangled name
"""
In Python, a mangled name refers to the modified name of a class attribute or method that has been defined with a double underscore prefix (__). This name mangling is a mechanism used to prevent name clashes in subclasses and to provide a level of encapsulation.

When you define a method or attribute with a double underscore, Python automatically changes its name to include the class name as a prefix. This is done to avoid accidental access or modification of the method or attribute from outside the class or from subclasses.
"""
obj._MyClass__private_method()  # This will work
```



### Why are access modifiers important in programming?
* Access modifiers improve security by limiting the accessibility of elements and preventing unauthorized access.
* The access modifier is a keyword that controls the accessibility of the class, hides the internal implementations, and enhances security.
* Access modifiers are important as they control the accessibility of code, promote encapsulation, hide the internal implementation, and maintain security.
<div style="page-break-before: always;"></div>



### **Ques. What is MRO(Method Resolution Order) / Diamond Problam?**
* MRO is a concept used in **inheritance**.
* MRO stands for Method Resolution Order. MRO defines the order of the inherited methods in the child class.
* In Python, the MRO is from **bottom to top** and **left to right**. This means that, first, the method is searched in the class of the object. If it’s not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.

```python
# Example1
  A
  |
  B
class A:
  def method(self):
    print("A.method() called")

class B(A):
  def method(self):
    print("B.method() called")

b = B()
b.method()  # output:- B.method() called
```

```python
# Example2
    B   A
    |   |
    |_C_|
class A:
  def method(self):
    print("A.method() called")

class B:
  pass

class C(B, A):
  pass

c = C()
c.method() # Outpur:- print("A.method() called")

# example_3
class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()  # Output:- A.method() called
```

```python
# Example:-
class father():
    def display(self):
        print("father class method")

class mother():
    def display(self):
        print("mother class method")
        
        
class son(mother,father):                  # left to right 
    def showS(self):
        print("son class method")

obj = son()
obj.showS()     # Output:- son class method
obj.display()   # Outpur:- mother class method

# if we change the ordering then
class son(father, mother):                  # left to right 
    def showS(self):
        print("son class method")

obj = son()
obj.showS()     # Output:- son class method
obj.display()   # Output:- father class method

------------------------------------------------------------------------
# Using Constructor
class father():
    def __init__(self):
        super().__init__()      # Calling Parent Class Constructor
        print("father class Constructor")
    def showF(self):
        print("father class method")

class mother():
    def __init__(self):
        super().__init__()      # Calling Parent Class Constructor
        print("mother class Constructor")
    def showM(self):
        print("mother class method")
class son(father, mother):                  # left to right 
    def __init__(self):
        super().__init__()      # Calling Parent Class Constructor 1st Wala
        print("son class Constructor")
    def showS(self):
        print("son class method")

obj = son()

Output:-
mother class Constructor
father class Constructor
son class Constructor
```

```python
# call parent call using obj
class mother():
    def __init__(self):
        super().__init__()      # Calling Parent Class Constructor
        print("mother class Constructor")

class father():
    def __init__(self):
        print("father class Constructor")

class son(father, mother):                  # left to right 
    def __init__(self):
        print("son class Constructor")

obj = son()
obj.__class__.__bases__[1].__init__(obj)    # 0 if father or 1 is mother class son(father, mother):

#output:
son class Constructor
mother class Constructor
```
<div style="page-break-before: always;"></div>


### **Ques. What is Abstract Class?**
* We cannot create an abstract class in Python directly. However, Python does provide a module that allows us to define abstract classes. The module we can use to create an abstract class in Python is abc(abstract base class) module.
**Rule**
* we can not create objects of an abstract class (abstract class ka hum object nahi bna sakte hai).
* It is not neccessary to declare all methods abstract in a abstract class.
* Abstract class can have abstract method and concreate method.
* If there is any abstract method in a class, that class must be abstract.
* The abstract methods of an abstract class must be defined in its child class/subclass.


### **Ques. When use abstratc class?**
* We use abstract class when there are some common feature shered by all the objects as they are.

### 📌 **How to Create an Abstract Method**
* Import the required tools from the abc module.
* Use the @abstractmethod decorator above your method.
* Make the class inherit from ABC (Abstract Base Class).

```python
from abc import ABC, abstractmethod  # Step 1

class Animal(ABC):  # Step 2: Inherit from ABC

    @abstractmethod  # Step 3: Use decorator
    def make_sound(self):  # Abstract method
        pass

```
<div style="page-break-before: always;"></div>

**Example:-**
```python
# gun is common features
# Defence Forse
#   Gun:- Ak 47
#   Area:- --
--------------------------
#   army:- Gun Ak 47,    Area:- Land
#   Air Force:- Gun Ak 47,    Area:- Sky
#   Navy:-      Gun Ak 47,    Area:- Sea
```

```python
from abc import ABC
class <Abstract_Class_Name>(ABC):
```
```python
from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self,a,b):
        pass

    def show(self):
        print("concreate class")

class child(Father):
    def disp(self,a,b):
        print(a+b)
        print("defining abstrat class")

class child2(Father):
    def disp(self,a,b):
        print(a*b)
        print("defining abstrat class")
c = child()
c.disp(10,50)
c.show()

c2 = child2()
c2.disp(10,30)

👉 Output:-
60
defining abstrat class
concreate class
300
defining abstrat class
```
<div style="page-break-before: always;"></div>



### **Ques. What is Method Overloading?**
* Two or more methods have the same name but different numbers of parameters, These methods are called overloaded methods.
```python
class Addition:
	# first sum for 2 params
	def my_sum(self, a, b):
		return a + b
	
	# second overloaded sum for 3 params
	def my_sum(self, a, b, c):
		return a + b + c

obj = Addition()
# print(obj.my_sum(3, 4))
print(obj.my_sum(3, 4, 5))  # Output: 12
```

### **Ques. What is Method Overriding?**
* When a child class method has the same name, same parameters, and same return type as a method.
```python
class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")

class Car(Vehicle):
    # overridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 Km/Hour")

# Creating object of Car class
car = Car()
car.max_speed()

Output:- max speed is 200 Km/Hour
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
<div style="page-break-before: always;"></div>


### **What is static method?**
* static method don't use the self parameter.
* static method ko hum object ke sath bhi call kar sakte hai or class ke stah bhi.
```python
class Student:
    
    @staticmethod
    def hello():
        print("hello")
    
stu1 = Student()
stu1.hello()        # output:- Hello  
Student.hello()     # output:- Hello
```