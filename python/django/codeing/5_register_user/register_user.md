### Basic customer table
#### Create Model file stacture
- Create a models folder in your app
- create customer.py file inside the model folder
- __init__.py file inside the model folder
```python
myapp/
    models/
        __init__.py
        customer.py
        ....
        ....
    views/
    urls.py
    apps.py
```

#### Create model
- model/customer.py file
- We **don't need to define the primary key**. Django auto-creates id as PK.
```python
from django.db import models
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)   # Set only first time
    updated_at = models.DateTimeField(auto_now=True)       # Update every save

    def save(self, *args, **kwargs):
        # Hash password before saving (good practice)
        if not self.password.startswith("pbkdf2"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name
```
- mode/__init__.py file
```python
from .customer import Customer
```

### Register cutomer model in admin.py file
```python
from django.contrib import admin
from .models import Customer

admin.site.site_header = "Mohit ka Panel"
admin.site.site_title = "Mohit Admin Portal"
admin.site.index_title = "Mohit Welcome to Dashboard"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "user_name", "created_at")
    search_fields = ("first_name", "last_name", "user_name")
```

### create view file
- create auth_view.py file
```python
def signupGet(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        context = {
            "first_name": firstname,
            "last_name": lastname,
            "email": email,
            "user_name": username,
        }

        # Check username
        if Customer.objects.filter(user_name=username).exists():
            messages.error(request, f"{username} already exists")
            return render(request, "auth/signup.html", context)
            # return render(request, "auth/signup.html", {"first_name": firstname, "last_name": lastname, "email": email})

        # Check email
        if Customer.objects.filter(email=email).exists():
            messages.error(request, f"{email} already exists")
            return render(request, "auth/signup.html")


        Customer.objects.create(
            first_name=firstname,
            last_name=lastname,
            user_name=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "auth/signup.html")
```

### register init file
```python
from .auth_view import signupGet, login_view, logout_view
```

### create html file
- create templates/auth/signup.html file
```python
<h2>Signup</h2>
{% if messages %}
<div id="message-box" style="color:red; margin-bottom:10px;">
    {% for message in messages %}
        {{ message }}
    {% endfor %}
</div>
{% endif %}
<form method="POST">
    {% csrf_token %}
    First Name: <input type="text" name="first_name" value="{{ first_name|default:'' }}"><br>
    Last Name: <input type="text" name="last_name" value="{{ last_name|default:'' }}"><br>
    Username: <input type="text" name="user_name" value="{{ user_name|default:'' }}"><br>
    Email: <input type="email" name="email" value="{{ email|default:'' }}"><br>
    Password: <input type="password" name="password"><br>
    <button type="submit">Signup</button>
</form>

<a href="/login/">Login</a>
```
```python
# jab koi error aati hai to form fill hi rahta hai 
value="{{ first_name|default:'' }}">

# view file mai
context = {
    "first_name": firstname,
    "last_name": lastname,
    "email": email,
    "user_name": username,
}

# Check username
if Customer.objects.filter(user_name=username).exists():
    messages.error(request, f"{username} already exists")
    return render(request, "auth/signup.html", context)
    # return render(request, "auth/signup.html", {"first_name": firstname, "last_name": lastname, "email": email})
```
### url file
```python
from django.contrib import admin
from django.urls import path
from car_app.views import view_home
from car_app.views import auth_view, dashboard_views


urlpatterns = [
    path("", view_home.home, name="home"),
    # path("signup/", auth_view.signupFunction, name="signup"),
    path('signup/', auth_view.signupGet, name='signupget'),
    path("login/", auth_view.login_view, name="login"),
    path('logout/', auth_view.logout_view, name="logout"),
    path('dashboard/', dashboard_views.dashboard, name="dashboard"),
]
```
