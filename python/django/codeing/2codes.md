

### Models
#### Excute migrations
```python
python manage.py makemigrations <app_name>
python manage.py migrate <app_name>
```

#### All fileds in model
```python
from django.db import models
# Create your models here.
class Crudst(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100, blank=False)
    username = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    image = models.FilePathField(path="/img") #for image, file, any type of file.
    image = models.ImageField(upload_to='uploads/products/') # only for image
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    
    active = models.BooleanField(default=True)  # can login
    date_joined = models.DateTimeField(auto_now_add=True)    
    stmobile = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):      
        return self.name	#django admin mai admin frount mai name sa list show hogi 

    def __str__(self):
    	return f"Product ({self.pk}): {self.name}"  #  __str__() method is overridden to return a string representation of the Product object.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        return self.title	# django admin mai admin frount mai title sa list show hogi

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)    
    
    
    def __str__(self):
        return self.author
```

#### How to create model Integrate if Existing DBs in your database?
```python
python manage.py inspectdb > blog_app/models.py
```




#### Get Product from the model query
```python
================in model.py=========
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')


    def __str__(self):
    	return f"Product ({self.pk}): {self.name}"

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();
			
========call in view file ================
from storeApp.models.product import Product

def Index(request):
    # return HttpResponse('first page')
    prod = Product.get_all_products();
    return render(request, 'index.html',{'product':prod})
	
=====in html file=========
{{product}}
```


### Serial number incremant in for loop
```python
<ul>
  {% for item in items %}
    <li>S.N. {{ forloop.counter|add:10 }}: {{ item }}</li>
  {% endfor %}
</ul>
```
```python
<ul>
  {% with counter=10 %}
    {% for item in items %}
      {% with counter=counter|add:1 %}
        <li>S.N. {{ counter }}: {{ item }}</li>
      {% endwith %}
    {% endfor %}
  {% endwith %}
</ul>
```


### Get the value from the query string
```python
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
from storeApp.models.product import Product
from storeApp.models.category import Category

# Create your views here.
def Index(request):
    # return HttpResponse('first page')
    prod = None	
    categoryID = request.GET.get('category') 	# get the value from the query string.
    categories = Category.get_all_categories()	# Get all the category.

    if categoryID:
        prod = Product.get_all_products_by_categoryid(categoryID)		# Get all the category by ID
    else:
        prod = Product.get_all_products();		# Get all the Product.
    

    data = {'product':prod,'categorie':categories}

    return render(request, 'index.html',data)
```

### Value already fill in the form after the form error and password hashing.
* view.py
```python
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
from storeApp.models.customer import Customer
from django.contrib.auth.hashers import make_password   # when we password hasing

# Create your views here.
def signUp(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	else:
		first_name 	= request.POST['firstname'].strip()   # Strip for reomve the white spaces
		last_name 	= request.POST['lastname']
		phone 		= request.POST['phone']
		email 		= request.POST['email'].strip()
		password	= request.POST['password'].strip()

		# agar error aati hai to jo field bhare the wo bhare rahe.
		# value ko html mai call karenge ya context mai bhaj kar
		value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
		# Validations
		error_messages = {}

		if not first_name:
			error_messages['first_name'] = "First name is required!"
		elif len(first_name) < 4:
			error_messages['first_name'] = "First name must be 4 characters or longer"

		if not last_name:
			error_messages['last_name'] = "Last name is required!"
		if not email:
			error_messages['email'] = "Email is required!"
		if Customer.objects.filter(email=email).exists():
			error_messages['email'] = "Email is already exist!"
		if not password:
			error_messages['password'] = "Password is required!"
		if not phone:
			error_messages['phone'] = "Phone number is required!"
		
		# Agar koi error message nahi hai to data save ho jayega
		if not error_messages:
			customer 	= Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=make_password(password))
			customer.save()
			# Home page par call kara diya url mai se
			return redirect('home_page')
		# other wise error message show hoga
		else:
			context = {'error':error_messages,'values':value}
			return render(request, 'signup.html', context)
```
* html form
```python
<form action="/signup" method="POST">
                
{% csrf_token %}

<div class="form-group">
    <label for="">First Name</label>
    <input type="text" name="firstname"
      id="" value="{{values.first_name}}" class="form-control form-control-sm" 
      placeholder="">
      {% if error.first_name %}
        <p style="color: red;">{{ error.first_name }}</p>
    {% endif %}
</div>

<div class="form-group">
    <label for="">Last Name</label>
    <input type="text" name="lastname" 
    id="" value="{{values.last_name}}" class="form-control form-control-sm"
    >
    {% if error.last_name %}
        <p style="color: red;">{{ error.last_name }}</p>
    {% endif %}
</div>
<input class="btn btn-sm btn-info" type="submit" value="Create An Account ">
</form>
```