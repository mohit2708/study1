### **What is URL Routing in Django?**
* Django URL routing decides which view should handle a particular URL request.
* URL Routing ka matlab hai URL ko kisi specific View function/class ke saath map karna.
* URL routing in Django is the process of mapping URL patterns to their corresponding views using urls.py.

#### Example
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]

# views.py:
def home(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Page")


# AB
/home/  →  home() view
/about/ →  about() view
```

### What is path() and re_path()?
* **path()** is used for **simple and readable URL patterns** with built-in converters, while **re_path()** is used when we need **complex URL matching using regular expressions**.

#### Example of path()
```python
from django.urls import path

urlpatterns = [
    path('user/<int:id>/', views.user),
]

/user/10/    ✅
/user/25/    ✅
/user/abc/   ❌
```

#### Example of re_path()?
```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^user/(?P<id>[0-9]{1,5})/$', views.user),
]

# means 1 se 5 digits.
```

### How do you pass parameters in URLs?
* In Django, we pass parameters in URLs using path converters such as <int:id> or <str:name>. Django captures the value from the URL and passes it as an argument to the view.

#### Example
```python
from django.urls import path

urlpatterns = [
    path('user/<int:id>/', views.user_detail),  # int only
    path('user/<str:name>/', views.user_detail) # String only
]
```

| Converter | Example        | Accepts                     |
| --------- | -------------- | --------------------------- |
| `int`     | `<int:id>`     | Integer                     |
| `str`     | `<str:name>`   | String                      |
| `slug`    | `<slug:title>` | Letters, numbers, `-`, `_`  |
| `uuid`    | `<uuid:id>`    | UUID                        |
| `path`    | `<path:url>`   | Complete path including `/` |


### **What is URL namespace?**
* URL namespace in Django is used to uniquely identify URL names, especially when multiple applications have URLs with the same name.
* URL namespace ka matlab hai URL names ko unique identify karna, especially jab project mein multiple apps ho aur same name ke URLs exist karte ho.

#### Example
* Maan lo 2 apps hain:
  * accounts/
  * and products/
* Dono mein detail naam ka URL hai.

* accounts/urls.py
```python
app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='detail'),
]
```

* products/urls.py
```python
app_name = 'products'

urlpatterns = [
    path('product/', views.product, name='detail'),
]
```

* Ab template mein:
```python
{% url 'accounts:detail' %}

# → Accounts ka detail URL
{% url 'products:detail' %}
```

### What is include() in Django?
* include() is used to include an app's URL patterns into the project's main URL configuration, helping us organize URLs app-wise.
* include() ka use main project's urls.py se kisi app ke urls.py ko connect/include karne ke liye hota hai.
#### Example
* Project urls.py:
```python
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
]
```

* users/urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]
```

#### Why use include()?
* Agar saare URLs ek hi urls.py mein likhenge, file bahut badi ho jayegi.
* include() se hum app-wise URLs separate rakh sakte hain.


### **What is URL reversing?**
* URL reversing in Django is used to **generate URLs dynamically using their URL names** instead of hard-coding URL paths. It makes applications easier to maintain when URL patterns change.
* URL reversing ka matlab hai URL name ka use karke actual URL generate karna, instead of URL ko manually hard-code karna.
* Agar URL change ho: toh template mein URL manually change karne ki zarurat nahi hai. Sirf urls.py change karna padega.

#### Example: URL Reversing
1. urls.py — Pehle URL define kiya
```python
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
```

2. views.py
```python
from django.http import HttpResponse
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')
```

3. profile.html
```python
<a href="{% url 'profile' %}">My Profile</a>
```

* **Ab maan lo URL change kar diya**
```python
urlpatterns = [
    path('my-profile/', views.profile, name='profile'),
]
```
* ❗ Template mein kuch change nahi karna
```python
<a href="{% url 'profile' %}">My Profile</a>
```

### **What is reverse() in Django?**
* reverse() Django ka Python function hai jo URL name se actual URL generate karta hai.
* reverse() is used to generate a URL from its named URL pattern in Python code.

#### Example
```python
# URL
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]

# views.py
from django.urls import reverse

def some_view(request):
    url = reverse('profile')
    print(url)

    return HttpResponse("Hello")

# Output:- /profile/
```

#### Example for dynamic path
```python
path('user/<int:id>/', views.user_detail, name='user_detail')


url = reverse('user_detail', kwargs={'id': 10})
print(url)

/user/10/
```

### **reverse() vs url?**

| `reverse()`                   | `{% url %}`                |
| ----------------------------- | -------------------------- |
| Python code mein use hota hai | Template mein use hota hai |
| `reverse('profile')`          | `{% url 'profile' %}`      |
| URL generate karta hai        | URL generate karta hai     |
