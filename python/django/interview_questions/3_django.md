### Back To TOP

|  No.  | Django Questions                                                                                         |
| :---: | -------------------------------------------------------------------------------------------------------- |
|       | [What is Django?](#-what-is-django)                                                                      |
|       | [How to install Django?](#-how-to-install-django)                                                        |
|       | [How to check django latest version?](#how-to-check-django-latest-version)                               |
|       | [Django:- Latest version](#latest-version-of-django)                                                     |
|       | [How to check installed packages?](#how-to-check-installed-packages)                                     |
|       | [How to run server?](#how-to-run-server)                                                                 |
|       | [Why is Django Used/Key Features?](#why-is-django-usedkey-features)                                      |
|       | [Django Architecture (MVT)](#django-architecture-mvt)                                                    |
|       | [What is MTV architecture?](#what-is-mtv-architecture)                                                   |
|       | [Create a Django Project?](#create-a-django-project)                                                     |
|       | [Django Project Structure](#django-project-structure)                                                    |
|       | [what is manage.py?](#1-managepy)                                                                        |
|       | [What is Django Apps?](#django-apps)                                                                     |
|       | [Create app](#creating-an-app)                                                                           |
|       | [Project vs App](#project-vs-app)                                                                        |
|       | [Why is Django called a "loosely coupled" framework?](#why-is-django-called-a-loosely-coupled-framework) |



<div style="page-break-before: always;"></div>

### 🎯 **What is Django?**
* Django—pronounced **“Jango”**. 
* Django is a free and open source and server-side web application framework written in Python.
* Django follows the **MVT** (Model View Template) pattern which is based on the Model View Template architecture. and provides many built-in features like authentication, database management, security, and an admin panel.
* It was orginally created By **Adrian Holovaty** and **simon willison**.

#### 🎯 **How to install Django?**
```python
pip install django
```

#### How to check django latest version?
```python
python -m django --version
```

#### **latest version of Django?**
* The latest version of Django is Django 6.1.

#### How to check installed packages?
```python
pip freeze
```

#### How to run server?
* By default, this cmd start the development server on the internal IP at port 8000
* By defalult, the server runs on port **8000** on the IP address **127.0.0.1**
```python
python manage.py runserver
python manage.py runserver 8000

# If i want to change server IP, pass it along with the port.
python manage.py runserver 0.0.0.0:8000
```

#### Why is Django Used/Key Features?
#### What are the advantages of Django?
* Fast Development
  * Django follows the **"Don't Repeat Yourself (DRY)" principle**.
  * Many built-in features reduce development time.
* Rapid development
* Built-in Admin Panel
  * Django automatically provides an admin interface.
  * You can manage users, products, orders, etc., without creating a separate admin dashboard.
* Authentication & Authorization
* ORM (Object Relational Mapper)
* Security features (CSRF, XSS, SQL Injection protection)
* Scalable and reusable code
* Large community support
* Form Handling
* Session Management
* Middleware Support
* REST API support (using Django REST Framework)
* 
* DRY (Don't Repeat Yourself) ka matlab hai: 👉 Same code ko baar-baar likhne se bachna.


1. Built-in Admin Panel
   1. Django automatically provides an admin interface.
   2. You can manage users, products, orders, etc., without creating a separate admin dashboard.
2. High Security
   1. Protects against common attacks:
      1. SQL Injection
      2. Cross-Site Scripting (XSS)
      3. Cross-Site Request Forgery (CSRF)
      4. Clickjacking
3. Scalable
   1. Suitable for small projects as well as large applications.
   2. Used by high-traffic websites.
4. ORM (Object Relational Mapping)
   1. Write Python code instead of raw SQL.
   2. Easier database operations and migration management.
   3. users = User.objects.filter(is_active=True)
5. MVT Architecture
   1. Uses Model-View-Template (MVT) pattern.
   2. Keeps code organized and maintainable.
6. Authentication System
   1. Built-in support for:
      1. Login
      2. Logout
      3. Registration
      4. Password Reset
      5. Permissions & Roles
7. Large Ecosystem
   1. Thousands of reusable packages available.
   2. Examples:
      1. Django REST Framework (API)
      2. Django Allauth (Social Login)
      3. Celery (Background Tasks)
8. Database Support
   1. MySQL
   2. PostgreSQL
   3. SQLite
   4. Oracle
9. SEO Friendly
   1.  Clean URLs and easy metadata management help SEO.
10. Excellent Documentation
   1.  One of the best documentations among Python frameworks.
   2. Easy for beginners to learn.
11. Testing Support
    1.  Built-in unit testing framework.
    2.  Helps maintain code quality.
<div style="page-break-before: always;"></div>

### 🎯**Django Architecture (MVT)**
* url request -> manage.py -> setting.py ->urls.py -> views.py -> models.py -> template.
* Django follows a software design pattern called a **MVT(Model view Template)** architecture.
* **Model:-** It helps in **handling the databse**. they provide the option to create edit and query data records in the databse.
* **View:-** the view is used to **execute the business logic** and intrect with a model to carry data and renders a template.
* **Template:-** The template is a **presentation layer**. It define the structure of file layout to present data in web page. it is an **html file** mixed with django template language.
```python
User Request
     ↓
   View
     ↓
  Model ↔ Database
     ↓
 Template
     ↓
User Response
```

### 🎯**What is MTV architecture?**
* Django की architecture को generally MVT (Model–View–Template) architecture कहा जाता है।
- Model → Handles database tables and data
- Template → Handles UI (HTML)
- View → Contains business logic
```python
User / Browser
      ↓
Django server
      ↓
Manage.py file
      ↓
setting.py file
      ↓
     URL
      ↓
    View
   ↙     ↘
Model    Template
  ↓         ↓
Database   HTML
      ↘   ↙
      Response
         ↓
      Browser
```


### 🎯**Create a Django Project?**
```python
django-admin startproject myproject
```
```python
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
<div style="page-break-before: always;"></div>


### 🎯**Django Project Structure?**
* When we create a Django project using:
```python
# Django creates a structure like this:

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

#### 1. manage.py
* This is the **command-line utility** used to manage your Django project.
```python
# Examples:
python manage.py runserver  :-  Start development server
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp users :-   Create an app
python manage.py shell
```

#### 2. __init__.py 
* An empty file that tells Python that the current directory should be considered as a Python package

2. settings.py
* Contains the **configuration/settings** of your Django project.
* It contains things like:
  * Database configuration
  * Installed apps
  * Middleware
  * Templates
  * Static files
  * Media files
  * Security settings
  * Time zone
```python
INSTALLED_APPS = [
    'users',
    'products',
]

DATABASES = {
    # Database configuration
}
```

3. urls.py
* This is the main URL configuration of the project.
* It decides which view should handle a particular URL.
* All the URLs of the project are present here
  
```python
# Example:

from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.users),
]
```

4. models.py
* Technically, the default project package created by startproject does not contain models.py; models.py belongs to Django apps.
```python
# For example:

myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   └── urls.py
│
└── users/
    ├── models.py
    ├── views.py
    └── ...
```
* models.py defines your database models.
```python
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

5. views.py
* Also belongs to an app, not normally the project package.
* It contains the application/business logic that handles requests.
```python
def home(request):
    return HttpResponse("Hello World")
```

6. asgi.py
* ASGI stands for Asynchronous Server Gateway Interface.
* It is used to serve Django applications in asynchronous environments and with ASGI-compatible servers.

7. wsgi.py
* WSGI stands for Web Server Gateway Interface.
* It is commonly used to deploy Django applications with traditional synchronous WSGI servers.
* This is an entry point for your application which is used by the web servers to serve the project you have created.

#### Project + App Structure
* In a real project, you'll usually have:
```python
myproject/
│
├── manage.py
│
├── myproject/              # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/                  # Django App
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── products/               # Another Django App
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```
<div style="page-break-before: always;"></div>

### 🎯**Django Apps?**
* A Django app is a small, independent module of a Django project that handles one specific functionality.
* A Django app is a reusable and modular component of a Django project that is responsible for a specific functionality, such as users, products, orders, or payments. A Django project can contain multiple apps.

```python
E-commerce Project
│
├── users        → Login, registration, profiles
├── products     → Product management
├── orders       → Order management
├── payments     → Payment processing
└── reviews      → Product reviews
```

### 🎯**Creating an App**
```python
python manage.py startapp products


products/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
```

### 🎯**Project vs App**
| Django Project                            | Django App                                |
| ----------------------------------------- | ----------------------------------------- |
| Complete website/application              | One specific functionality                |
| Contains multiple apps                    | Handles a particular feature              |
| Created using `django-admin startproject` | Created using `python manage.py startapp` |
| Example: `ecommerce`                      | Example: `products`, `orders`             |


### **Why is Django called a "loosely coupled" framework?**
* Django is called a loosely coupled framework because its components such as Models, Views, Templates, URLs, and Middleware **are independent of each other**. Changes in one component usually do not require changes in other components, making the application easier to maintain, test, and scale.
* Loosely Coupled = Components are independent and can be changed or replaced without affecting the whole application.
* We can change the frontend template, switch the database, or modify URLs without affecting the core business logic. This demonstrates Django's loosely coupled architecture.