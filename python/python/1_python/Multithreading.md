### **Multithreading?**
* In Python Multithreading is a technique that allows a program to run multiple tasks simultaneously.
* Multithreading is a technique in programing that allows multiple threads of execution to run concurrently within a single process.
* In Python, We can use the threading module to implement multithreading.

Benefits:-
* It's a powerful tool that can improve application performance and responsiveness.

### Steps Multithreading in Python
* **Step 1:** Import Module
```python
import threading
```
* **Step 2:** Create a Thread
  *  we create an object of the Thread class. It takes the **‘target’** and **‘args’** as the parameters. The target is the **function** to be executed by the thread whereas the args is the **arguments** to be passed to the target function.
```python
t1 = threading.Thread(target, args)
t2 = threading.Thread(target, args)
```
* **Step 3:** Start a Thread
  * To start a thread, we use the start() method of the Thread class.
```python
t1.start()
t2.start()
```
* **Step 4:** End the thread Execution
  * Once the threads start, the current program (you can think of it like a main thread) also keeps on executing. In order to stop the execution of the current program until a thread is complete, we use the join() method.
```python
t1.join()
t2.join()
```

#### Example:-
```python
# Normal calling
import threading
from time import sleep, perf_counter

def fun1():
    start_time = perf_counter()
    print("start ")
    fun2()
    fun3()
    print("end")
    end_time = perf_counter()
    print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')


def fun2():
    sleep(10)
    print("fun2 completed")
    
def fun3():
    sleep(4)
    print("fun3 completed")
    
    
fun1()

# throwh threading calling
from threading import Thread
from time import sleep, perf_counter

def fun1():
    start_time = perf_counter()
    print("start ")
    t1 = Thread(target=fun2)
    t2 = Thread(target=fun3)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end")
    end_time = perf_counter()
    print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')


def fun2():
    sleep(10)
    print("fun2 completed")
    
def fun3():
    sleep(4)
    print("fun3 completed")
    
    
fun1()
```
```python
import threading

def print_cube(num):
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    print("Square: {}" .format(num * num))

# print_cube(10)

t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()
```