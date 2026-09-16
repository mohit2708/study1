### **What is __init__ Method?**
* **__init__** is a constructor method in Python, and is **automatically called** to allocate memory when a **new object/instance is created**.
* All classes have a function called __init__() function, whatever you create them or not, which is always excuted when the object is being initiated.
```python
class Student:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("My name is " + self.firstname + " " + self.lastname)
       
    def stdInfo(self):
        print("My name is " + self.firstname + " " + self.lastname)
    
# creating a new object 
stu1 = Student("Mohit", "Saxena") #output:- My name is Mohit Saxena
stu1.stdInfo()  #output:- My name is Mohit Saxena

print(stu1.firstname)   # Output:- Mohit
print(stu1.lastname)    # Output:- Saxena
```