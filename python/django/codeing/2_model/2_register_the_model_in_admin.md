### Register the model in admin
- Go to myapp/admin.py and add:

#### Basic Registration
- Bas itna likhne se model admin me show hone lagega.
```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

```python
from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-id',)
    list_per_page = 20
    readonly_fields = ('created_at',)
```

#### Custom Admin Class (Advanced)
1. list_display
```python
list_display = ('id', 'name', 'email')
```

2. search_fields
```python
search_fields = ('name', 'email')
```

3. list_filter
- Right side me filter panel
```python
list_filter = ('is_active', 'created_at')
```

4. ordering
```python
ordering = ('-id',)
```

5. list_editable
- List view se hi edit karne ka option
```python
list_editable = ('email',)
```

6. list_per_page
- Pagination set karne ke liye
```python
list_per_page = 20
```

7. readonly_fields
- Field ko editable mat banaye
```python
readonly_fields = ('created_at',)
```

8. fields / fieldsets
- Form ka UI control karne ka
```python
fields = ('name', 'email', 'address')
```

### Header and Title change:
```python
from django.contrib import admin
from .models import Customer

admin.site.site_header = "Mohit ka Panel"
admin.site.site_title = "Mohit Admin Portal"
admin.site.index_title = "Mohit Welcome to Dashboard"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "user_name", "created_at")
    search_fields = ("first_name", "last_name", "user_name")
```