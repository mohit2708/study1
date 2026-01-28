### **Ques. What is Method Overloading?**
* Two or more methods have the same name but different numbers of parameters, These methods are called overloaded methods.
* Python does not directly support method overloading
```python
class Addition:
	# first sum for 2 params
	def my_sum(self, a, b):
		return a + b
	
	# second overloaded sum for 3 params
	def my_sum(self, a, b, c):
		return a + b + c

obj = Addition()
# print(obj.my_sum(3, 4)) # missing 1 required positional argument:
print(obj.my_sum(3, 4, 5))  # Output: 12
```

- **Since Python does not support traditional method overloading, we can use workarounds to achieve similar behavior:**
1. **Optional Arguments:-** We can define a single method with optional arguments using default values.
```python
def greet(name = None, age = None):
    if name and age:
        print(f"Hello, {name}! You are {age} years old.")
    elif name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

# Example usage:
greet()  # Output: Hello!
greet("John")  # Output: Hello, John!
greet("Jane", 30)  # Output: Hello, Jane! You are 30 years old.
```
2. **Variable Argument Lists:-** We can use variable argument lists (*args and **kwargs) to define a single method that accepts any number of arguments.
```python
def greet(*args):
    if len(args) == 1:
        print(f"Hello, {args[0]}!")
    elif len(args) == 2:
        name, age = args
        print(f"Hello, {name}! You are {age} years old.")
    else:
        print("Invalid number of arguments!")

# Example usage:
greet("John")  # Output: Hello, John!
greet("Jane", 30)  # Output: Hello, Jane! You are 30 years old.
```

3. Using the @singledispatch Decorator:-
- Python's **functools** module provides a decorator called **@singledispatch** that allows us to define multiple functions with the same name but different argument types.
```python
from functools import singledispatch

@singledispatch
def greet(arg):
    print("Invalid argument type!")

@greet.register(str)
def _(name: str):
    print(f"Hello, {name}!")

@greet.register(int)
def _(age: int):
    print(f"You are {age} years old!")

# Example usage:
greet("John")  # Output: Hello, John!
greet(30)  # Output: You are 30 years old!
```

### **Ques. What is Method Overriding?**
* When a child class method has the **same name**, **same parameters**, and **same return type as a method**.
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

#### Why Method Overriding?
- Method overriding is useful when we want to:
  - **Customize behavior:** Override methods to provide custom behavior for a specific subclass.
  - **Extend functionality:** Add new functionality to an existing method without modifying the original implementation.
  - **Improve performance:** Optimize method implementations for specific use cases.

- Example
```python
# Superclass (Parent class)
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print(f"Calculating area of {self.name}...")
        return 0

# Subclass (Derived class) - Circle
class Circle(Shape):
    def __init__(self, radius, name="Circle"):
        super().__init__(name)
        self.radius = radius

    def area(self):  # Overriding the area method
        return 3.14159 * (self.radius ** 2)

# Subclass (Derived class) - Rectangle
class Rectangle(Shape):
    def __init__(self, width, height, name="Rectangle"):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):  # Overriding the area method
        return self.width * self.height

# Create objects and calculate areas
circle = Circle(5)
print(f"Circle area: {circle.area()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")
```



### Extra
### Operator Overloading
- Operator overloading is a feature of object-oriented programming (OOP) that allows developers to redefine the behavior of operators when working with custom-defined classes or objects.
- In Python, operators such as +, -, *, /, etc., are defined for built-in data types like numbers and strings. However, when you create a custom class, these operators may not work as expected, because they do not know how to handle your custom object.
- Operator overloading allows you to redefine the behavior of these operators so that they can be used with your custom objects in a meaningful way.

#### Why Operator Overloading?
- Operator overloading is useful when:
  - **Improving Readability:** It makes your code more readable by allowing you to use familiar operators instead of calling specific methods.
  - **Simplifying Complex Operations:** By redefining operators, you can simplify complex operations and make them more intuitive.
  - 
#### Example of Operator Overloading in Python
- Let's create a Vector class that represents a vector with x and y coordinates. We will overload the + operator to add two vectors together:

