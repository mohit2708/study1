### Create virtual enviroment
```python
python -m venv virtual-name
```

### **Activated virtual enviroment**
```pyhton
cd virtual-name\Scripts
d:\mohit\virtual-name\Scripts> activate
```

### Install django
```python
<virtual-name> d:\mohit> python -m pip install django
OR
pip install django
```

### Create project
```python
django-admin startproject projectName .
```

### Create App
```python

python manage.py startapp app_name
OR
django-admin startapp app_name

====project ki settings.py mai appn_ame add kar denge======
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app_name>',               # add app
]

====project ki settings.py mai template add kar denge======
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],      # add
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Migrate file in database
```python
 python manage.py migrate
```

### main Urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings					# add this line for image
from django.conf.urls.static import static        	# add this line for image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('storeApp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	# add this line for image
```

### app urls,py
```python
from django.contrib import admin
from django.urls import path
# from . import views
from .views import home
from .views import signup
from .views import login

# from .views.cart import Cart
# from .views.checkout import CheckOut
# from .views.orders import OrderView
# from .middlewares.auth import  auth_middleware


urlpatterns = [
    # path('', views.Index, name='home1'),
    path('', home.Index, name='home_page'),
    path('signup', signup.signUp, name='sign_up'),
    path('login', login.login, name='login'),
    # path('logout', logout , name='logout'),
    # path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    # path('check-out', CheckOut.as_view() , name='checkout'),
    # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
```


### Create the Model
* Create the models folder in my app
* create the __init__.py file
```python
from .product import Product
from .category import Category
from  .customer import  Customer
from  .orders import  Order
```
* and create the product.py file
```python
from django.db import models
from .category import Category


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
        return Product.objects.filter(id_in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();
```
* Create category.py file
```python
from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
    	return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
```
* Create the Customer.py file under the model folder
```python
from django.db import  models
from django.utils.timezone import now

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False
```


### SignUp 
* Create the view file "signup.py"
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
* html form under the template folder.
```python
{% extends 'base.html' %}
{% block content %}
<div class="container mt-4">
    <div class="p-4 m-4">
        <div class="col-lg-5 rounded mx-auto border pt-4">
            <div class="text-center col">
                <img 
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Shopping_cart_with_food_clip_art_2.svg/307px-Shopping_cart_with_food_clip_art_2.svg.png" alt=""
                class="" style="height: 150px;">
            <!-- <hr> -->
            <div class="display-8">Create An Account</div>
            <hr>
            </div>
            <h3 hidden class="alert alert-light border rounded">Create An Account</h3>
            <!-- {{error}} -->
            <form action="/signup" method="POST">
                
                {% csrf_token %}

                
                <!-- firstname -->
                <div class="form-group">
                    <label for="">First Name</label>
                    <input type="text" name="firstname"
                     id="" value="{{values.first_name}}" class="form-control form-control-sm" 
                     placeholder="">
                     {% if error.first_name %}
                        <p style="color: red;">{{ error.first_name }}</p>
                    {% endif %}
                </div>

                <!-- last name -->
                <div class="form-group">
                    <label for="">Last Name</label>
                    <input type="text" name="lastname" 
                    id="" value="{{values.last_name}}" class="form-control form-control-sm"
                    >
                    {% if error.last_name %}
                        <p style="color: red;">{{ error.last_name }}</p>
                    {% endif %}
                </div>

                <!-- phone -->
                <div class="form-group">
                    <label for="">Phone</label>
                    <input type="text" name="phone" 
                    id="" class="form-control form-control-sm"
                    value="{{values.phone}}"
                    placeholder="565698959"
                    >
                    {% if error.phone %}
                        <p style="color: red;">{{ error.phone }}</p>
                    {% endif %}
                </div>
                <!-- email -->
                <div class="form-group">
                    <label for="">Email</label>
                    <input required type="email" name="email" id=""
                    value="{{values.email}}" 
                    class=" form-control-sm form-control" placeholder="example@gmail.com">
                    {% if error.email %}
                        <p style="color: red;">{{ error.email }}</p>
                    {% endif %}
                </div>


                <!-- password -->
                <div class="form-group">
                    <label for="">Password</label>
                    <input type="password" 
                    name="password" 
                    id=""
                     class="form-control form-control-sm" placeholder="********">
                     {% if error.password %}
                        <p style="color: red;">{{ error.password }}</p>
                    {% endif %}
                </div>

                <hr>
                <div class="form-group">
                    <input class="btn btn-sm btn-info" type="submit" value="Create An Account ">
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

### Login
* login.py file under the view folder
```python
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from storeApp.models.customer import Customer
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email 		= request.POST['email'].strip()
        password	= request.POST['password'].strip()

        try:
            get_cusomerData_by_email = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            error_message = 'Email or Password invalid !!'
            return render(request, 'login.html', {'error': error_message})

        flag = check_password(password, get_cusomerData_by_email.password)

        if flag:
            return redirect('home_page')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, 'login.html', {'error': error_message})

