🚀 DJANGO ADMIN FULL CUSTOMIZATION GUIDE

Niche diye gaye saare points real industry projects me use hote hain.

1️⃣ Admin Theme / Header / Logo Change
✔ Admin title, header, and welcome text change:

admin.py

from django.contrib import admin

admin.site.site_header = "My Project Admin Panel"
admin.site.site_title = "My Admin"
admin.site.index_title = "Welcome to My Dashboard"

2️⃣ Custom Actions Add

Aap list view me custom operations add kar sakte ho — jaise “Mark Active”, “Mark Inactive”, etc.

Example

admin.py

@admin.action(description="Mark selected customers as active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Mark selected customers as inactive")
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    actions = [make_active, make_inactive]

3️⃣ CSV Export Button Add

List page me ek button aayega → selected rows ko CSV me download karo.

Code:
import csv
from django.http import HttpResponse

@admin.action(description="Export Selected Rows as CSV")
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'

    writer = csv.writer(response)
    writer.writerow([field.name for field in queryset.model._meta.fields])  # header

    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in obj._meta.fields])

    return response


Then register:

actions = [export_as_csv]

4️⃣ Custom Buttons (Extra Links / Actions)

Admin change page me top pe custom button add karna:

Step 1: Template override folder banaye:
project/
   templates/
      admin/
         customer/
            change_form.html

Step 2: Add custom button
{% extends "admin/change_form.html" %}
{% block submit_buttons_top %}
    <a href="/custom-action-url/" class="button">Custom Action</a>
    {{ block.super }}
{% endblock %}

5️⃣ Inline Model Editing (Parent-child form ek hi page par)

Example: Customer ke orders same page me edit karna.

models.py
class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)

admin.py
class OrderInline(admin.TabularInline):
    model = Order
    extra = 1   # kitne blank rows dikhe

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

6️⃣ Rich Text Editor Add (CKEditor / TinyMCE)
Install:
pip install django-ckeditor

settings.py
INSTALLED_APPS = [
    'ckeditor',
]

models.py
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()

admin.py

No change required — auto rich editor aa jayega.

7️⃣ Admin Icons, Logo, Favicon Change
Step 1: Static folder me images rakho:
static/admin/img/logo.png
static/admin/img/favicon.ico

Step 2: Override base site template

Create:

templates/admin/base_site.html

base_site.html
{% extends "admin/base_site.html" %}
{% load static %}

{% block branding %}
<div style="display:flex; align-items:center;">
  <img src="{% static 'admin/img/logo.png' %}" height="40" />
  <h1 id="site-name">My Custom Admin</h1>
</div>
{% endblock %}

8️⃣ Admin CSS / Dark Theme / Custom Styling
Step 1: settings.py
STATICFILES_DIRS = [BASE_DIR / "static"]

Step 2: admin.py
class CustomAdminSite(admin.AdminSite):
    class Media:
        css = {
            "all": ["css/admin_custom.css"],
        }

admin_custom.css
#header {
    background: #222;
}
#header h1, #header a {
    color: #fff !important;
}

9️⃣ Django Admin Dashboard Customization

Admin index page me custom charts, stats, and counts add:

Step 1: Override index.html
templates/admin/index.html

index.html
{% extends "admin/index.html" %}
{% block content %}
<h1>Dashboard</h1>
<p>Total Users: {{ user_count }}</p>
{{ block.super }}
{% endblock %}

admin.py
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

class MyAdmin(AdminSite):
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['user_count'] = User.objects.count()
        return super().index(request, extra_context)

🔟 Custom Admin Login Page (Branding)

Create:

templates/admin/login.html


Add:

{% extends "admin/login.html" %}
{% load static %}

{% block branding %}
<img src="{% static 'admin/img/logo.png' %}" height="60" />
{% endblock %}

🧨 BONUS FEATURES (Advanced)

If you want, I can provide these too:

🔥 Custom admin dashboard with charts
🔥 Export to Excel, PDF
🔥 Custom admin menu
🔥 Collapsible fieldsets
🔥 Custom form validation inside admin
🔥 Disable delete/edit buttons
🔥 Role-based admin permissions
🔥 Multi-theme admin (light/dark)

👉 Want full ready-to-use code with folder structure?

Just say:

"Give me full Django admin customization project structure + code"
======================================================================
https://chatgpt.com/share/69232a55-4aa8-800b-8c01-30fbc7e6e076