### Django का Default User Model
- Django का Default User Model उपयोग करके Simple Signup (Registration) करना सबसे आसान और recommended तरीका है, खासकर beginners के लिए। इसमें हम django.contrib.auth.models.User का use करते हैं।

#### Django Default User Model क्या होता है?
- Django पहले से ही एक built-in User model देता है:
```python
from django.contrib.auth.models import User
```
- इसमें ये fields already होती हैं:
  - username
  - email
  - password
  - first_name
  - last_name
  - is_active
  - is_staff
  - is_superuser
- इसलिए अलग से models.py में user table बनाने की जरूरत नहीं होती।

#### Signup View (Simple Function Based View)
```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        username   = request.POST.get("username")
        email      = request.POST.get("email")
        password   = request.POST.get("password")

        # Username already exists check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        # Email already exists check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")

        # Create user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password)  # Password hashing
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "signup.html")

```

#### URLs Configuration
- app/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]

```
- Main project urls.py में app include करें:
```python
path("", include("accounts.urls")), 
```

#### Signup HTML Form
- templates/signup.html
```python
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
</head>
<body>

<h2>Signup Form</h2>

{% if messages %}
  {% for message in messages %}
    <p style="color:red;">{{ message }}</p>
  {% endfor %}
{% endif %}

<form method="POST">
    {% csrf_token %}

    <input type="text" name="first_name" placeholder="First Name" required><br><br>
    <input type="text" name="last_name" placeholder="Last Name" required><br><br>
    <input type="text" name="username" placeholder="Username" required><br><br>
    <input type="email" name="email" placeholder="Email" required><br><br>
    <input type="password" name="password" placeholder="Password" required><br><br>

    <button type="submit">Signup</button>
</form>

</body>
</html>

```


### chatgpt link
- https://chatgpt.com/share/6927ee9b-c4c4-800b-90ec-0791d2aa078e
- https://chatgpt.com/share/6927ee9b-c4c4-800b-90ec-0791d2aa078e
- https://chatgpt.com/share/6927ee9b-c4c4-800b-90ec-0791d2aa078e