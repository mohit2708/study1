### **main urls.py**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration_function_based/', include('registration_function_based.urls')),
]
```

### **Urls.py**
```python
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

### **views.py**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
	# return HttpResponse('first page')
	return render(request, 'authentication/index.html')

def signin(request):
	if request.method == "POST":
		username 	= request.POST['username']
		password 	= request.POST['password']

		user = authenticate(username=username,password=password)

		if user is not None:
			login(request, user)
			fname = user.first_name
			return render(request, 'authentication/index.html',{'fname': fname})

		else:
			messages.error(request, "invalid credinatiols!!!!")
			return redirect('name_login')

	return render(request, 'authentication/login.html')

def signup(request):
	if request.method == "POST":
		username 	= request.POST.get('username')
		first_name 	= request.POST['fname']
		last_name 	= request.POST['lname']
		email 		= request.POST['email']
		phone 		= request.POST['phone']
		password 	= request.POST['password']
		confirm_pass = request.POST['cpassword']

        if User.objects.filter(username=username):
			messages.error(request,'username is already exists')
			return redirect('signup')

		if User.objects.filter(email=email):
			messages.error(request,'email is already exists')
			return redirect('signup')

		if password != confirm_pass:
			messages.error(request,'passowrd can not be match')
			return redirect('signup')

		if not username.isalnum():
			messages.error(request,'user name must be alphanumaric')
			return redirect('signup')

		myuser = User.objects.create_user(username,email,password)
		myuser.first_name = first_name
		myuser.last_name = last_name

		myuser.save()

		messages.success(request,"your account create successfully")

		return redirect('name_login')

	return render(request, 'authentication/signup.html')


def signout(request):
	logout(request)
	print('logout')
	messages.success(request,'logged out succesffully')
	return redirect('home')
```


### **Index.html**
```python
{% for message in messages %}
<h3>{{message}}</h3>
{% endfor %}


{% if user.is_authenticated %}
	<h1>hello {{fname}} </h1>
	<h4>You are logged in</h4>
	<a href="/logout">logout</a>
{% else %}
	<a href="{% url 'name_login' %}">Login</a>
	<a href="/signup">signup</a>
{% endif %}
```

### **signup.html**
```python
<!DOCTYPE html>
<html>
<body>

<h2>Signup  Forms</h2>

<form action="{% url 'signup' %}" method="post">
	{% csrf_token %}
	<label>User Name:</label><br>
	<input type="text" id="username" name="username" placeholder="Enter Your User Name"><br>

	<label>First name:</label><br>
	<input type="text" id="fname" name="fname" placeholder="Enter Your First Name"><br>

	<label>Last name:</label><br>
	<input type="text" id="lname" name="lname"><br><br>

	<label>Email:</label><br>
	<input type="email" id="email" name="email"><br><br>

	<label>Phone:</label><br>
	<input type="text" id="phone" name="phone"><br><br>
	
	<label>Password:</label><br>
	<input type="password" id="password" name="password"><br><br>

	<label>Confirm Password:</label><br>
	<input type="text" id="cpassword" name="cpassword"><br><br>

	<button type="submit">Submit</button>
</form> 
{% for message in messages %}
<h3>{{message}}</h3>
{% endfor %}
</body>
</html>
```


### **login.html**
```python
<!DOCTYPE html>
<html>
<body>

<h2>Sign In</h2>
{% for message in messages %}
<h3>{{message}}</h3>
{% endfor %}
<form action="{% url 'name_login' %}" method="post">
    {% csrf_token %}
    <label>User Name:</label><br>
    <input type="text" id="username" name="username" placeholder="Enter Your User Name"><br>

    <label>Password:</label><br>
    <input type="password" id="password" name="password" placeholder="Enter Your Password"><br>


    <button type="submit">SignIn</button>
</form> 

</body>
</html>
```