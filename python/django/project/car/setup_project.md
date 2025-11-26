### Create virtual environment
```python
python -m venv virtual-name
```

### Activated virtual enviroment
```pyhton
cd virtual-name\Scripts
d:\mohit\virtual-name\Scripts> activate
```

### Install django
```python
<virtual-name> d:\mohit> python -m pip install django
OR
pip install django
```

### Create project
```python
django-admin startproject projectName .
OR
python manage.py startproject projectName .
```

### Start server
```python
python manage.py runserver
# change port
python manage.py runserver 8484
```


### Project setup one pc to another Pc
- optional this part
* First of all we run the command
```python
pip freeze > requirements.txt
```
* And other system follows these step
```python
# Create and activate virtual environment
virtualenv -p python3 env
. ./env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
pip install --default-timeout=100 -r requirements.txt

# Create SQLite databse, run migrations
cd myapp
./manage.py migrate

# Run Django dev server
./manage.py runserver
```
 
### Create App
- Create App
```python
python manage.py startapp app_name
OR
django-admin startapp app_name
```

- Now Add the app name in project -> setting.py file
```python
====project ki settings.py mai appn_ame add kar denge======
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',
]
```
- Add the template
```python
====project ki settings.py mai template add kar denge====== 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


### Url Settings
#### Step1:-
* Add code in **project urls.py** file
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')), # authentication is a app name
    path('accounts/', include('accounts.urls')), # accounts is a app name   
]
```

#### Step2:-
* Create urls.py file in your app folder(authentication)
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('create', views.stinsert, name='create1'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete_st),
]
```


### MySQL Database Connectivity
```python
firstly we create the database in mysql
```
* Install the package:- 
```python
pip install mysqlclient
```
In setting.py
```python
Update the connection string.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'mysql_user',
        'PASSWORD': 'mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            
         }
    }
}
```
```python
python manage.py migrate
```


### Super User create In Django
```python
====jha manage.py hota hai wha tak ka path======
(env) D:\mohit\blog\blog_project> python manage.py migrate
(env) D:\mohit\blog\blog_project> python manage.py createsuperuser
user
email
pass
(env) C:\Users\mohits4\env\Scripts\testdjango> python manage.py runserver
```

- if got error
```python
$ python manage.py createsuperuser
Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.
```
```python
winpty python manage.py createsuperuser
```



### Register in admin file
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