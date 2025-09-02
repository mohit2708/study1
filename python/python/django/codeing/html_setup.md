### **Html Setup Ek page ko dusre mai call karana**
* Seting.py
```python
1. Create the folder `static` in root file.
===== css and js incluse karne ke liye seeting
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

* templates/Base.html
```python
<!DOCTYPE html>
<html lang="en">
<head>
  <title>AdminLTE 3 | {% block title %}{% endblock %}</title>

  {% load static %}                     # include
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="{% static 'css/all.min.css' %}">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
 {% block start %}
 {% endblock %}
</body>
</html>
```

* templates/home.html
```python
{% block title %}Page Title{% endblock title %}

{% extends "base.html" %}
{% block start %}
kuch bhi
{% endblock start %}
```

