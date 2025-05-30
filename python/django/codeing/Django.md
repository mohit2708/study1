### View calling
```python
=========urls.py======================
from .import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.individual_post, name='individual_post'),
]
======create viesw.py file=============
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, welcome to the index page.')


def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be. mohit')

```

## view calling using template
```python
====setting.py=========
 'DIRS': ['templates'],
# "DIRS": ["personal_portfolio/templates/"],
 =======create template folder in root directiry where is managed file=====
 =======and create file index.html ================
 <h1>Hello</h1>
 <h1>Hello {{name}}</h1>
 =====views.py=======
from django.shortcuts import render
from django.http import HttpResponse
def individual_post(request):
    return render(request, 'index.html')
    return render(request,"signup.html", {'name':'mohit'})
=======urls.py=======
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.individual_post, name='individual_post'),
]
```

## add 2 value
```python
=====urls.py==========
path('add/', views.add1, name='addvalue'),
======koi html file=================
<form action="{% url 'addvalue' %}">
	<input type="text" name="num1">
	<input type="text" name="num2">
	<input type="submit">
</form>
======result.html file=====
results : {{result}}
==========views.py===========
def add1(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1 + val2
    return render(request, "result.html", {'result':res})
============jab method post ho to===========================
<form method="post" action="{% url 'addvalue' %}">
	{% csrf_token %}
	<input type="text" name="num1">
	<input type="text" name="num2">
	<input type="submit">
</form>
===views.py=====
def add1(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request, "result.html", {'result':res})
```



## Registration
```python
=====model.py========
from django.db import models
# Create your models here.
class Auth(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
==========views.py========
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from auth_app.models import Auth
from issue_traking.forms import TicketForm

def handalsighnup(request):    
    try:
        if request.method == 'POST':
            fi_name= request.POST.get('f_name')            
            last_name= request.POST['last_name']
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            Auth.objects.update_or_create(username=username, email=email, last_name=last_name, first_name=fi_name, password=password, re_password=confirm_password)            
            return render(request, 'auth/signup.html')
        else:
		#form = TicketForm()
		#return render(request,'index.html', {'form':form})
            return render(request, 'auth/signup.html')
    except Exception as e:
        print("error:::", e)
+++++++++2 Type+++++++++++++

==urls.py====
path('signup1', views.handalsighnup, name='signup'),
=====signup.html=======
<form method="post" action="/signup1">
        {% csrf_token %}
<div class="col"><input type="text" class="form-control" name="f_name" placeholder="First Name" required="required"></div>
<div class="col"><input type="text" class="form-control" name="last_name" placeholder="Last Name" required="required"></div>
{{form.ticket_type}}
<input class="btn btn-primary btn-lg" type="submit">
```

### Ek page ko dusre mai call karana
```python
==========base.html===========
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
 {% block start %}
 {% endblock %}
</body>
</html>
===========home.html===========
{% extends "base.html" %}
{% block start %}
kuch bhi
{% endblock start %}
```

### Image ke liye settings
create media folder in root.
```python
=======model.py=========
image = models.ImageField(upload_to="ecomm/images", default="")

======settings.py=========
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

========main urls.py mai==========
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),
    path('issues/', include('issue_traking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### simple Slider  in loop
```python
==========views.py===========
def index(request):
    products = Product.objects.all()
    #print(products)   
    params = {'product':products}
    return render(request, 'ecomm/index.html', params)
========index.html==============
<ol class="carousel-indicators">
	{% for i in product %}
        <li class="{% if forloop.first %} active{% endif %}" data-slide-to="{{i}}" data-target="#myCarousel"></li>
        {% endfor %}
</ol>
------------------------
{% for i in product %}
<div class="item {% if forloop.first %} active{% endif %}" id="slide2">
<img src="{{i.image.url}}" >
<div class="carousel-caption">
<h4>{{i.product_name}}</h4>
<p>hi you</p>
</div>
</div>
{% endfor %}
      
```

__Installing packages:-__
```python
pip install requests
```
```python
cd C:\Users\mohits4\env\Scripts
django-admin startproject projectName
cd projectName
Python manage.py runserver
```


### for transfer project
```python
(env) C:\Users\mohits4\env\Scripts\testdjango> pip freeze > requirements.txt
(env) C:\Users\mohits4\env\Scripts\testdjango> pip install -r requirements.txt
```

### html form view using views.py
```python
=========models.py====================
from django.db import models
from django.utils import timezone

# Create your models here.
PRIORITY_CHOICES = (('critical', 'Critical'),
                    ('major', 'Major'),
                    ('medium', 'Medium'),
                    ('minor', 'Minor'),
                    ('trivial', 'Trivial'))
        
TYPE_CHOICES = (('bug', 'Bug'),
                ('feature', 'Feature'))
    
class Ticket(models.Model):

    title = models.CharField(max_length=64, default=' ', blank=False)
    description = models.TextField(blank=False)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default='trivial')
    ticket_type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='bug')
    date_added = models.DateTimeField(default=timezone.now, blank=False, editable=False)
    created_by = models.CharField(max_length=32, default=' ', blank=False, editable=False)

    def __str__(self):
        return self.title
===========form.py=========
from django import forms
from issue_traking.models import Ticket

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = '__all__'
      # fields = ('post','post2','category',)

============views.py===========
from django.shortcuts import render
from . import forms
from issue_traking.forms import TicketForm
# Create your views here.

def index(request):

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            pass
    form = TicketForm()
    return render(request, 'index.html', {'form':form})
===============index.html================
{% extends "home.html" %}
{% block start %}
<form method="post" action="" class="createticketform" enctype="multipart/form-data">
        <fieldset class="form-group">
            <legend>Create a new ticket</legend>
            {% csrf_token %}
            <div class="form-group">
                <label>Title:</label>
                <input type="text" class="form-control" id="title" name="title">
            </div>   
            <div class="form-group">
                <label>Description:</label>
                <textarea class="form-control" id="description" name="description" rows="3"></textarea>
            </div> 
            <div class="form-group">
                <label>File Upload:</label>
                <input type="file" class="form-control" id="file_upload" name="file_upload">
            </div>
            <div class="form-group">
                <label>Tickit Type:</label>
                {{form.ticket_type}}
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </fieldset>
    </form>
{% endblock start %}
```


### Install cripsy tag
```python
--------------------------------------
-->  pip install django-crispy-forms
---------------------------------------
INSTALLED_APPS = (
    ...
    'crispy_forms',
)
-----------------------------------------
{% load crispy_forms_tags %}
{{form|crispy }}
```


### Insert Data
**Create model.py**
```python
from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

    def __str__(self):
        return self.title
```
**create html file**
```python
<html>
   <head>
      <title>Create a Post </title>
   </head>
   <body>
      <h1>Create a Post </h1>
      <form action="" method="POST">
         {% csrf_token %}
         Title: <input type="text" name="title"/><br/>
         Content: <br/>
         <textarea cols="35" rows="8" name="content">
         </textarea><br/>
         <input type="submit" value="Post"/>
      </form>
   </body>
</html>
```
**Views.py**
```python
from django.shortcuts import render
from .models import Post


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'posts/create.html')  

        else:
                return render(request,'posts/create.html')
```

