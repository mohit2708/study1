### 🎯 **What is Django Template Engine?**
* Django Template Engine is a system in Django that is used to create dynamic HTML pages by combining HTML templates with data from Python/Django views.
* Django Template Engine is a built-in system used to generate dynamic HTML pages. It allows us to display data from views/models in HTML using template syntax such as variables, loops, conditions, template inheritance, and filters.

#### Example
* views.py
```python
from django.shortcuts import render

def home(request):
    name = "Mohit"
    return render(request, "home.html", {"name": name})
```
* home.html
```python
<h1>Welcome {{ name }}</h1>
```
* Output:- Welcome Mohit

### Important Template Syntax?
| Syntax           | Purpose                     |
| ---------------- | --------------------------- |
| `{{ variable }}` | Display data                |
| `{% if %}`       | Conditional logic           |
| `{% for %}`      | Loop                        |
| `{% url %}`      | Generate URL                |
| `{% include %}`  | Include another template    |
| `{% extends %}`  | Template inheritance        |
| `{% block %}`    | Define replaceable sections |
| `{# comment #}`  | Template comment            |


### 🎯 **Difference between {{ }} and {% %}?**
* **{{ }}** is used to **display dynamic data or variables**, whereas **{% %}** is used for **template logic and instructions such as conditions, loops, URL generation, and template inheritance**.
* Django templates में {{ }} और {% %} दोनों का use dynamic behavior के लिए होता है, लेकिन उनका purpose अलग है।

#### {{ }}
* Data display करने के लिए
* यह variable या value को HTML में show करता है।


#### {% %}
* Logic / Template instructions के लिए
* इसका use condition, loop, URL, template inheritance आदि के लिए होता है।

#### **if** — Condition
```python
{% if age >= 18 %}
    <p>Adult</p>
{% else %}
    <p>Minor</p>
{% endif %}
```

#### **for** — Loop
```python
{% for user in users %}
    <p>{{ user.name }}</p>
{% endfor %}
```

#### **url** — Generate URL
```python
<a href="{% url 'home' %}">Home</a>
```

#### **extends** — Template Inheritance
```python
{% extends "base.html" %}
```

#### **include** — Include Another Template
```python
{% include "header.html" %}
```

#### **block** — Define a Replaceable Section
```python
{% block content %}
    <h1>Home Page</h1>
{% endblock %}
```


| `{{ }}`                  | `{% %}`                                   |
| ------------------------ | ----------------------------------------- |
| Data/value display करता है | Logic/instructions execute करता है          |
| Variables के लिए           | `if`, `for`, `url`, `extends`, `block` आदि |
| Example: `{{ name }}`    | Example: `{% if user %}`                  |

### 🎯 **What are template tags?**
* Template tags are special Django template commands **used to perform logic** and **template operations such as conditions**, **loops**, URL generation, template inheritance, and including other templates. They are written using {% %} syntax.

### **What are filters?**
* Django template filters are u**sed to modify or format variable values before displaying them** in a template.
* Filters are applied **using the pipe (|) symbol**, such as {{ name|upper }}.
* Django Template Filters are used to modify or format the value of a variable before displaying it in a template.
* They are written using the pipe (|) symbol.
* Filter = Variable ke data ko modify/format karna.
```python
{{ name|upper }}

# Output:- MOHIT
```

#### Multiple Filters
```python
{{ name|lower|title }}

# maan lo naam hai MOHIT SAXENA
name
 ↓
"MOHIT SAXENA"
 ↓ lower
"mohit saxena"
 ↓ title
" Mohit Saxena"
```

| Filter          | Purpose       | Example  |                      |
| --------------- | ------------- | -------- | -------------------- |
| `upper`         | Uppercase     | `{{ name | upper }}`            |
| `lower`         | Lowercase     | `{{ name | lower }}`            |
| `title`         | Title Case    | `{{ name | title }}`            |
| `length`        | Length        | `{{ name | length }}`           |
| `default`       | Default value | `{{ name | default:"Guest" }}`  |
| `truncatechars` | Shorten text  | `{{ text | truncatechars:20 }}` |
| `date`          | Format date   | `{{ date | date:"Y-m-d" }}`     |
| `add`           | Add value     | `{{ age  | add:"5" }}`          |

### **How do you extend templates?**
* Django provides template inheritance using {% extends %} and {% block %} tags. We create a common base template containing the shared HTML structure, and child templates extend it and override specific blocks with page-specific content.
* Django में template inheritance का use करके हम एक common/base HTML template को दूसरे templates में reuse कर सकते हैं।
* इसके लिए मुख्यतः {% extends %} और {% block %} का use होता है।

#### Example
* base.html
```python
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>

    <header>
        <h1>My Website</h1>
    </header>

    {% block content %}
    {% endblock %}

</body>
</html>
```
* home.html
```python
{% extends "base.html" %}

{% block title %}
Home
{% endblock %}

{% block content %}
    <h2>Welcome to Home Page</h2>
    <p>Hello Mohit!</p>
{% endblock %}
```


### **What is template inheritance?**
* Template inheritance is a Django feature that allows child templates to reuse a common base template and override specific blocks with their own content. It helps avoid code duplication and makes templates easier to maintain.
* **almost same, but exactly same nahi hai.**
* {% extends %} → Django ka template tag hai.
* Template inheritance → concept/feature hai, jisme extends ka use karke base template reuse karte hain.
* Simple way to remember:
  * Template Inheritance = Concept
  * extends = Tag used to implement that concept ✅


### **What is base.html?**
* base.html is a custom parent template that contains the common layout of a website, such as header, navbar, footer, and common blocks.

### **How do you load static files in templates?**
* Django me CSS, JavaScript, Images jaise static files use karne ke liye {% load static %} tag use karte hain.
* {% load static %} Django template me static template tag library ko load karne ke liye use hota hai. Iske baad hum {% static %} tag ka use karke CSS, JavaScript aur image files ke URLs generate kar sakte hain.

```python
project/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
```

#### Steps
* Step 1: Template me static tag load karo
```python
{% load static %}
```

* Step 2: Static file ko use karo
```python
# css file
<link rel="stylesheet" href="{% static 'css/style.css' %}">

# js file
<script src="{% static 'js/script.js' %}"></script>

# image file
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

* Step 3: settings.py
```python
STATIC_URL = 'static/'
```

### Difference between STATIC_URL and STATIC_ROOT?
* **STATIC_URL** browser ko static files ka **URL path** batata hai, jaise /static/.
* **STATIC_ROOT** production me collectstatic command ke baad static **files ko store karne ki final directory** hoti hai.

#### Setting
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

| Feature       | STATIC_URL               | STATIC_ROOT                          |
| ------------- | ------------------------ | ------------------------------------ |
| Purpose       | Static files ka URL path | Static files ka physical folder path |
| Used By       | Browser                  | Django `collectstatic` command       |
| Example       | `/static/`               | `/var/www/project/staticfiles/`      |
| Environment   | Development & Production | Mainly Production                    |
| Stores Files? | No                       | Yes                                  |


### Difference between static files and media files?
* **Static Files** wo files hoti hain jo developer provide karta hai, jaise CSS, JavaScript aur website images.
* **Media Files** wo files hoti hain jo **users upload karte hain, jaise profile pictures**, documents aur videos.
```python
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# structure
media/
├── profile_pics/user1.jpg
├── documents/resume.pdf
└── videos/demo.mp4

static/
├── css/style.css
├── js/script.js
└── images/logo.png
```