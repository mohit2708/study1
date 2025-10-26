### Swegger
1. **django-rest-swagger:** This package was one of the earlier solutions for integrating Swagger with DRF. However, it is now deprecated and not actively maintained. It's recommended to use drf-yasg or drf-spectacular instead.
2. **drf-openapi:** This package provides a way to generate OpenAPI 2.0 specifications for your DRF APIs. It is less commonly used compared to drf-yasg and drf-spectacular, but it can still be a viable option if you are looking for something lightweight.
3. **django-rest-framework-apispec:** This package integrates DRF with apispec, allowing you to generate OpenAPI specifications. It provides decorators for documenting your views and can be a good choice if you prefer using apispec for schema generation.
4. **flasgger:** While primarily designed for Flask, flasgger can be used in Django projects with some adjustments. It provides a simple way to create Swagger documentation and can be integrated with DRF, but it may require more manual setup compared to the other options.


### **Recommendation:-** 
* The best options are generally considered to be **drf-yasg** and **drf-spectacular**.
#### drf-yasg:-
* **Pros:**
  * Supports OpenAPI 2 (Swagger), which is widely used.
  * Provides a built-in Swagger UI that is easy to set up and use.
  * Allows for detailed documentation using decorators, making it straightforward to explain complex endpoints.

* **Cons:**
  * Limited to OpenAPI 2, which may not support some of the newer features available in OpenAPI 3.
  * Some manual schema definitions may be required.

#### drf-spectacular:-
* **Pros:**
  * Supports OpenAPI 3, which includes more features and flexibility than OpenAPI 2.
  * Automatically generates the schema based on your DRF views and serializers, reducing manual documentation effort.
  * Offers better support for complex types and nested serializers.
  * Provides various customization options for tailoring the generated schema.

* **Cons:**
  * The initial setup and customization may have a steeper learning curve compared to drf-yasg.



### Proceed for drf-spectacular
* First, install drf-spectacular using pip:
```python
pip install drf-spectacular
```
* Add drf_spectacular to your INSTALLED_APPS in your Django settings file (settings.py):
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_spectacular',
]
```
* You may also want to configure the REST_FRAMEWORK settings to use drf-spectacular for schema generation:
```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```
* We can do this in your main urls.py file:
```python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
```
* Run server
```python
python manage.py runserver
```
