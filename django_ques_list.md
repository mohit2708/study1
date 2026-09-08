# 🎯 Python Django Questions

### 🧠 [**Dajngo project setup**](/python/django/interview_questions/django_project_setup.md)
1. [Virtual Environment](/python/virtual_env.md)
2. Django install karo
3. [Django project create karo](/python/django/interview_questions/django_project_setup.md#django-project-create-karo)
4. Server run karo
5. App create karo
6. App ko settings.py mein add karo
7. First View banao
8. URL seeting
9. Database migrations
10. Admin user banao


### 🧠 [**Django Basic Questions**](/python/django/interview_questions/3_django.md)
1. [What is **Django**?](/python/django/interview_questions/3_django.md#-what-is-django)
2. ⭐ [How to install Django?](/python/django/interview_questions/django_project_setup.md)
3. ⭐ How to check django latest version?
4. How to check installed packages?
5. Django:- Latest version
6. Why is Django Used/Key Features?
7. Django Architecture (MVT)
8. ⭐ [What is MTV architecture?](/python/django/interview_questions/3_django.md#what-is-mtv-architecture)
9. ⭐ [Create a Django Project?](/python/django/interview_questions/3_django.md#create-a-django-project)
10. [Django Project Structure](/python/django/interview_questions/3_django.md#django-project-structure)
    1.  [what is manage.py?](/python/django/interview_questions/3_django.md#1-managepy)
12. [What is Django Apps?](/python/django/interview_questions/3_django.md#django-apps)
    1.  ⭐ [How to Create app?](/python/django/interview_questions/3_django.md#creating-an-app)
14. ⭐ [Project vs App](/python/django/interview_questions/3_django.md#project-vs-app)
15. ⭐ [How to run server?](/python/django/interview_questions/3_django.md#how-to-run-server)
16. [Why is Django called a "loosely coupled" framework?](/python/django/interview_questions/3_django.md#why-is-django-called-a-loosely-coupled-framework)
17. [What are the advantages of Django?](/python/django/interview_questions/3_django.md#what-are-the-advantages-of-django)
18. Difference between MVT and MVC? - no
19. Why is Django called a "batteries-included" framework? - no
20. What are Django settings? - no

### 🧠 [**Django SuperUser Questions**](/python/django/interview_questions/models_migration.md)
1. [How to create superuser?](/python/django/interview_questions/superuser.md#how-to-create-superuser)
<div style="page-break-before: always;"></div>

### 🧠 [**Django Models & Migrations Questions**](/python/django/interview_questions/models_migration.md)
1. [What is a Model?](/python/django/interview_questions/models_migration.md#what-is-a-model)
2. ⭐ [What are Migrations?](/python/django/interview_questions/models_migration.md#what-are-migrations)
3. ⭐ [What are Migrate?](/python/django/interview_questions/models_migration.md#what-are-migrate)
4. [Difference between makemigrations and migrate?](/python/django/interview_questions/models_migration.md#difference-between-makemigrations-and-migrate)
5. [See the all execut command?](/python/django/interview_questions/models_migration.md#see-the-all-execut-command)
6. See the specific App command?
7. [To see the raw SQL Query](/python/django/interview_questions/models_migration.md#to-see-the-raw-sql-query)
8. What is the Meta Class?
9. ⭐ [What is ORM?](/python/django/interview_questions/models_migration.md#what-is-orm)
10. [Advantages of Django ORM?](/python/django/interview_questions/models_migration.md#advantages-of-orm)
11. [How do you write raw SQL?](/python/django/interview_questions/models_migration.md#how-do-you-write-raw-sql)
12. What is indexes in Django?
13. ⭐ What is inspectdb in Django?
14. [how to setup database in django?](/python/django/interview_questions/models_migration.md#how-to-setup-database-in-django)
15. [What is Redis?](/database/Redis/Redis.md#what-is-redis)


Difference between CharField and TextField?
What is ForeignKey?
What is OneToOneField?
What is ManyToManyField?
What is on_delete?
What is Meta class?
What is __str__() method?
How do you add indexes in Django?
What is a custom model manager?



### 🧠 [**Django Views Questions**](/python/django/interview_questions/view.md)
1. [What is a View?](/python/django/interview_questions/view.md#what-is-a-view)
2. [Types of Views?](/python/django/interview_questions/view.md#types-of-views)
   1. Function-Based View (FBV)
   2. Class-Based View (CBV)
3. [Function Based View (FBV) vs Class Based View (CBV)?](/python/django/interview_questions/view.md#difference-between-fbv-and-cbv)
4. [Advantages of CBV?](/python/django/interview_questions/view.md#advantages-of-cbv-class-based-views)
5. What is Generic View?
6. What is APIView?
7. What is TemplateView?
8. What is ListView?
9.  What is DetailView?
10. What is CreateView?
11. What is UpdateView?
12. What is DeleteView?
13. What is Mixin?
14. How to view **all items** in a Model using Django QuerySet?
15. How to **Filter Items** in Django QuerySet?
16. How to **get a particular item** in Django?
17. ⭐ Difference between **get()** and **filter()** in Django?
18. [How to **insert**, **update** and **delete** object using queryset?](/python/django/interview_questions/view.md#how-to-insert-update-and-delete-object-using-queryset)


   

### [URLs & Routing](/python/django/interview_questions/URLs_Routing.md)
1. What is URL Routing in Django?
2. Difference between path() and re_path()?
3. What is URL namespace?
4. What is include()?
5. How do you pass parameters in URLs?
6. What is URL reversing?
7. What is reverse()?

Example:

path('user/<int:id>/', views.user)

### 🧠 [**Django Templates Questions**](/python/django/interview_questions/Templates.md)
1. [What is Django Template Engine?](/python/django/interview_questions/Templates.md#what-is-django-template-engine)
2. Difference between {{ }} and {% %}?
3. What are template tags?
4. What are filters?
5. How do you extend templates?
6. What is template inheritance?
7. What is base.html?
8. no
9. What is context in Django templates?
10. How do you pass data from a view to a template?
11. What is the difference between Template Tags and Template Filters?
12. What is {% include %} in Django?
13. What is {% block %} in Django templates?
14. What is {% extends %} vs {% include %}?
15. What is {% csrf_token %} and why is it used?
16. How do you use if-else conditions in templates?
17. How do you use for loops in Django templates?
18. How do you handle empty querysets/lists in templates?
19. What is {% empty %} in a for loop?
20. How do you generate URLs in Django templates?
21. What is the {% url %} tag?
22. How do you load static files in Django templates?
23. What is {% load static %}?
24. How do you add CSS and JavaScript files to a Django template?
25. What is the difference between static files and media files?
26. What is {% with %} tag?
27. What is {% comment %} tag?
28. How do you write comments in Django templates?
29. What are built-in template filters in Django?
30. Can we create custom template filters? How?
31. Can we create custom template tags? How?
32. What is safe filter?
33. What is default filter?
34. What is truncatechars filter?
35. What is date filter?
36. What is length filter?
37. How do you display model data in a template?
38. How do you access related model objects in a template?
39. How do you display images uploaded by users?
40. What happens if a template variable does not exist?
41. How do you configure the Django template directory?
42. What is TEMPLATES setting in settings.py?
43. What is DIRS in the TEMPLATES configuration?
44. What is APP_DIRS?
45. What is the difference between Django Templates and Jinja2?
46. How does Django Template Engine prevent XSS attacks?
```python
Django Template Engine
base.html
{% extends %}
{% block %}
{% include %}
Context
Passing data from View → Template
{% csrf_token %}
{% url %}
{% load static %}
Custom Template Tags & Filters
```



### 🧠 [Forms](/python/django/interview_questions/Forms.md)
1. [What are Django Forms?](/python/django/interview_questions/Forms.md#what-are-django-forms)
Difference between Form and ModelForm?
What is form validation?
What are clean methods?
What is CSRF protection?
Why use {% csrf_token %}?

Example:

<form method="post">
{% csrf_token %}
</form>


7. Authentication & Authorization
Authentication vs Authorization?
What is Django Authentication System?
How do you create a user?
What is authenticate()?
What is login()?
What is logout()?
What is User model?
What are Permissions?
What are Groups?
How do you create a Custom User Model?
What is AbstractUser?
What is AbstractBaseUser?
What is login_required?
Frequently Asked

1. Middleware
What is Middleware?
Django request-response cycle?
Built-in middleware examples?
How do you create custom middleware?
What is SessionMiddleware?
What is AuthenticationMiddleware?
What is CSRF Middleware?
Interview Answer

Middleware request aur response ke beech execute hone wala layer hota hai jo processing karta hai.

9. Sessions & Cookies
What are Sessions?
What are Cookies?
Session vs Cookie?
How does Django store sessions?
What is request.session?

10. Django REST Framework (DRF)
What is DRF?
Why use DRF?
What is Serializer?
ModelSerializer vs Serializer?
What is APIView?
What is ViewSet?
What is Router?
What is Pagination?
What is Filtering?
What is Throttling?
What is Authentication?
JWT Authentication?
Token Authentication?
Session Authentication?
What is Permission Class?
Difference between PUT and PATCH?
What is Swagger?
Most Asked

Serializer
Python Object ⇄ JSON Conversion

11. Caching
What is Caching?
Why use caching?
What cache backends are supported?
What is Redis Cache?
What is Memcached?
How do you cache views?

### 🧠 [**Django Signals Questions**](/python/django/interview_questions/Signals.md)
1. [What are Django Signals?](/python/django/interview_questions/Signals.md#what-are-django-signals)
2. Why use signals?
3. Signal vs overriding save()? - no


### 🧠 [**Django Security**](/python/django/interview_questions/Security.md)
1. [What is CSRF?](/python/django/interview_questions/Security.md#-what-is-csrf-cross-site-request-forgery)
2. [What is XSS?](/python/django/interview_questions/Security.md#-what-is-xss-cross-site-scripting)
3. [CSRF VS XSS](/python/django/interview_questions/Security.md#-csrf-vs-xss)
4. [What is SQL Injection?](/python/django/interview_questions/Security.md#-what-is-sql-injection)
   1. How does Django prevent SQL Injection?
5. [What is Clickjacking?](/python/django/interview_questions/Security.md#-what-is-clickjacking)
6. [What is Security Middleware?](/python/django/interview_questions/Security.md#-what-is-security-middleware)
   

7.  Deployment
How do you deploy Django?
What is WSGI?
What is ASGI?
Gunicorn vs Uvicorn?
Nginx role?
How do you serve static files?
Difference between Development and Production?

1.  Advanced Django
What is QuerySet?
What is Lazy Loading?
What is select_related()?
What is prefetch_related()?
Difference between select_related and prefetch_related?
What is Custom Manager?
What is Context Processor?
What is Celery?

What is Django Channels?
What is WebSocket?
What is ASGI?
Very Important Interview Question

select_related()

Used for ForeignKey and OneToOne.
Performs SQL JOIN.

prefetch_related()

Used for ManyToMany and Reverse FK.
Performs separate query and joins in Python.
Top 20 Django Interview Questions (Must Prepare)
What is Django?
Explain MVT Architecture.
What is ORM?
What are migrations?
Difference between FBV and CBV?
What is Middleware?
Authentication vs Authorization?
What is CSRF?
What is Serializer in DRF?
APIView vs ViewSet?
What is JWT?
Difference between PUT and PATCH?
What is Throttling?
What is Pagination?
What is Signals?
What is QuerySet?
select_related vs prefetch_related?
What is WSGI and ASGI?
How does Django prevent SQL Injection?
Explain Django request lifecycle.

Ye 20 questions almost har Django interview (2–8 years experience) me pooche ja sakte hain.