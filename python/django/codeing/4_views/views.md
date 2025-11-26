### Multipal views
- Step 1: Create the Views Folder Structure
```python
myapp/
    views/
        __init__.py
        home_view.py
        test_view.py
        user_view.py
        auth_view.py
    urls.py
```

#### Include files in init.py file
- __init__.py is required — otherwise Django cannot import your views folder.
- Export functions
```python
from .home import view_home
from .auth_view import login_view, signup_view
from .product import product_list
```

#### Import them in urls.py
```python
from my_app.views import view_home, login_view, signup_view, product_list

urlpatterns = [
    path('', view_home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('products/', product_list, name='products'),
]
```
- 2 Option
```python
# from car_app.views import view_home, product_views, customer_views
from car_app.views import view_home
# from car_app.views.view_home import home

path("", view_home.home, name="home"),
# path('', home, name='home'),
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

### Your Case: Multiple view files inside a views/ folder
```python
myapp/
    views/
        __init__.py
        auth_views.py
        product_views.py
        customer_views.py
    models.py
    urls.py
```
#### 
- ✔ Option 1: Import each file separately
```python
# init.py file
from myapp.views import auth_views, product_views, customer_views

# urls.py
urlpatterns = [
    path("login/", auth_views.login_view, name="login"),
    path("product/", product_views.product_list, name="product"),
    path("customer/", customer_views.customer_view, name="customer"),
]
```
- Option 2: Import specific functions
```python
# urls.py
from myapp.views.auth_views import login_view
from myapp.views.product_views import product_list


```

