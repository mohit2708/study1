|  No.  | [Install django and create project and app](./1.2_install_django_project_app.md) |
| :---: | -------------------------------------------------------------------------------- |
|       | [Install django?](#install-django)                                               |
|       | [Uninstall django?](#uninstall-django)                                           |
|       | [Check django version?](#check-django-version)                                   |
|       | [Create project?](#create-project)                                               |
|       | [Start server?](#start-server)                                                   |
|       | [Create App?](#create-app)                                                       |

### Install django
```python
<virtual-name> d:\mohit> python -m pip install django
OR
pip install django
```

### Uninstall django
```python
pip uninstall django
```

### Check django version
```python
django-admin --version (OR)
python -m django --version
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

### Create App
```python

python manage.py startapp app_name
OR
django-admin startapp app_name

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