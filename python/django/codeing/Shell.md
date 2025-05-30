```python
python manage.py shell
```

### Run with sql query
* install package
```python
pip install django-extensions
```
* add code in settings.py after package install
```python
INSTALLED_APPS = INSTALLED_APPS + [
    # ...
    'django_extensions',
]
```
```python
python manage.py runserver
```

### Now wo check shell in CMD
```python
python manage.py django_shell-plus
python manage.py shell_plus --print-sql
```

