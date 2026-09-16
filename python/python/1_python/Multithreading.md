### **What is Multithreading?**
* Multithreading is a programming technique that **allows multiple threads to run concurrently within a single process**.
* In Python, multithreading enables a program to **perform multiple tasks at the same time.**
* Python provides the **threading** module to implement multithreading.

#### Benefits of Multithreading
* Improves application responsiveness.
* Makes better use of waiting time during I/O operations (file handling, database calls, API requests, etc.).
* Allows multiple tasks to execute concurrently.
* Enhances overall application performance for I/O-bound tasks.

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

### How does Python achieve Multithreading?
* Python achieves multithreading using the **threading** module, which allows multiple threads to be created and managed within a single process.
* Python achieves multithreading using the **threading** module. Although the Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time, multithreading is still effective for I/O-bound tasks because threads can run while others are waiting for I/O operations.
```python
import threading
import time

def task(name):
    print(f"{name} started")
    time.sleep(3)   # Simulating I/O operation
    print(f"{name} completed")

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()
```


### How does Python achieve multithreading despite the GIL (Global Interpreter Lock)?
* Python supports multithreading using the **threading module**, but due to the **GIL**, only one thread can execute Python bytecode at a time. **Therefore, multithreading is most effective for I/O-bound tasks (API calls, file operations, database queries), while multiprocessing is preferred for CPU-bound tasks.**


### **multithreading vs multiprocessing?**
* Dono ka purpose multiple tasks ko concurrently/parallelly execute karna hai, lekin dono ka working different hai.
* **Multithreading** is mainly suitable for **I/O-bound tasks**, while **multiprocessing** is suitable for **CPU-bound tasks**.
  * **Reason:** Python ka GIL (Global Interpreter Lock) ek process ke andar ek time par ek thread ko Python bytecode execute karne deta hai. Multiprocessing mein separate processes hote hain, isliye CPU cores ka true parallel use possible hota hai.

| Feature         | Multithreading               | Multiprocessing                          |
| --------------- | ---------------------------- | ---------------------------------------- |
| Unit            | Thread                       | Process                                  |
| Memory          | Same memory share karte hain | Separate memory hoti hai                 |
| GIL             | GIL ke under                 | Har process ka apna GIL                  |
| Best for        | **I/O-bound tasks**          | **CPU-bound tasks**                      |
| CPU parallelism | Python code ke liye limited  | **True parallelism**                     |
| Overhead        | Low                          | Higher                                   |
| Communication   | Easy, shared memory          | IPC required                             |
| Example         | API/DB/File operations       | ML, image processing, heavy calculations |
| Python module   | `threading`                  | `multiprocessing`                        |


#### Example of Multithreading
```python
import threading

t1 = threading.Thread(target=download_file)
t2 = threading.Thread(target=call_api)

t1.start()
t2.start()

# Yahaan tasks mostly waiting kar rahe hain → I/O-bound → multithreading useful.
```

#### Example of Multiprocessing
```python
from multiprocessing import Process

p1 = Process(target=heavy_calculation)
p2 = Process(target=heavy_calculation)

p1.start()
p2.start()

# Yahaan dono processes CPU par actual computation kar sakte hain → CPU-bound → multiprocessing useful.
```


### **What is I/O-bound Tasks?**
* I/O = Input / Output
* Jab program ka zyada time CPU calculation me nahi, balki kisi external resource ka response wait karne me lagta hai, use I/O-bound task kehte hain.

#### Examples of I/O-bound Tasks
* **Database Query**:- Database se data aane tak thread wait karta hai.
```python
users = db.execute("SELECT * FROM users")
```

* **API Call** :- Server response aane tak wait karta hai.
```python
response = requests.get("https://api.example.com/users")
```

* **File Read/Write**:- Disk se file read hone tak wait karta hai.
```python
with open("data.txt") as f:
    data = f.read()
```

* **Network Request**:- Network se data aane tak wait karta hai.
```python
socket.recv()
```

### **What is CPU-bound Tasks?**
* Jab program ka zyada time calculations karne me lagta hai.
* Examples:
  * Large mathematical calculations
  * Image processing
  * Video encoding
  * Machine Learning training
  * Data analysis on huge datasets
```python
for i in range(100000000):
    result += i
```

### I/O-bound vs CPU-bound
| Task Type | Time kis me lagta hai?           | Best Option            |
| --------- | -------------------------------- | ---------------------- |
| I/O-bound | Waiting (DB, API, File, Network) | Multithreading / Async |
| CPU-bound | Computation (calculations)       | Multiprocessing        |


