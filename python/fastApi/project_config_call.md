### Project config call
* Create config->project.py
```python
class Settings:
    PROJECT_NAME:str = "Mohit API's. 🔥"
    PROJECT_VERSION: str = "1.0.0"

settings = Settings()
```
* Call main.py file
```python
from config.project import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
```