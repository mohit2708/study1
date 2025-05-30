### Url 2nd type of calling views in app file.
```python
from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
```


### **In view.py file**
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('first page')
```

### **View calling using template**
```python
====setting.py=========
 'DIRS': ['templates'],

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








