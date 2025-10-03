### **What is with?**
* The with statement in Python is used to wrap the execution of a block of code within methods defined by a context manager. It’s primarily designed to simplify resource management and ensure that setup and cleanup code runs reliably, even if errors occur.

#### **What does with do?**
* It calls the context manager’s __enter__() method before the block starts.
* It executes the block of code inside the with.
* When the block finishes (whether normally or due to an exception), it calls the context manager’s __exit__() method to clean up.

### Why use with?
* **Automatic resource management:** e.g., files, network connections, locks.
* **Cleaner code:** Avoids explicitly writing try-finally blocks for cleanup.
* **Safer:** Ensures resources are properly released even if an error happens.

#### Example:-
```python
f = open('file.txt', 'r')
try:
    data = f.read()
finally:
    f.close()

# Same with with (simpler and safer):
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed here
```
#### Summary:
* with makes working with resources easier and safer by ensuring that setup and cleanup happen properly, without you needing to write explicit cleanup code every time.

#### using with statement?
* The method shown in the above section is not entirely safe. If some exception occurs while opening the file, then the code will exit without closing the file.
```python
# Opening file in read mode and printing the contents of the file.
with open("test.txt", mode='r') as f:
    data = f.readlines() #This reads all the lines from the file in a list.
    print(data) #This will print the content of the Hello World file!

# Opening a file in write mode.
with open("test.txt", mode='w') as f:
    f.write("Data after write operation")
# Opening file in read mode to check the contents.
with open("test.txt", mode='r') as f:
    data = f.readlines() # this reads all the lines from the file in a list.
    print(data) #this will print the overwritten content of the file that is       "Data after write operation"

# Opening a file in append mode and appending data to the file.
with open("test.txt", "a") as f:
    f.write(" Appending new data to the file")
# Opening file in read mode to check the contents.
with open("test.txt", mode='r') as f:
    data = f.readlines() #This reads all the lines from the file in a list.
    print(data) #this will print the existing content of file plus the appended content
```