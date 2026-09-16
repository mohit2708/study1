### **What is the use of self in Python?**
* The Self parameter is a **reference** to the **current instance of the class**, we can access the attributes and methods of the class in python.
* We can give **any name** in place of self but **first parameter** is **compulsory**.
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mohit", 36)
p1.myfunc()     # Output:- Hello my name is Mohit
```
```python
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name 
    def myfunc(abc):
        print("Hello my name is " + abc.name) 
p1 = Person("mohit") 
p1.myfunc() # Output:- Hello my name is mohit
```