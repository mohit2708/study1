### **How to use for Authentication in Django?**
* Django provides a built-in authentication system through **django.contrib.auth**. For REST APIs, we commonly use Django REST Framework with JWT authentication, typically using **djangorestframework-simplejwt**.
* Django ka built-in Authentication System hota hai.
* Django mein by default ye available hota hai:
  * django.contrib.auth
  * User model
  * authenticate()
  * login()
  * logout()
  * Password hashing
  * Sessions
  * Permissions
  * Groups

#### Example:
```python
from django.contrib.auth import authenticate, login, logout

user = authenticate(
    username="mohit",
    password="123456"
)

if user is not None:
    login(request, user)
```

### JWT ke liye Django mein commonly:
```python
pip install djangorestframework
pip install djangorestframework-simplejwt
```

```python
from rest_framework_simplejwt.tokens import RefreshToken
```

### **What is authenticate() in Python/Django?**
* authenticate() is a Django function used to verify a user's credentials. If the credentials are valid, it returns the User object; otherwise, it returns None.
* In Django, authenticate() is used to verify whether the provided username/email and password are valid.
* It is mainly used during login.
```python
from django.contrib.auth import authenticate, login

user = authenticate(
    username="mohit",
    password="123456"
)

if user is not None:
    login(request, user)
    print("Login successful")
else:
    print("Invalid credentials")
```