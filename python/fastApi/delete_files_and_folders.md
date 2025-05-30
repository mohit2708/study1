### How to delete files and folders in Python?
* Refrence:- https://www.python-engineer.com/posts/delete-files-python/
* Deletion of files:-
```python
import os
os.remove("/home/user/Documents/notes.txt")
```
* pathlib.Path.unlink(missing_ok=False)
```python
import pathlib

path = pathlib.Path("/home/user/Desktop/sample_pdf.pdf")
path.unlink()
```
* Deletion of folders
```python
import os
os.rmdir("/home/user/Desktop/Images")
```
* pathlib.Path.rmdir()
```python
import pathlib

path = pathlib.Path("/home/user/Desktop/Images") # create a path object first, rmdir() does not take any arguments
path.rmdir()
```
* shutil.rmtree(directory_path)
```python
import shutil
shutil.rmdir("/home/user/Desktop/Images")
```