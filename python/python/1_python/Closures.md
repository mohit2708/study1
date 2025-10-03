### **Python Closures**
* Python closure is a nested function that we can define a function from the inside of another function. And this function is called a nested function.
* a closure is a nested function that references one or more variables from its enclosing scope.
* function ke ander ke function ko nested function kahte hai.
```python
def functionA():
   print ("Outer function")
   def functionB():
      print ("Inner function")
   functionB()

functionA()

Output:
Outer function
Inner function
```
```python
def functionA(name):
   print ("Outer function")
   def functionB():
      print ("Inner function")
      print ("Hi {}".format(name))
   functionB()
   
functionA("Python")

Output:-
Outer function
Inner function
Hi Python
```
```python
def greet(name):
    # inner function
    def display_name():
        print("Hi", name)
    
    # call inner function
    display_name()

# call outer function
greet("John")  

# Output: Hi John
```