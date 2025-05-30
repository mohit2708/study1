# Django interview questions

### Table of Contents

https://www.interviewbit.com/django-interview-questions/ -- 4 tak complete
https://www.javatpoint.com/django-interview-questions-and-answers -- 1

|  No.  | Questions                                                                                               |
| :---: | ------------------------------------------------------------------------------------------------------- |
|       | [What is Django?](#Ques-What-is-Django)                                                                 |
|       | [What is the latest version of Django?](#Ques-What-is-the-latest-version-of-Django)                     |
|       | [Explain Django architecture?](#Ques-Explain-Django-architecture)                                       |
|       | [Explain the django project directory structure?](#Ques-Explain-the-django-project-directory-structure) |
|       | [Give a brief about the settings.py file?](#Ques-Give-a-brief-about-the-settingspy-file)                |
|       | [What are static files in Django? And how can you set them?](#)                                         |
|       | [What is the difference between Python and Django?](#)                                                  |
|       | [What is Jinja templating?](#)                                                                          |
|       | [What are templates in Django or Django template language?](#)                                          |
|       | [create a migration file inside the migration folder?](#)                                               |
|       | [What are models in Django?](#)                                                                         |
|       | [Name some companies that make use of Django?](#)                                                       |
|       | [How to create virtual Enviroment and How can Activate?](#)                                             |
|       | [How to install Django and Uninstall Django?](#)                                                        |
|       | [How do you check for the version of Django installed on your system?](#)                               |
|       | [Check all the version of install modules?](#)                                                          |
|       | [What is the difference between a project and an app in Django?](#)                                     |
|       | [How to create Project and App?](#)                                                                     |
|       | [Project Directery](#)                                                                                  |
|       | [App Directery](#)                                                                                      |
|       | [How to Run Server](#)                                                                                  |
|       | [create a superuser](#)                                                                                 |
|       | [ What is the django command to view a databse schema of an existing(or legacy) databse?](#)            |
|       | [How to view all items in the Model using django QuerySet?](#)                                          |
|       | [How to filter items in the model using django QuerySet?](#)                                            |
|       | [How to get a particular items in the model using django QuerySet?](#)                                  |
|       | [Model Meta Options](#)                                                                                 |
|       | [Meta Class in Models?](#)                                                                              |
|       | [What is CRUD operations Django?](#)                                                                    |
|       |                                                                                                         |
|       |                                                                                                         |
|       |                                                                                                         |


### **Ques. What is virtual Enviroment**
* A virtual environment is like a separate space wherein we can install our project requirements which is completely isolated from the global installations.

### **Ques. What is Django?**
* Django—pronounced “Jango,”. Django is a free and open source and server-side web application framework written in Python.
* Django follows the MVT (Model View Template) pattern which is based on the Model View Controller architecture.
* It was orginally created By Adrian Holovaty and simon willison.

### **Ques. What is the latest version of Django?**
The latest version of Django is Django 4.1.

### **Ques. Explain Django architecture?**
* url request -> manage.py -> setting.py ->urls.py -> views.py -> models.py -> template.
* Django follows a software design pattern called a **MVT(Model view Template)** architecture.
* **Model:-** It helps in handling the databse. they provide the option to create edit and query data records in the databse.
* **View:-** the view is used to execute the business logic and intrect with a model to carry data and renders a template.
* **Template:-** The template is a presentation layer. It define the structure of file layout to present data in web page. it is an html file mixed with django template language.
----
* Here, a user requests for a resource to the Django, Django works as a controller and check to the available resource in URL.
* If URL maps, a view is called that interact with model and template, it renders a template.
* Django responds back to the user and sends a template as a response.
------

### **Ques. Explain the django project directory structure?**
<ul>
    <li><b>manage.py</b> - A command-line utility that allows you to interact with your Django project</li>
    <li><b>__init__.py</b> - An empty file that tells Python that the current directory should be considered as a Python package</li>
    <li><b>settings.py</b> - configurations of the current project like DB connections.</li>
    <li><b>urls.py</b> - All the URLs of the project are present here</li>
    <li><b>wsgi.py</b> - This is an entry point for your application which is used by the web servers to serve the project you have created.</li>
</ul>

### **Ques. Give a brief about the settings.py file?**
As the name implies, 
* it's the main settings file of the Django file. Everything inside the Django project, 
* like databases, 
* middlewares, 
* templating engines, 
* installed applications, 
* static file addresses, 
* main URL configurations, 
* backend engines, 
* allowed hosts and servers, 
* and security key stores in this file as a dictionary or list.

So when Django files start, it first executes the settings.py file and then loads the respective databases and engines to quickly serve the request.




### **Ques. What are static files in Django? And how can you set them?**
* static file for used add the image, css and javascript files.
* Static files managed by “**django.contrib.staticfiles**”. 
* There are three main things to do to set up static files in Django:
1. Set STATIC_ROOT in settings.py
```python
STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
2. Run manage.py collect static
3. Set up a Static Files entry on the PythonAnywhere web tab


### **Ques. What is the difference between Python and Django?**
* Both Python and Django are intertwined but not the same. Python is a programming language used for various application developments: machine learning, artificial intelligence, desktop apps, etc.
* Django is a Python web framework used for full-stack app development and server development.
* Using core Python, you can build an app from scratch or craft the app with Django using prewritten bits of code.

### **Ques. What are templates in Django or Django template language?**
* A template in Django is basically written in HTML, CSS, and Javascript in a .html file. Django framework efficiently handles and generates dynamically HTML web pages that are visible to the end-user.
* Django Templates can be configured in app_name/settings.py.

### **Ques. What is Jinja templating?**
Jinja Templating is a very popular templating engine for Python, the latest version is Jinja2. 
* Sandbox Execution - This is a sandbox (or a protected) framework for automating the testing process
* HTML Escaping - It provides automatic HTML Escaping as <, >, & characters have special values in templates and if using a regular text, these symbols can lead to XSS Attacks which Jinja deals with automatically.
* Template Inheritance
* Generates HTML templates much faster than default engine
* Easier to debug as compared to the default engine.

### **Ques. create a migration file inside the migration folder?**
```python
python manage.py makemigrations

# after creation a migration to reflect in the database.
python manage.py migrate

# single migration 
python manage.py sqlmigrate app_name migrate_name

# to see all migrations.
python manage.py showmigrations

# to see specific migrations by specifying app name
python manage.py showmigrations app_name
```


### **Ques. What are models in Django?**
* A model is a class used in Django that represents table or collection in our database, and where every attribute of the class is a field of the table or collection. Models are defined in the app/models.py (in our example: myapp/models.py).
* A model is a Python class in Django that is derived from the **django.db.models.Model** class. It is used to interact with and get results from the database tables of our application.
* Each model class maps to a single table in the database.
* Every model inherits from **django.db.models.Model**.

```python
from django.db import models

class Employee(models.Model):

    id = models.AutoField('Id', primary_key=True)
    first_name  = models.CharField('First name', max_length=15, null = True)
    last_name   = models.CharField('Last name', max_length=16, blank=True)
    email       = models.EmailField(max_length = 255, unique=True, null = True)
    user_name   = models.CharField(max_length=50, unique=True, null = True, error_messages ={
                    "unique":"The User Name Field you entered is unique."
                    })
    number = models.IntegerField()
    dof = models.DateField('Birthday')

    class Meta:
      db_table = "employee"
  
   	def __str__(self):
		  return "{} {}".formet(self.first_name, self.last_name)
```

### **Ques. Name some companies that make use of Django?**
Some of the companies that make use of Django are Instagram, DISCUS, Mozilla Firefox, YouTube, Pinterest, Reddit, etc.

#### Ques. What are the features of Django?
* SEO Optimized
* Extremely fast

### **Ques. How to create virtual Enviroment and How can Activate?**
```python
python -m venv virtual-name

# Activate Process
virtual Enviroment Folder -> Scripts -> Activate
```

### **Ques. How to install Django and Uninstall Django?**
```python
# Install Django
pip install django
python -m pip install django

# Uninstall Django
pip uninstall django
```

### **Ques. How do you check for the version of Django installed on your system?**
```python
# you can open the command prompt and enter the following command:
python -m django –-version

# You can also try to import Django and use the get_version() method as follows:
import django
print(django.get_version())
```

### **Ques. Check all the version of install modules?**
```python
pip freeze
```

### **Ques. What is the difference between a project and an app in Django?**
* in simple words Project is the entire Django application and an app is a module inside the project that deals with one specific use case. For eg, payment system(app) in the eCommerce app(Project)
* A project, is a collection of these apps.


### **Ques. How to create Project and App?**
```python
# Create the Project
django-admin startproject projectName

# Create the app
python manage.py startapp app_name
```

### **Project Directery**
```python
project
  manage.py
  project
    __init__.py
    asgi
    settings  # congigration of the project like db connection, middleware.
    urls      # urls
    wsgi      # this is entery point server related details
```

### **App Directery**
```python
app
  __init__.py
  admin.py
  apps.py
  migrations
    __init__.py
  models.py
  tests,py
  views.py
```

### **Ques. How to Run Server?**
```python
# run a project
python manage.py runserver

#change a port number
python manage.py runserver:8484

# change the server ip and port
python manage.py runserver0.0.0.0:8484
```

### **Ques. create a superuser**
```python
# create a super user
python manage.py createsuperuser

username: ------
email address: ------
password: -------
password(again): ------
superuser created successfully
```

### **Ques. What is the django command to view a databse schema of an existing(or legacy) databse?**
```python
python manage.py inspectdb
OR
python manage.py inspectdb > blog_app/models.py
```

### **Ques. How to view all items in the Model using django QuerySet?**
```python
Users.objects.all()

# where "Users" is a model name
```

### **Ques. How to filter items in the model using django QuerySet?**
```python
Users.objects.filter(name="mohit")

# where "Users" is a model name
```

### **Ques. How to get a particular items in the model using django QuerySet?**
```python
Users.objects.get(id=25)

# where "Users" is a model name
```

### **Ques. Model Meta Options?**
1. abstract
   If abstract = True, this model will be an abstract  base class
```python
class student(models.Model):
  class Meta:
      abstract = True
```

2. app_label
   If a model is defined outside of applications in INSTALLED_APPS, it must declare which app  it belongs to:
```python
class student(models.Model):
  class Meta:
      app_label = 'myapp' # add app name here
```

3. verbose_name:- verbose_name is basically a human-readable name for your model
```python
class student(models.Model):
  class Meta:
      verbose_name = "stu" # add verbose_name  here
```

4. ordering:- Ordering is basically used to change the order of your model fields.
```python
class student(models.Model):
  class Meta:
      ordering = [-1]
```

5. proxy:- If we add proxy = True a model which subclasses another model will be treated as a proxy model
```python
class Student(Teacher):
  class Meta:
      proxy = True
```

6. permissions:- Extra permissions to enter into the permissions table when creating this object. Add, change, delete and view permissions are automatically created for each model.
```python
class student(models.Model):
  class Meta:
      permissions = []
```

7. db_table:- We can overwrite the table name by using db_table in meta class.
```python
class student(models.Model):
  class Meta:
      db_table = 'table_name'
```

8. get_latest_by:- It returns the latest object in the table based on the given field, used for typically DateField, DateTimeField, or IntegerField.
```python
class student(models.Model):
  class Meta:
      get_latest_by = "order_date"
```



### How to Show tables in admin Panel
```python
# 1 Option
# In model file
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, verbose_name = "First Name")  
    last_name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        ret = self.first_name + ', ' + self.last_name
        return ret
# Add below code in admin.py
from employeeFunctionBased.models import Employee
 admin.site.register(Employee)

# 2 Option in admin.py
from employeeFunctionBased.models import Employee

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name']
```

### Include Css and js in django
 ```python
 # 1. Create the Static Folder where manage.py
 # 2. Add Code in setting.py

STATIC_URL = 'static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR,'static') ]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# 3. Add code in html file
{% load static %}
<link rel="stylesheet" type="text/css"  href="{% static 'admin/css/adminlte.min.css' %}" />
 ```


### **Ques. Meta Class in Models?**
Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options. It’s completely optional to add a Meta class to your model.
```python
class student(models.Model):
    class Meta:
        options........
```


### **Ques. What is CRUD operations Django?**
Django is a Python-based web framework that follows the MVT (Model View Template) pattern and allows you to quickly create web applications. It offers built-in class-based generic views for CRUD operations. CRUD in general means Creating, Retrieving, Updating and Deleting operations on a table in a database.

What is class based view in Django?
Class-based view is an alternative to function-based view. They do not replace function-based views, but have some distinct differences and advantages over function-based views.

What is generic views in Django?
Django generic views have been developed as shortcuts for common usage methods such as displaying object details.
They take some of the common methods found in view development and abstract them so that you can quickly write common views of data without writing too much code.

What is DetailView in Django?
Django DetailView should be used when you want to present detail of a single model instance. Its purpose is to use with only one object.

### **What is a cookie in Django?**
* A cookie is a small piece of information that is stored in the client browser. It is used to store user’s data in a file permanently (or for the specified time). Cookie has its expiry date and time and gets removed automatically when it gets expired. Django provides in-built methods to set and fetch cookies.





====================================================================================================================
1. What is Django Admin Interface?
Django comes with a fully customizable in-built admin interface, which lets us see and make changes to all the data in the database of registered apps and models. To use a database table with the admin interface, we need to register the model in the admin.py file.

1. Explain Django’s Request/Response Cycle.
In the Request/Response Cycle, first, a request is received by the Django server. Then, the server looks for a matching URL in the urlpatterns defined for the project. If no matching URL is found, then a response with 404 status code is returned. If a URL matches, then the corresponding code in the view file associated with the URL is executed to build and send a response.


1. What are migrations in Django?
A migration in Django is a Python file that contains changes we make to our models so that they can be converted into a database schema in our DBMS. So, instead of manually making changes to our database schema by writing queries in our DBMS shell, we can just make changes to our models. Then, we can use Django to generate migrations from those model changes and run those migrations to make changes to our database schema.

1. What are views in Django?
A view in Django is a class and/or a function that receives a request and returns a response. A view is usually associated with urlpatterns, and the logic encapsulated in a view is run when a request to the URL associated with it is run. A view, among other things, gets data from the database using models, passes that data to the templates, and sends back the rendered template to the user as an HttpResponse.

1. What is the use of the include function in the urls.py file in Django?
As in Django there can be many apps, each app may have some URLs that it responds to. Rather than registering all URLs for all apps in a single urls.py file, each app maintains its own urls.py file, and in the project’s urls.py file we use each individual urls.py file of each app by using the include function.

1.  Why is Django called a loosely coupled framework?
Django is called a loosely coupled framework because of its MVT architecture, which is a variant of the MVC architecture. It helps in separating the server code from the client-related code. Django’s models and views take care of the code that needs to be run on the server like getting records from database, etc., and the templates are mostly HTML and CSS that just need data from models passed in by the views to render them. Since these components are independent of each other, Django is called a loosely coupled framework.


1.  What is Django ORM?
ORM stands for Object-relational Mapper. Instead of interacting with the database by writing raw SQL queries and converting the data returned from the query into a Python object, ORM allows us to interact with the database using objects of our model class. So, we just interact with our models and ORM converts these changes into SQL queries based on the database we are using, e.g., SQLite.

1.  How do templates work in Django?
In Django, templates are used to dynamically generate web content. Django’s templating engine handles templating that involves parsing, processing, and converting the template into an HttpResponse to return back to the client. These templates are by default written in Django Templating Language (DTL), which allows us to output the dynamic content in the templates based on the data passed in by the view.

1.  How do we register a model with Django admin?
To register a model with Django’s admin interface, we make changes to our apps admin.py file. We have to open the admin.py file in the app folder in which our models are. For example, if we have an app named ‘polls’ and we wish to register a model named ‘Question’, then we need to open ‘polls/admin.py’ and import the Question model and write: admin.site.register(Question). This will register our Question model with the admin site.

1.  How do we generate a super user in Django?
In our project folder that contains Django’s manage.py script, we have to open the command prompt and type the python manage.py createsuperuser command. Then, we need to enter the username, the email, and finally the password, twice (for conformation). This will create a super user for our Django project.

1.  Mention some disadvantages of Django.
Django has the following disadvantages:

Django’ modules are bulky.
It is completely based on Django ORM.
Components are deployed together.
We must know the full system to work with it.
16. What is Sessions Framework in Django?
The Sessions framework in Django is used to store arbitrary information about the user on the server in the database. This is done because HTTP is a stateless protocol, i.e., it does not store information between subsequent requests. Django uses a cookie containing a special session ID to identify each browser and its associated session with the site.

1.  What is a middleware in Django?
A middleware is a layer in Django’s Request/Response processing pipeline. Each middleware is responsible for performing some specific functions on the request and/or response, such as caching, gzipping, etc.

1.  What is a QuerySet in Django?
A QuerySet in Django is basically a collection of objects from our database. QuerySets are used by the Django ORM. When we use our models to get a single record or a group of records from the database, they are returned as QuerySets.

1.  What is Django REST Framework?
Django REST Framework (DRF) is a Django app and a framework that lets us create RESTful APIs rapidly. DRF is especially useful if we have an existing Django web application and we wish to quickly generate an API for it.

Certification in Full Stack Web Development

21. What is a context in Django?
A context in Django is a dictionary, in which keys represent variable names and values represent their values. This dictionary (context) is passed to the template which then uses the variables to output the dynamic content.

22. List some of the caching strategies that Django supports.
Django supports the following caching strategies:

File System Caching
Memcached
In-memory Caching
Database Caching
23. What is a Meta Class in Django?
A Meta class is simply an inner class that provides metadata about the outer class in Django. It defines such things as available permissions, associated database table name, singular and plural versions of the name, etc.

24. When should we generate and apply migrations in a Django project and why?
We should do that whenever we create or make changes to the models of one of the apps in our project. This is because a migration is used to make changes to the database schema, and it is generated based on our models.

25. What is serialization in Django?
Serialization is the process of converting Django models into other formats such as XML, JSON, etc.

26. What are generic views?
When building a web application there are certain kind of views that we build again and again, such as a view that displays all records in the database (e.g., displaying all books in the books table), etc. These kinds of views perform the same functions and lead to repeated code. To solve this issue, Django uses class-based generic views. When using generic views, all we have to do is inherit the desired class from django.views.generic module and provide some information like model, context_object_name, etc.

28. Which class do we inherit from in order to perform unit tests?
We inherit from django.test.TestCase in order to perform unit tests as it contains all the methods we need to perform unit tests like assertEquals, assertTrue, etc.

29. Which class do we inherit from in order to perform functional tests?
We inherit from django.test.LiveServerTestCase. It launches a live Django server in the background on setup and shuts it down on teardown. This allows the use of automated test clients, e.g., the Selenium client, to execute a series of functional tests inside a browser and simulate a real user’s actions.

30. What is the django.test.Client class used for?
The Client class acts as a dummy web browser, allowing us to test our views and interact with our Django-powered application programmatically. This is especially helpful for doing integration testing.
