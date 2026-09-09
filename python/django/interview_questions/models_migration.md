|  No.  | Django Models & Database Questions                                                              |
| :---: | ----------------------------------------------------------------------------------------------- |
|       | [What is a Model?](#what-is-a-model)                                                            |
|       | [What are Migrations](#what-are-migrations)                                                     |
|       | [Difference between makemigrations and migrate](#difference-between-makemigrations-and-migrate) |
|       | [See the all execut command?](#see-the-all-execut-command)                                      |
|       | [What is the Meta Class?](#what-is-the-meta-class)                                              |
|       | [What is ORM?](#what-is-orm)                                                                    |
|       | [What is indexes in Django?](#what-is-indexes-in-django)                                        |
|       | [How do you write raw SQL?](#how-do-you-write-raw-sql)                                          |
|       | [What is inspectdb in Django?](#what-is-inspectdb-in-django)                                    |
|       | [how to setup database in django?](#how-to-setup-database-in-django)                            |

<div style="page-break-before: always;"></div>


### 🎯**What is a Model?**
* A Django Model is a Python class that represents a database table. 
* It defines the fields and relationships of the data and allows us to interact with the database using Django ORM without writing raw SQL for most operations.

#### Where do we create a Model?
* Models are generally created inside an app's models.py:
```python
myproject/
│
├── manage.py
│
├── myproject/
│   ├── settings.py
│   └── urls.py
│
└── users/
    ├── models.py      # ← Model is created here
    ├── views.py
    └── admin.py
```
```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    description = models.TextField()             # Long text
```

* After creating the model, run:
```python
python manage.py makemigrations

# Then
python manage.py migrate
```

[Back to Top](#back-to-top)

### 🎯**What are Migrations?**
* Migrations are files that Django uses to track and apply changes made to models in the database schema.
* Whenever you create, modify, or delete a model field, Django records those changes in migration files.
```python
python manage.py makemigrations
```

### 🎯**What are migrate?**
* **migrate** applies those migration files to the database and updates the database schema.
```python
python manage.py migrate
```

### 🎯**Difference between makemigrations and migrate?**
* **makemigrations** creates migration files based on changes in Django models, while **migrate** applies those migration files to the database and updates the database schema.
* makemigrations prepares the changes; migrate executes them.

| `makemigrations`             | `migrate`                               |
| ---------------------------- | --------------------------------------- |
| Creates migration files      | Applies migration files to the database |
| Detects changes in models    | Executes SQL on the database            |
| Does not change the database | Changes the database structure          |
| Generates migration scripts  | Runs migration scripts                  |

```python
# Create/Modify a Model
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

# Step 2
python manage.py makemigrations # Run makemigrations

# Example migration file:
migrations.CreateModel(
    name='Employee',
    fields=[
        ('id', models.BigAutoField(primary_key=True)),
        ('name', models.CharField(max_length=100)),
        ('email', models.EmailField()),
    ],
)

# Run migrate
python manage.py migrate
```

### **See the all execut command?**
```python
python manage.py showmigration
```

### See the specific App command?
```python
python manage.py showmigration app_name
```

### To see the raw SQL Query
* sqlmigrate is a Django management command used to **display the SQL statements** that will be executed for a specific migration. It helps developers inspect and understand the database changes before applying the migration.
* Django में sqlmigrate एक command है जो बताती है कि किसी migration को apply करने पर Django कौन-सी SQL query database में execute करेगा।
```python
python manage.py sqlmigrate app_name migration_name
```



### 🎯**What is the Meta Class?**
* The Meta class is an **inner class inside a Django model** that is used to **provide metadata (extra configuration) about the model**.
* It does not create database fields. Instead, it controls how Django behaves with the model.
* **HINDI:-** Meta class model ki additional configuration define karne ke liye use hoti hai. Isme db_table, ordering, verbose_name, unique_together, indexes, constraints, permissions jaise options define kiye ja sakte hain.
```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = "employees"
```

#### Common Uses of Meta
1. Specify a **custom table name**.
```python
class Meta:
    db_table = "employees"

# appname_employee
```

2. ordering
* - (minus sign) lagane se descending order ho jata hai.
* for Ascending Order (A → Z)
```python
class Meta:
    ordering = ['name']
```
* for Descending Order (Z → A)
```python
class Meta:
    ordering = ['-name']
```

* ISI trahe se bahute sare hai
```python
from django.db import models
from django.db.models import Q

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "employees"
        ordering = ["name"]
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        unique_together = ['name', 'email']
        get_latest_by = "id"
        indexes = [
            models.Index(fields=["email"]),
        ]
        constraints = [
            models.CheckConstraint(
                condition=Q(salary__gte=0),
                name="salary_positive"
            )
        ]
```
| Option                | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `db_table`            | Custom table name                         |
| `ordering`            | Default sorting                           |
| `verbose_name`        | Singular name in Admin                    |
| `verbose_name_plural` | Plural name in Admin                      |
| `unique_together`     | Multiple fields unique                    |
| `indexes`             | Database indexes                          |
| `constraints`         | Custom DB constraints                     |
| `permissions`         | Custom permissions                        |
| `default_permissions` | Add/remove default permissions            |
| `managed`             | Whether Django manages the table          |
| `abstract`            | Create abstract base model                |
| `proxy`               | Create proxy model                        |
| `app_label`           | Assign model to an app manually           |
| `get_latest_by`       | Latest object field                       |
| `db_table_comment`    | Add table comment (newer Django versions) |


### 🎯**What is ORM?**
* ORM (Object Relational Mapping) is a technique that allows us to interact with a database using Python objects and methods instead of writing SQL queries directly.
* Django provides a built-in ORM called Django ORM.

#### Advantages of ORM
* No need to write SQL for common operations.
* Database-independent (MySQL, PostgreSQL, SQLite, etc.).
* Faster development.
* More readable and maintainable code.
* Helps prevent SQL injection in normal ORM usage.

#### Example
1. Get Data
```python
employees = Employee.objects.all()
Employee.objects.get(id=1)
Employee.objects.filter(name="Mohit")
```

2. Create
```python
Employee.objects.create(
    name="Mohit",
    email="mohit@gmail.com"
)
```

3. Read
```python
Employee.objects.all()
Employee.objects.get(id=1)
Employee.objects.filter(name="Mohit")
```

4. Update
```python
emp = Employee.objects.get(id=1)
emp.name = "Rahul"
emp.save()
```
5. Delete
```python
emp = Employee.objects.get(id=1)
emp.delete()
```

### 🎯**What is indexes in Django?**
* Django mein database index add karne ke liye mainly Meta class ke andar indexes option use karte hain.
* Index ka purpose database queries ko faster banana hota hai, especially jab kisi column par frequently filter(), order_by() ya lookup kiya jata hai.

1. Single-field Index
```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields=['email']),
        ]
# Yahan email column par index create hoga.
```
* Single field ke liye directly:
```python
email = models.EmailField(db_index=True)
```

2. Multiple Indexes
```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['department']),
        ]
```

3. Composite Index
```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['department', 'salary']),
        ]
```

4. Index ko Custom Name dena
```python
class Meta:
    indexes = [
        models.Index(
            fields=['email'],
            name='employee_email_idx'
        ),
    ]
```

### 🎯**db_index=True vs Meta.indexes**
| `db_index=True`                            | `Meta.indexes`                          |
| ------------------------------------------ | --------------------------------------- |
| Simple single-field index                  | More flexible                           |
| Field ke andar define hota hai             | `Meta` ke andar define hota hai         |
| `email = models.EmailField(db_index=True)` | `models.Index(fields=['email'])`        |
| Basic use case                             | Composite/custom indexes ke liye useful |

### 🎯**How do you write raw SQL?**
* Django normally ORM use karta hai, lekin jab complex query ho ya ORM se query likhna convenient na ho, tab raw SQL use kar sakte hain.
* Django mein raw SQL execute karne ke mainly 3 common ways hain.
1. **Model.objects.raw()**
```python
employees = Employee.objects.raw(
    "SELECT * FROM employees WHERE salary > %s",
    [50000]
)

for employee in employees:
    print(employee.name)
```

2. **connection.cursor()**
* Agar INSERT, UPDATE, DELETE ya koi arbitrary SQL execute karna hai:
```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "UPDATE employees SET salary = %s WHERE id = %s",
        [60000, 1]
    )

# Example select
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT id, name FROM employees WHERE salary > %s",
        [50000]
    )

    rows = cursor.fetchall()

for row in rows:
    print(row)
```

3. RawSQL
* Django ke queryset ke andar custom SQL expression use karna ho to RawSQL use kar sakte hain:
```python
from django.db.models.expressions import RawSQL

employees = Employee.objects.annotate(
    custom_value=RawSQL(
        "salary * 2",
        []
    )
)
```

### **What is inspectdb in Django?**
* **inspectdb** is a Django management command that examines an existing database schema and automatically generates Django model code for the database tables. It is mainly used when integrating Django with a legacy or already existing database.
* **Hindi:-** inspectdb Django का एक management command है जो existing database tables से Django models automatically generate करता है।
```python
# 👉 Output screen पर दिखेगा।
python manage.py inspectdb

# 👉 Output models.py में लिख दिया जाएगा।
python manage.py inspectdb > models.py

# Only one table
python manage.py inspectdb employee
python manage.py inspectdb employee department role > models.py
```

### **how to setup database in django?**
* In Django, database setup mainly means configuring the database in **settings.py**, installing the required database driver, and then running migrations.

1. Default SQLite database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

2. MySQL database setup
* If you want to use MySQL, first install the driver:
```python
pip install mysqlclient
```
* Create a database in MySQL: CREATE DATABASE db_name;
* Then configure settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### Difference between CharField and TextField?
* **CharField** is used for storing small strings and requires max_length, such as names, titles, and emails.
* **TextField** is used for storing large amounts of text like descriptions, comments, and blog content, and it does not require max_length.

```python
# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)      # Short text
    description = models.TextField()             # Long text
```

### **What is ForeignKey?**
* ForeignKey is used to create a Many-to-One relationship between two models.
* 👉 It means many records of one table can be related to one record of another table.
```python
# models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
```
