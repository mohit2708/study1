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

#### Ques. How do you remove a file from a folder in python?
????p


#### Ques. Program to Delete all files with a specific extension?
```python
import os 
from os import listdir
my_path = 'C:\Python Pool\Test\'
for file_name in listdir(my_path):
    if file_name.endswith('.txt'):
        os.remove(my_path + file_name)
```

### What is the Python “with” statement designed for?



### Creates a file
```python
# Using open() with Write Mode ('w'):- This method creates a new file or truncates an existing file.
with open('example.txt', 'w') as file:
    file.write("This is a new file created in write mode.")

# Using open() with Append Mode ('a'):- This method creates a new file if it doesn't exist and appends content to it if it does.
with open('example.txt', 'a') as file:
    file.write("\nThis line is added to the existing file.")

# Using open() with Exclusive Creation Mode ('x')
try:
    with open('example.txt', 'x') as file:
        file.write("This file is created using exclusive mode.")
except FileExistsError:
    print("File already exists.")
```

### Read files
```python
# using read() method
f = open("example.txt", "r")
print(f.read())
f.close()


# Using the with statement
with open("demofile.txt") as f:
  print(f.read())

# using loop
with open("demofile.txt") as f:
  for x in f:
    print(x)


# Return the 5 first characters of the file:
with open("demofile.txt") as f:
  print(f.read(5))


# Using open() with Read Mode ('r')
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Read Lines
# You can return one line by using the readline() method:
with open("example.txt") as f:
  print(f.readline())

# By calling readline() two times, you can read the two first lines:
with open("example.txt") as f:
  print(f.readline())
  print(f.readline())

# Reading Line by Line:- You can read a file line by line using a loop.
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Use strip() to remove newline characters


# Using readline():- The readline() method reads one line at a time. You can call it multiple times to read subsequent lines.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

```

### write a file
```python
# Using open() with Write Mode ('w'):- This method creates a new file or truncates an existing file.
with open('example.txt', 'w') as file:
    file.write("This is a new file created in write mode.")

# Using open() with Append Mode ('a'):- This method creates a new file if it doesn't exist and appends content to it if it does.
with open('example.txt', 'a') as file:
    file.write("\nThis line is added to the existing file.")

# Using open() with Exclusive Creation Mode ('x')
try:
    with open('example.txt', 'x') as file:
        file.write("This file is created using exclusive mode.")
except FileExistsError:
    print("File already exists.")

# Writing Multiple Lines:- You can write multiple lines to a file using the writelines() method. 
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

### Delete file
```python
# os.remove() function
import os

file_name = 'example.txt'
try:
    os.remove(file_name)
    print(f"{file_name} has been deleted.")
except FileNotFoundError:
    print(f"{file_name} does not exist.")
except PermissionError:
    print(f"Permission denied to delete {file_name}.")


# Using os.unlink()
import os

file_name = 'example.txt'
try:
    os.unlink(file_name)
    print(f"{file_name} has been deleted.")
except FileNotFoundError:
    print(f"{file_name} does not exist.")
except PermissionError:
    print(f"Permission denied to delete {file_name}.")

# Using os.rmdir() for Directories:- If you need to delete an empty directory, you can use os.rmdir(). 
# Note that this will only work if the directory is empty.
import os

directory_name = 'empty_directory'
try:
    os.rmdir(directory_name)
    print(f"{directory_name} has been deleted.")
except FileNotFoundError:
    print(f"{directory_name} does not exist.")
except OSError:
    print(f"{directory_name} is not empty or cannot be removed.")

# Using shutil.rmtree() for Non-Empty Directories
# If you want to delete a directory and all its contents (files and subdirectories), you can use the shutil module.
# to delete non-empty directories.
import shutil

directory_name = 'non_empty_directory'
try:
    shutil.rmtree(directory_name)
    print(f"{directory_name} and all its contents have been deleted.")
except FileNotFoundError:
    print(f"{directory_name} does not exist.")
except PermissionError:
    print(f"Permission denied to delete {directory_name}.")
```

