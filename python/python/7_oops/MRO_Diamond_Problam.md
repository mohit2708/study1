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