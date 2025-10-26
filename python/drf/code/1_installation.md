* **Step1:-** [Create the virtual environment](../common_codeing/1.1_install_python_virtual_env.md)
* **Step2:-** [Install django](../django/codeing/1.2_install_django_project_app.md#install-django)
* **Step3:-** Installation
```python
pip install djangorestframework
```
* **Step4:-** Add 'rest_framework' to your INSTALLED_APPS setting.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

#### Create the app:
```python
python manage.py startapp students
```

#### add the app name in INSTALLED_APPS in setting file
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'students',
    'api',
    'apiclassbased',
    ...
]
```
