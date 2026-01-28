### **Ques. What is the super() Function?**
* Super() method is used to access method and properties of the parant class.
* The **super** function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.
* **Benefits** of using the super() function.
  * We are not required to remember or specify the parent class name to access its methods.
  * We can use the super() function in both single and multiple inheritances.
  * The super() function support code reusability as there is no need to write the entire function
```python
class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()

Output:- Jessa works at Google
```


#### super() with Single Inheritance
```python
class Animal:
    def smell(self,name):
        print(name, "can smell")
        
class Dog(Animal):
    def __init__(self):
        super().smell("Dog")
        
    def bark(self):
        print("Dog can bark")
    
dog = Dog()     # Output:- Dog can smell
dog.bark()  # Output:- Dog can bark
```
```python
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # Call the constructor of the parent class
        self.age = age

    def display(self):
        super().display()       # Call the display method of the parent class using super keyword
        Parent.display(self)    # Call the display method of the parent class using class name
        print(f"Child age: {self.age}")

# Example usage
parent = Parent("John")
parent.display()    # output:- Parent name: John

child = Child("Alice", 10)
child.display() # output:- Parent name: Alice, Parent name: Alice, Child age: 10
```

#### super() with Multiple Inheritance
```python
class Parent:
    def __init__(self):
        print("This is the parent class")
        
class Parent1:
    def __init__(self):
        print("This is the parent1 class")
        
class Child(Parent1, Parent):
    def __init__(self):
        ##Calling constructor of the Parnet 1 class
       super().__init__()
    
ob = Child() # output:- This is the parent1 class


# if we have inherit class parent and parent1
class Child(Parent, Parent1):
    def __init__(self):
        ##Calling constructor of the Parnet 1 class
       super().__init__()
    
ob = Child() # output:- This is the parent class
```