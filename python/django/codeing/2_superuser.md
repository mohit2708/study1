### **Migrate file in database**
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


### Show app in your admin
```python
=========admin.py=====
from django.contrib import admin
from blog_app.models import Post, Comment, Category
# Register your models here.
admin.site.register(Post)     //app supar admin mai show hone ke liye
admin.site.register(Comment)     //app supar admin mai show hone ke liye
admin.site.register(Category)     //app supar admin mai show hone ke liye
```

* 2nd Option
```python
from django.contrib import admin
from employeeFunctionBased.models import Employee

# Register your models here.
# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name']
	list_editable = ['last_name']				# Field Editable in the admin pannel.
	search_fields = ('last_name',)				# Serach field option in admin pannel
	list_filter = ('first_name','last_name')		# list filter in admin pannel
 
# admin.site.register(Employee,EmployeeModelAdmin) 		# instead of @admin.register(Employee)
```


```python
==============eshop project============
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer )
admin.site.register(Order )
```