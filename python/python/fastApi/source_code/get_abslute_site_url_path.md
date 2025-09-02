### Get absolute Path
```python
@router.get("/get_site_url")
def get_site_url(request: Request = None):
    current_url = request.url
    print("request url ",current_url.scheme + '://' + current_url.hostname)
    return JSONResponse(
        content={
            "success": True,
            "code": 200,
            "message": "Current URL retrieved successfully",
            "data": {
                "url": str(current_url),
                "scheme": current_url.scheme,
                "hostname": current_url.hostname,
                "port": current_url.port,
                "path": current_url.path,
                "query": current_url.query
            }
        },
        status_code=200
    )
```

### Get Site Path
```python
@router.get("/get_absolute_path")
def get_absolute_path():

    # Use os.getcwd() to get the current working directory.
    # Use os.path.abspath() to get the absolute path of a file or directory.
    # Use Path.cwd() to get the current working directory as a Path object.
    # Use Path.resolve() to get the absolute path of a file or directory as a Path object.

    # Get the current working directory
    current_working_directory = Path.cwd()
    
    # Get the absolute path of a specific file or directory
    absolute_path = Path("uploads/image/profile_image").resolve()


    
    return JSONResponse(
        content={
            "success": True,
            "code": 200,
            "message": "Absolute path retrieved successfully",
            "data": {
                "current_working_directory": str(current_working_directory),
                "absolute_path": str(absolute_path)
            }
        },
        status_code=200
    )
```