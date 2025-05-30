### Url Settings
#### Step1:-
* Add code in **project urls.py** file
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')), # authentication is a app name
    path('accounts/', include('accounts.urls')), # accounts is a app name   
]
```

#### Step2:-
* Create urls.py file in your app folder(authentication)
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('create', views.stinsert, name='create1'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete_st),
]
```