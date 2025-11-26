### **In view.py file**
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('first page')
```


### **View calling using template**
- your project -> setting.py
```python
'DIRS': ['templates'],
```

```python
=======create templates folder in root directiry where is managed file=====
=======and create file index.html ================
<h1>Hello</h1>
<h1>Hello {{name}}</h1>


=====views.py=======
from django.shortcuts import render
from django.http import HttpResponse
def individual_post(request):
    return render(request, 'index.html')
    return render(request,"signup.html", {'name':'mohit'})
```


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




### Organize your views into multiple files within a single folder
```python
Create a "views" folder in your app
```
```python
Create multiple view files: like "views1.py" and "views2.py"

# in view1.py file

from django.http import HttpResponse

def view1(request):
    return HttpResponse("This is View 1")

def view2(request):
    return HttpResponse("This is View 2")

# in view2.py file
from django.http import HttpResponse

def view3(request):
    return HttpResponse("This is View 3")

def view4(request):
    return HttpResponse("This is View 4")
```
```python
call in urls.py

from django.urls import path
from .views import views1, views2

urlpatterns = [
    path('view1/', views1.view1, name='view1'),
    path('view2/', views1.view2, name='view2'),
    path('view3/', views2.view3, name='view3'),
    path('view4/', views2.view4, name='view4'),
]
```