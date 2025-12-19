### Multipal views
- Step 1: Create the Views Folder Structure
```python
myapp/
    views/
        __init__.py
        home_view.py
        test_view.py
        user_view.py
    urls.py
```
- ⚠️ __init__.py is required — otherwise Django cannot import your views folder.
- Step 2: Create Your View Files
- Example: home_view.py
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home view")

```
- Example: test_view.py
```python
from django.http import HttpResponse

def test(request):
    return HttpResponse("This is test view")
```

- Step 3: Import These Views in urls.py
```python
from django.urls import path
from .views import home_view, test_view

urlpatterns = [
    path('', home_view.home, name='home'),
    path('test/', test_view.test, name='test'),
]

```

- Group views inside views/init.py
```python
# views/__init__.py
from .home_view import home
from .test_view import test
```
- After this → you can delete views.py.