```
* Create the file for login.html in template folder
```python
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <div class="p-4 m-4">
        <div class="col-lg-4 mt-4 border mb-4 mx-auto rounded pt-4">
            <div class="text-center col">
            
                <img 
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Shopping_cart_with_food_clip_art_2.svg/307px-Shopping_cart_with_food_clip_art_2.svg.png" alt=""
                class="" style="height: 150px;">
            <!-- <hr> -->
            <div class="display-8">Create An Account</div>
            <hr>
            </div>
            <h3 hidden class="alert alert-light border mt-4 mb-4 rounded">Login Here</h3>
            <form action="/login" method="POST">
                {% csrf_token %}
                {% if error%}
                <div class="alert alert-danger" role="alert">
                    {{error}}
                </div>
                {% endif %}
                <!-- email -->
                <div class="form-group">
                    <label for="">Email</label>
                    <input required type="email" name="email" id=""
                    value="{{values.email}}" 
                    class=" form-control-sm form-control" placeholder="example@gmail.com">
                </div>
                <!-- password -->
                <div class="form-group">
                    <label for="">Password</label>
                    <input type="password" 
                    name="password" 
                    id=""
                     class="form-control form-control-sm" placeholder="********">
                </div>

                <hr>
                <div class="form-group">
                    <input class="btn btn-sm btn-info col-lg-4" type="submit" value="Login">
                </div>
            </form>
        </div>
    </div>
</div>

{% endblock %}
```

### Login function based convert to class based
```python
from django.views import View  # Add this line

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            error_message = 'Email or Password invalid !!'
            return render(request, 'login.html', {'error': error_message})

        flag = check_password(password, customer.password)

        if flag:
            return redirect('home_page')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, 'login.html', {'error': error_message})
```
```python
from storeApp.views.login import LoginView 

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),   
]
```
### signup function based convert to class based
```python
from django.views import View

# Create your views here.



class SignUpView(View):
	def get(self, request):
		return render(request, 'signup.html')


	def post(self, request):
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
```python
from storeApp.views.signup import SignUpView

urlpatterns = [
    # path('signup', signup.signUp, name='sign_up'),
    path('signup', SignUpView.as_view(), name='sign_up'),
]
```

### Home page 
* create home.py file in view folder
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
        prod = Product.get_all_products_by_categoryid(categoryID)		# # Get all the category by ID
    else:
        prod = Product.get_all_products();		# Get all the Product.
    

    data = {'product':prod,'categorie':categories}

    return render(request, 'index.html',data)
```

* Create index.html file
```python
{% extends 'base.html' %}
{% block content %}
<div class="container-fluid mt-3">
	<div class="row">

		<div class="col-lg-3 mx-auto">
			<div class="list-group">

				<a href="/" class="list-group-item list-group-item-action">All Products</a>

				{% for category in categorie %}
				<a href="/?category={{category.id}}"
					class="list-group-item list-group-item-action">{{category.name}}</a>
				{% endfor %}
			</div>
		</div>

		
		<div id='products' class="col-lg-9 mx-auto">
			<div class="row mx-auto">
				{% for val in product %}
				<div class="card mx-auto mb-3" id={{val.id}} style="width: 18rem;">
					<img class="card-img-top" src="{{val.image.url}}" alt="Card image cap">
					<p></p>
					<div class="card-body">
						<p class="card-title">{{val.name}}</p>
						<p class="card-text"><b>{{val.price}}</b></p>
						<p class="card-text"><b>{{val.category.name}}</b></p>
					
					</div>

					<div class="card-footer p-0 no-gutters">

						<input type="submit" class="float-right btn btn-light  form-control"
								value="Add To Cart">

					</div>

				</div>
				{% endfor %}
			</div>
		</div>

	
	</div>
</div>

{% endblock %}

```

