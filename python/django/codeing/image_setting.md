### model.py
```python

```

### main urls.py project ki
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings					# add this line
from django.conf.urls.static import static        # add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('crud_classbased', include("crud_classbased.urls")),
    path('resume/', include('resumeuploder.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     # add this line

### setting.py
```python
import os

STATIC_URL = 'static/'
MEDIA_URL = '/media/'                           # If required
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
```

### Html page
```python
<form method="post" action="{% url 'store' %}" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="col-sm-6">
      <label>Image</label>
      <input type="file" class="form-control" name="pimage" id="pimage">
    </div>

    <button type="submit" class="btn btn-default">Submit</button>
</form>
```