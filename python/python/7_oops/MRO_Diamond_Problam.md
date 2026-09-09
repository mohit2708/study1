### **Ques. What is MRO(Method Resolution Order) / Diamond Problam?**
* MRO is a concept used in **inheritance**.
* MRO stands for Method Resolution Order. MRO defines the order of the inherited methods in the child class.
* In Python, the MRO is from **bottom to top** and **left to right**. This means that, first, the method is searched in the class of the object. If it’s not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.
* sable pahle child class ke function ko call karege agar child class mai wo function nahi hai to uske uper wali class mai call karge agar usme bhi nahi hai to uske uper wali class mai call karega asa hi same process chalega.

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

### Diamond Problem?
* The Diamond Problem occurs in multiple inheritance when a child class inherits from two classes that have the same parent class. It creates ambiguity about which parent method should be called. Python solves this using MRO (Method Resolution Order) and the C3 linearization algorithm.
* जब एक class दो parent classes से inherit करती है, और दोनों parent classes एक ही common parent class से inherit करती हैं, तो inheritance structure diamond जैसा बन जाता है।
```python
        A
       / \
      B   C
       \ /
        D
```

#### Example of Diamond Problem
```python
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


obj = D()
obj.show()


# Explain
1. D में show() है?
❌ नहीं → B में जाओ

2. B में show() है?
❌ नहीं → pass का मतलब है B ने कोई नया show() नहीं बनाया → C में जाओ

3. C में show() है?
❌ नहीं → A में जाओ

4. A में show() है?
✅ हाँ!
```