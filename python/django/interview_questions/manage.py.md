### What is manage.py?
- manage.py Django का **command-line utility script** होता है जो आपके Django project को run और manage करने के लिए use होता है।
- जब आप django-admin startproject projectname चलाते हो, तब project के root में manage.py बनता है।
- यह internally:
  - आपके project की settings load करता है
  - सही environment set करता है
  - फिर Django command execute करता है
- 🧠 Interview line
  - manage.py is a project-specific command-line utility that allows us to interact with Django and execute management commands using the project’s settings.

### manage.py क्या करता है?
- यह Django के commands run करने का entry point है।
- आप जो भी Django commands चलाते हो जैसे:
  - python manage.py runserver
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py startapp appname
- ये सब manage.py के through run होते हैं।


### manage.py file
```python
#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```
- Important line 👇
  - यह बताती है कि कौन-सी settings file use करनी है।
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')
```


