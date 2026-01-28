### **Ques. What is Concrete Method?**
- A concrete method is a method that is completely implemented in a class and can be called directly by creating an object of that class.
* A concreate method is a method whose action is defined in the abstract class itself.
- Example:- 
```python
class Animal:
    def sound(self):   # concrete method
        print("Animal makes a sound")

obj = Animal()
obj.sound() # Output:- Animal makes a sound
```

### Concrete Method inside Abstract Class?
- Yes! An abstract class can contain concrete methods.
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    def start(self):        # concrete method
        print("Vehicle started")

    @abstractmethod
    def mileage(self):
        pass
```
- ✔️ start() is concrete
- ❌ mileage() is abstract

```python
from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self): 
        pass                                # method without body

    def show(self):
        print("concrete method")            # concrete Method / method with body
```
- Example 2
```python
class Father:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def show_data(self):
        print(self.first_name)

obj = Father('mohit','saxena')
obj.show_data() # Output:- mohit
```

### Concrete Method inside Abstract Class?


### Concrete Method vs Abstract Method
- Abstract Method ❌ (No implementation)
- Concrete Method ✅ (Has implementation)