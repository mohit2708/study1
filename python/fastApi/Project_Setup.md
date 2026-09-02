|  No.  | Project Setup                                                             |
| :---: | ------------------------------------------------------------------------- |
|       | [virtual environment:- Create](#create-virtual-environment)               |
|       | [virtual environment:- Activate](#activated-virtual-environment)          |
|       | [Install Fastapi](#install-fastapi)                                       |
|       | [upgratde Pip version](#upgratde-pip-version)                             |
|       | [Install Uvicorn](#install-uvicorn)                                       |
|       | [Create main.py file with route](#create-a-mainpy-file-with-routes)       |
|       | [Run the server](#run-the-server)                                         |
|       | [Project setup one pc to another Pc](#project-setup-one-pc-to-another-pc) |
<div style="page-break-before: always;"></div>

# Project Setup
### 🎯**Create virtual environment**
* create the folder and open the cmd
```python
python -m venv virtual-name
OR
pip install virtualenv  # Install the package.
virtualenv MyFirstApp
MyFirstApp\scripts\activate
```

#### Activated virtual environment
```pyhton
cd virtual-name\Scripts
d:\mohit\virtual-name\Scripts> activate
(OR)
source env_crud/Scripts/activate
```

#### For activate
| Terminal   | Command                            |
| ---------- | ---------------------------------- |
| PowerShell | `.\virt_env\Scripts\Activate.ps1`  |
| CMD        | `virt_env\Scripts\activate.bat`    |
| Git Bash   | `source virt_env/Scripts/activate` |


### 🎯**Install Fastapi**
* we have install two packages/library **fastapi** and **uvicorn**
```python
pip install fastapi
OR
pip install "fastapi[standard]"
```

### 🎯**upgratde Pip version**
```python
python.exe -m pip install --upgrade pip
```
<div style="page-break-before: always;"></div>

### 🎯**Install Uvicorn**
* FastAPI doesn’t come with any built-in server application. To run FastAPI app, you need an ASGI server called uvicorn, so install the same too, using pip installer. 
```python
# You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
pip install "uvicorn[standard]"
```

#### Uvicorn version
```python
uvicorn --version
```

#### Upgrade Uvicorn
```python
pip install --upgrade uvicorn fastapi
```

#### Uninstall Uvicorn
```python
pip uninstall uvicorn fastapi
```
<div style="page-break-before: always;"></div>

### 🎯**Create a main.py file with routes**
- firstaly active the virtual env
- Create main.py file in folder 


#### Basic Request
```python
from fastapi import FastAPI

app = FastAPI()

# Handles GET requests
@app.get("/")
def first_page_function():
    return {"msg":"Hello FastAPI🚀"}

# Handles POST requests
@app.post("/post_route")
def post_function():
    return {"msg":"calling post routes🚀"}

# Handles PUT requests
@app.put("/put_route")
def put_function():
    return {"msg":"calling put routes🚀"}

# Handles PATCH requests
@app.patch("/patch_route")
def patch_function():
    return {"msg":"calling patch routes🚀"}

# Handles DELETE requests
@app.delete("/delete_route")
def delete_function():
    return {"msg":"calling delete routes🚀"}

# Handles HEAD requests
@app.head("/items/{item_id}")
def head_item(item_id: int):
    # This will return the headers without a body
    pass
```
<div style="page-break-before: always;"></div>

#### We can use summary, description and tag
```python
@app.get("/", summary="Path parameters", description="Path parameters api", tags=["Path parameters"])
def first_page_function():
    return {"msg":"Hello FastAPI🚀"}
```
<div style="page-break-before: always;"></div>


### 🎯**Run the server**
- got to directory where main.py exist
```python
uvicorn main:app --reload

uvicorn main:app --host 127.8.4.8 --port 12   # Difrent port

# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [28720]
# INFO:     Started server process [28722]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
```
```python
Open your browser at http://127.0.0.1:8000/
Open your browser at http://127.0.0.1:8000/items
```

#### Run the server when main.py file in another folder.
```python
uvicorn foldername.main:app --reload
```


#### another way to run server
```python
# create run.py file and call main file
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)

# and run 
python run.py
```
<div style="page-break-before: always;"></div>

### 🎯**Project setup one pc to another Pc**
* First of all we run the command
```python
pip freeze > requirements.txt
```
* And other system follows these step
```python
# Create and activate virtual environment
virtualenv -p python3 env
. ./env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
pip install --default-timeout=100 -r requirements.txt

# Create SQLite databse, run migrations
cd myapp
./manage.py migrate

# Run Django dev server
./manage.py runserver
```