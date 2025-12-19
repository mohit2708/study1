## Model
### Create a models folder in your app
- Inside your app
```python
myapp/
    models/
        __init__.py
        customer.py
        ....
        ....
    views/
    urls.py
    apps.py
```

### Create the Model File
- models/customer.py
```python
from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
```
- You **don't need to define the primary key**. Django auto-creates id as PK.

### Expose the model in models/__init__.py
- File: models/__init__.py
```python
from .customer import Customer
```

### Update your AppConfig
- Make sure your app has apps.py like:
```python
from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
```

### Run Migrations
```python
python manage.py makemigrations
python manage.py migrate
```

### Good Practice Notes (Straight Advice)
- Don’t store plain passwords — use Django’s built-in password hashing if customers need login.
- If this Customer is meant to be a user account, use Django’s custom User model.

### I want to custom primary key
- Option 1 (Popular): Auto-generated UUID as Primary Key
```python
import uuid
from django.db import models

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

```

- Option 2: Custom Auto-Increment Numeric PK
```python
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

```


### Register model in admin
```python
from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "user_name", "created_at")
    search_fields = ("first_name", "last_name", "user_name")

```