### Install Fastapi
* we have install two packages/library **fastapi** and **uvicorn**
```python
pip install fastapi
OR
pip install "fastapi[standard]"
```

### Install Uvicorn
* FastAPI doesn’t come with any built-in server application. To run FastAPI app, you need an ASGI server called uvicorn, so install the same too, using pip installer. 
```python
# You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
pip install "uvicorn[standard]"
```

### Uvicorn version
```python
uvicorn --version
```


### Upgrade Uvicorn
```python
pip install --upgrade uvicorn fastapi
```

### Uninstall Uvicorn
```python
pip uninstall uvicorn fastapi
```

### upgratde Pip version
```python
python.exe -m pip install --upgrade pip
```