```python

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Create vectors and add them using the overloaded + operator
v1 = Vector(2, 3)
v2 = Vector(4, 5)

result = v1 + v2
print(result)  # Output: Vector(6, 8)
```
```python
In this example:

The Vector class represents a vector with x and y coordinates.
We overload the + operator using the __add__ method.
When we add two vectors together using v1 + v2, the __add__ method gets called, returning a new Vector object with the summed coordinates.
Common Operator Overloading Methods
Here are some common methods used for operator overloading in Python:

Method	Operator
__add__	+
__sub__	-
__mul__	*
__truediv__	/
__floordiv__	//
__eq__	==
__ne__	!=
__lt__	<
__le__	<=
__gt__	>
__ge__	>=
Best Practices
Be consistent: Consistently overload operators across your classes to ensure predictable behavior.
Document operator overloading: Clearly document which operators are overloaded and how they behave in your class documentation.
Conclusion
Operator overloading is a powerful feature of Python's OOP that allows you to redefine the behavior of operators for custom-defined classes or objects, making your code more readable, intuitive, and efficient.

This model doesn't return token count.
U
User
what is Function Overloading:

AI
llama3.3:latest
Function Overloading in Python
Function overloading is a technique where multiple functions with the same name can be defined but with different parameter lists. This allows for more flexibility when calling functions.

What is Function Overloading?
In function overloading, we define multiple functions with the same name but different parameters. The correct function to call is determined based on the number and types of arguments passed.

Why Function Overloading?
Function overloading is useful when:

Improving Code Readability: It allows you to write more readable code by providing a single interface for multiple related operations.
Reducing Function Names: By using the same function name, we can avoid having multiple function names that are similar but differ only in their parameters.
Example of Function Overloading (using @singledispatch decorator)
Python does not directly support function overloading like some other programming languages, such as C++ or Java. However, you can use the @singledispatch decorator from the functools module to achieve similar behavior:

<>
python


from functools import singledispatch

@singledispatch
def fun(arg):
    print("Invalid argument type!")

@fun.register(int)
def _(arg: int):
    print(f"Integer value: {arg}")

@fun.register(str)
def _(arg: str):
    print(f"String value: {arg}")

# Call the function with different types of arguments
fun(10)  # Output: Integer value: 10
fun("Hello")  # Output: String value: Hello
In this example:

The @singledispatch decorator is used to define a single-dispatch generic function.
The @fun.register decorator is used to register different implementations of the function based on argument types.
Using Default Argument Values for Function Overloading
Another way to achieve function overloading-like behavior in Python is by using default argument values:

<>
python


def greet(name = "World", age = None):
    if name and not age:
        print(f"Hello, {name}!")
    elif name and age:
        print(f"Hello, {name}! You are {age} years old.")
    else:
        print("Invalid arguments!")

# Call the function with different combinations of arguments
greet()  # Output: Hello, World!
greet("John")  # Output: Hello, John!
greet("Jane", 30)  # Output: Hello, Jane! You are 30 years old.
In this example:

The greet function has default argument values for name and age.
The behavior of the function changes based on the presence or absence of these arguments.
Using Variable Argument Lists (*args and **kwargs) for Function Overloading
You can also use variable argument lists to achieve function overloading-like behavior:

<>
python


def greet(*args):
    if len(args) == 1:
        print(f"Hello, {args[0]}!")
    elif len(args) == 2:
        name, age = args
        print(f"Hello, {name}! You are {age} years old.")
    else:
        print("Invalid number of arguments!")

# Call the function with different numbers of arguments
greet("John")  # Output: Hello, John!
greet("Jane", 30)  # Output: Hello, Jane! You are 30 years old.
In this example:

The greet function uses a variable argument list (*args) to accept any number of arguments.
The behavior of the function changes based on the number and values of these arguments.
Conclusion
While Python does not directly support function overloading like some other programming languages, you can achieve similar behavior using techniques such as:

@singledispatch decorator from functools
Default argument values
Variable argument lists (*args and **kwargs)
By understanding these techniques, you can write more flexible and readable code that handles different scenarios in a single function interface.
```