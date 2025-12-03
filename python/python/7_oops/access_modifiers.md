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