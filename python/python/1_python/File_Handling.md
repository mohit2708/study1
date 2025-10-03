### **Ques. What is File Handling in Python?**
* Suppose you are working on a file saved on your personal computer. If you want to perform any operation on that file like opening it, updating it or any other operation on that, all that comes under File handling.
* File handling in Python involves interacting with files on your computer to read data from them or write data to them. Python provides several built-in functions and methods for creating, opening, reading, writing, and closing files.
* Types Of File in Python
* Binary file
  * <b>Document files:</b> .pdf, .doc, .xls etc.
  * <b>Image files:</b> .png, .jpg, .gif, .bmp etc.
  * <b>Video files:</b> .mp4, .3gp, .mkv, .avi etc.
  * <b>Audio files:</b> .mp3, .wav, .mka, .aac etc.
  * <b>Database files:</b> .mdb, .accde, .frm, .sqlite etc.
  * <b>Archive files:</b> .zip, .rar, .iso, .7z etc.
  * <b>Executable files:</b> .exe, .dll, .class etc.
* Text file
  * <b>Web standards:</b>  html, XML, CSS, JSON etc.
  * Source code:</b> c, app, js, py, java etc.
  * Documents:</b> txt, tex, RTF etc.
  * Tabular data:</b> csv, tsv etc
  * Configuration:</b> ini, cfg, reg etc
  
| Modes | Description                                                                                                                                                                                                                                |
| :---- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| r     | Opens a file in read-only mode. The pointer of the file is at the beginning of the file. This is also the default mode.                                                                                                                    |
| rb    | Opens a file for reading only in binary format.                                                                                                                                                                                            |
| r+    | Opens the file for reading and writing. The pointer is at the beginning of the file.                                                                                                                                                       |
| rb+   | Opens a file for both reading and writing in binary format.                                                                                                                                                                                |
| w     | Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.                                                                                                         |
| wb    | Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.                                                                                        |
| w+    | Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.                                                                        |
| wb+   | Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.                                                       |
| a     | Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.                                         |
| ab    | Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.                        |
| a+    | Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.                  |
| ab+   | Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing. |
| x     | open for exclusive creation, failing if the file already exists                                                                                                                                                                            |
| +     | open file for updating (reading and writing)                                                                                                                                                                                               |
| b     | Opens the file in binary mode                                                                                                                                                                                                              |
| t     | Opens the file in text mode (default)                                                                                                                                                                                                      |

### Opening a File in Python
* This function takes two arguments. First is the filename along with its complete path, and the other is access mode. This function returns a file object.
* To perform any file operation, the first step is to open the file. Python's built-in open() function is used to open files in various modes, such as reading, writing, and appending. The syntax for opening a file in Python is −
```python
file = open("filename", "mode")
```


```python
#example 1
print("hello")
# file1 = open("C:\Users\mohits4\Desktop\mohit\study\python\python\1_python\code\example.txt", "r")
file1 = open("example.txt", "r")
print(file1.read())

#example 2
print("hello")
# file1 = open("C:\Users\mohits4\Desktop\mohit\study\python\python\1_python\code\example.txt", "r")
file1 = open("example.txt", "a")
file1.write("Now the file has more content!")
file1.close()
file1 = open("example.txt", "r")
print(file1.read())
```


### How to read file in python?
* Open a File on the Server:- The **open()** function returns a file object, which has a **read() method** for reading the content of the file.
```python
file = open("file_name.txt", "r")  # Opens the file in read mode
content = file.read()  # Read the content of the file
print(content)
file.close()  # Close the file when done
```
* By default the read() method returns the whole text, but you can also specify how many characters you want to return.
```python
f = open("demofile.txt", "r")
print(f.read(5))

Output:- Hello
```

* The **readline() function** helps you read a **single** line from the file.
```python
file_obj = open("example.txt", "r", encoding="utf-8")
print(file_obj.readline())
file_obj.close()

Output:-
Hello World
```

* As the name suggests, the **readlines() method** reads **all the lines** in the file and returns them properly separated in a list.
```python
file_obj = open("example.txt", "r", encoding="utf-8")
print(file_obj.readlines())
file_obj.close()

Output:- 
This is a new file.
We have now learnt all read functions.
We are trying a new method 
to loop over files.
```


* **Close Files:-** It is a good practice to always close the file when you are done with it.
```python
file = open("demofile.txt", "r")
print(f.readline())
file.close()
```

#### How to Write a File in Python
* We're creating it using the **w** mode. Once we open the new file, it's obviously empty. We're then going to write content into it.
* Write - will overwrite any existing content and Create a new file if it does not exist.
```python
file_obj = open("writing.txt", "w")
```

* **a** Append - will append to the end of the file
```python
file = open("writing.txt", "a")
file.write("This way, I will preserve the existing contents in the file")
print(file.read())
file.close()
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