### **Ques. What do * (single asterisk) and ** (double asterisk)?**
### **Ques. What do * args and ** kwargs?**

#### Single Asterisk
#### *args (Non-Keyword Arguments)
* *args allows you to pass a variable number of non-keyword arguments to a function.
* args is treated as a **tuple** containing all the extra arguments that were passed.
* If we do not know how many arguments will be passed to your function, add a * before the parameter name in the function definition. This way the function will receive a **tuple** of arguments, and can access the items accordingly.

```python
# Example 1
def print_colors(*args):
    print(args)
print_colors('red','blue','green','yellow')

Output:- ('red', 'blue', 'green', 'yellow')

# Example 2
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

Output:-
Hello
Welcome
to
GeeksforGeeks

# Example 3
def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)


fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

Output:-
First argument : Hello
Argument *argv : Welcome
Argument *argv : to
Argument *argv : GeeksforGeeks
```
<div style="page-break-before: always;"></div>

#### **kwargs(Keyword Arguments)
* kwargs allows you to pass a variable number of keyword arguments (arguments that have a **key-value pair**) to a function.
* kwargs is treated as a **dictionary** containing all the extra keyword arguments that were passed.
* If you do not know how many keyword arguments that will be passed to your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly.

```python
# Example 1
def print_numbers(**kwargs):
  for key, value in kwargs.items():
      print (f"{key} is a {value}")
print_numbers(mohit="TL", two="two",three=3,four="four")

Output:-
mohit is a TL
two is a two
three is a 3
four is a four

# Example 2
def fun(arg1, **kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun("Hi", s1='Geeks', s2='for', s3='Geeks')

Output:-
s1 == Geeks
s2 == for
s3 == Geeks
```

#### Using both *args and **kwargs
```python
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)
Output:-
Positional arguments: (1, 2, 3)
Keyword arguments: {'a': 4, 'b': 5}
```