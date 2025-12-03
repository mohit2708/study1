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