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