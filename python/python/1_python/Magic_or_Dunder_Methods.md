### **Ques. What is Magic Method Or Dunder Methods?**
* Python Magic methods are the methods starting and ending with double underscores ‘__’. They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.
* Python में Magic Methods को ही आमतौर पर Dunder Methods या Special Methods कहा जाता है। ये methods ऐसे predefined method names हैं जिनके आगे और पीछे double underscore (__) होता है, जैसे __init__, __str__, __len__, __add__ आदि। Python इन्हें कुछ operations पर implicitly यानी automatically call करता है।
* The dir() function can be used to see the number of magic methods inherited by a class.
```python
print(dir(int))
```
#### Complete Important Magic Methods Table
| Category             | Method               | Example         |
| -------------------- | -------------------- | --------------- |
| Creation             | `__new__()`          | object creation |
| Initialization       | `__init__()`         | `Student()`     |
| String               | `__str__()`          | `str(obj)`      |
| Representation       | `__repr__()`         | `repr(obj)`     |
| Length               | `__len__()`          | `len(obj)`      |
| Addition             | `__add__()`          | `a + b`         |
| Subtraction          | `__sub__()`          | `a - b`         |
| Multiplication       | `__mul__()`          | `a * b`         |
| Division             | `__truediv__()`      | `a / b`         |
| Floor division       | `__floordiv__()`     | `a // b`        |
| Modulus              | `__mod__()`          | `a % b`         |
| Power                | `__pow__()`          | `a ** b`        |
| Equality             | `__eq__()`           | `a == b`        |
| Not equal            | `__ne__()`           | `a != b`        |
| Less than            | `__lt__()`           | `a < b`         |
| Greater than         | `__gt__()`           | `a > b`         |
| Indexing             | `__getitem__()`      | `obj[0]`        |
| Assignment           | `__setitem__()`      | `obj[0] = x`    |
| Delete item          | `__delitem__()`      | `del obj[0]`    |
| Membership           | `__contains__()`     | `x in obj`      |
| Iteration            | `__iter__()`         | `for x in obj`  |
| Next                 | `__next__()`         | `next(obj)`     |
| Callable             | `__call__()`         | `obj()`         |
| Boolean              | `__bool__()`         | `if obj`        |
| Context manager      | `__enter__()`        | `with obj`      |
| Context manager      | `__exit__()`         | `with obj`      |
| Attribute access     | `__getattribute__()` | `obj.name`      |
| Missing attribute    | `__getattr__()`      | `obj.xyz`       |
| Attribute assignment | `__setattr__()`      | `obj.x = 10`    |
| Attribute deletion   | `__delattr__()`      | `del obj.x`     |
| Destructor           | `__del__()`          | object cleanup  |

```python
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

| Special Method | Description                 |
| -------------- | --------------------------- |
| __len__()      | Supports the len() function |

```python
class emp():
    def __init__(self,name,salery):
        self.name = name
        self.salery = salery
        
    def __len__(self):            # Magic method
        return len(self.name)
        
obj = emp('mohit', 422573)
print(obj.__len__())    # Output:- 5
print(len(obj))         # Output:- 5
```

#### Important Magic Methods
1. __new__() :- यह object को create करने के लिए responsible होता है।
```python
class Student:

    def __new__(cls):
        print("Object created")
        return super().__new__(cls)

    def __init__(self):
        print("Object initialized")


s = Student()

# Output:-
Object created
Object initialized
```

2. __init__() :- Object initialization के लिए।
```python
class Student:

    def __init__(self, name):
        self.name = name

s = Student("Mohit")
print(s.name)   # Output:- Mohit
```

##### Notes:- 
* __new__()  → object create करता है
* __init__() → created object को initialize करता है

3. __str__() :- यह object की user-friendly string representation देता है।
* Without __str__():
```python
class Student:

    def __init__(self, name):
        self.name = name


s = Student("Mohit")   

print(s) # Output:- <__main__.Student object at 0x...>
```
* With __str__():
```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Mohit")

print(s)    # Output:- Mohit
```

4. __repr__() :- __repr__() object की developer-friendly / unambiguous representation के लिए होता है।
```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age})"

s = Student("Mohit", 25)

print(repr(s))  # Output:- Student(name='Mohit', age=25)
```

#### __str__() vs __repr__()
| `__str__()`                  | `__repr__()`                        |
| ---------------------------- | ----------------------------------- |
| User-friendly                | Developer-friendly                  |
| `str(obj)`                   | `repr(obj)`                         |
| `print(obj)` में commonly used | Debugging/developer representation  |
| Readability पर focus         | Unambiguous representation पर focus |

#### Arithmetic Magic Methods
* ये operator overloading के लिए बहुत important हैं।
1. __add__()    -> a+b
2. __sub__()    a-b
3. __mul__()    a*b
4. __truediv__()    /
5. __floordiv__()   //
6. __mod__() % 
7. __pow__() **
* इन special methods के जरिए custom objects arithmetic operators को support कर सकते हैं।

