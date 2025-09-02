### models.py
```python
from django.db import models

# Create your models here.
class Resume(models.Model):

	STATE_CHOICE = (
		('Assam','Assam'),
		('Goa','Goa'),
	)

	name = models.CharField(max_length=100)
	dob = models.DateField(auto_now=False, auto_now_add=False,blank=True)
	gender = models.CharField(max_length=100)
	email = models.EmailField()
	locality = models.CharField(max_length=100)
	pin = models.PositiveIntegerField()
	state = models.CharField(choices=STATE_CHOICE, max_length=50)
	city = models.CharField(max_length=100)
	job_city = models.CharField(max_length=50)
	profile_image = models.ImageField(upload_to='profileimg/', blank=True)
	my_file = models.FileField(upload_to='doc', blank=True)
```

### urls.py
```python
from django.contrib import admin  
from django.urls import path  
from resumeuploder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('',views.HomeView.as_view(), name='homeview'),
    path('<int:pk>',views.EmployeeListView.as_view(), name='employee_list'),

] 
```

### Create forms.py in your app
```python
from django import forms
from .models import Resume

GENDER_CHOICES = [
('Male','Male'),
('Female','Female')
]

JOB_CITY_CHOICES = [
('Delhi','Delhi'),
('Puna','Puna'),
('Rachi','Rachi'),
('Mumbai','Mumbai'),
('Banglore','Banglore'),
]
# categories = [] #forms.ModelChoiceField(queryset=ArticleCategory.objects.all().order_by('name'))
# category = forms.ModelChoiceField(queryset=ArticleCategory.objects.all().order_by('name'),
                       # widget= the widget you want to use)

class ResumeForm(forms.ModelForm):
	# gender = forms.ChoiceField(choices=GENDER_CHOICES, widget = forms.RadioSelect)		# Gender show in form 1 option
	job_city = forms.MultipleChoiceField(label= 'Prefeered Job Locations',choices=JOB_CITY_CHOICES, widget = forms.CheckboxSelectMultiple)

	class Meta:
		model = Resume
		# add field in form
		fields = ['name', 'dob', 'gender','email','locality','pin','state','city','job_city','profile_image','my_file']
		# Reaname field in form when we calling in {{form}} in html file
		labels = {'name':'Full Name','dob':'Date Of Birth','gender':'Gender','locality':'Locality',
		'pin':'Pin Code'}
		# add activity in form field just like class and other things
		widgets = {
			'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Full Name'}),
			'dob':forms.TextInput(attrs={'class':'form-control','id':'datepicker'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control input'}),	# Gender show in form 1 option		
			'locality':forms.TextInput(attrs={'class':'form-control'}),
			'pin':forms.TextInput(attrs={'class':'form-control'}),
			'state': forms.Select(attrs={'class': 'form-control input'}),
			'city':forms.TextInput(attrs={'class':'form-control'}),
			'job_city':forms.TextInput(attrs={'class':'form-control'}),
			# 'profile_image':forms.TextInput(attrs={'class':'form-control'}),
			# 'my_file':forms.TextInput(attrs={'class':'form-control'}),
		}
```

### views.py
```python
from django.shortcuts import render
from .forms import ResumeForm
from . models import Resume
from django.views import View
# Create your views here.

class HomeView(View):
	def get(self, request):
		form = ResumeForm()
		getDataOfEmp = Resume.objects.all()
		print(getDataOfEmp)
		return render(request,'resume/home.html', {'form':form,'getDataOfEmp':getDataOfEmp})

	def post(self, request):
		form = ResumeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'resume/home.html', {'form':form})

class EmployeeListView(View):
	def get(self, request, pk):
		print(pk)
		viewDataOfEmp = Resume.objects.get(pk=pk)
		return render(request, 'resume/emp_list.html',{'viewDataOfEmp':viewDataOfEmp})
```

### home.html
```python
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
  <title>Resume</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>

    <link rel="stylesheet" href="//code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css">
  <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
  <script src="https://code.jquery.com/ui/1.13.2/jquery-ui.js"></script>
</head>
<body>
<style type="text/css">
	
</style>
<div class="container">
  <h2>Resume</h2>
  <form action="" method="post" enctype="multipart/form-data">
  	{% csrf_token %}
  	{{form|a}}
  	<!-- as_p ka mtb as a peragraph -->
  	<div class="row">
  		<div class="col-sm-6">
			<div class="form-group">
			  <label>Full Name:</label>
			  {{form.name}}
			  {{ form.name.errors }}
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group">
			  <label>Gender:</label>
			  {{form.gender}}
			</div>
		</div>
	</div>

	<div class="row">
  		<div class="col-sm-6">
			<div class="form-group">
			  <label>Date Of Birth:</label>
			  {{form.dob}}
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group">
			  <label>Email:</label>
			  {{form.email}}
			</div>
		</div>
	</div>

	<div class="row">
  		<div class="col-sm-6">
			<div class="form-group">
			  <label>Locality:</label>
			  {{form.locality}}
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group">
			  <label>Pin Code:</label>
			  {{form.pin}}
			</div>
		</div>
	</div>

	<div class="row">
  		<div class="col-sm-6">
			<div class="form-group">
			  <label>state:</label>
			  {{form.state}}
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group">
			  <label>city:</label>
			  {{form.city}}
			</div>
		</div>
	</div>

	<div class="row">
  		<div class="col-sm-6">
			<div class="form-group">
			  <label>Job City:</label>
			  {{form.job_city}}
			</div>
		</div>
		<div class="col-sm-6">
			<div class="form-group">
			  <label>Profile Image:</label>
			  {{form.profile_image}}
			</div>
		</div>
	</div>

	<div class="row">
  		<div class="col-sm-6">
			<div class="form-group">
			  <label>My File:</label>
			  {{form.my_file}}
			</div>
		</div>

	</div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>

<h1>Employee Details</h1>
{% for emp in getDataOfEmp %}
{{emp.id}} 
{{emp.name}} : <a href="{% url 'employee_list' emp.id  %}">{{emp.name}} </a>
<hr>
{%  endfor %}
</div>
 <script>
  $( function() {
    $( "#datepicker" ).datepicker();
  } );
  </script>
</body>
</html>
```

### Empl_list.html
```python
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Resume</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container">
<h1>Employee Details</h1>
<p>Application No. {{viewDataOfEmp.id}}</p>
<p>Name. {{viewDataOfEmp.name}}</p>
<p>Date Of Birth. {{viewDataOfEmp.dof}}</p>
<p>Gender:- {{viewDataOfEmp.gender}}</p>
<p>Address:- {{viewDataOfEmp.location}}</p>
<p>City:- {{viewDataOfEmp.city}}</p>
<p>Job City:- {{viewDataOfEmp.job_city}}</p>
<img src="{{viewDataOfEmp.profile_image.url}}" width="150" height="150">
<p>attachment:- <a href="{{viewDataOfEmp.my_file.url}}">Download File</a></p>
</div>
</body>
</html>
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
    path('crud_function/', include('crud_function.urls')),
    path('crud_class/', include('crud_class.urls')),
    path('blog', include("blog.urls")),
    path('crud_classbased', include("crud_classbased.urls")),
    path('resume/', include('resumeuploder.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     # add this line

```

### setting.py
```python
import os


STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') 
```
