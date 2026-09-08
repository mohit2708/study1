### 🎯**Dajngo project setup**
#### Virtual Environment
* [More](../../virtual_env.md)
```python
# Create virtual env
python -m venv venv

# activate
venv\Scripts\activate
```

2. Django install karo
```python
pip install django

# check version
django-admin --version
```

#### Django project create karo
```python
django-admin startproject myproject

myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

4. Server run karo
```python
python manage.py runserver  # http://127.0.0.1:8000/

# Django ka default page open ho jayega.
```
<div style="page-break-before: always;"></div>

5. App create karo
```python
python manage.py startapp users

myproject/
│
├── manage.py
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── users/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

6. App ko settings.py mein add karo
* myproject/settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',    # add app
]
```

7. First View banao
* users/views.py
```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Django")
```

8. URL seeting
* App ke andar urls.py banao:- users/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

* Project ke urls.py mein include karo
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
```

9. Database migrations
```python
python manage.py migrate
```

10. Admin user banao
```python
python manage.py createsuperuser

# http://127.0.0.1:8000/admin/
```


