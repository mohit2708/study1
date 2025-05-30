### creaet model
```python
class ModelName(models.Model):

    id          = models.AutoField('Id', primary_key=True)
    first_name  = models.CharField('First name', max_length=15, null = True, blank=True)
    last_name   = models.CharField('Last name', max_length=16, blank=True)
    email       = models.EmailField(max_length = 255, unique=True, null = True)
    user_name   = models.CharField(max_length=50, unique=True, null = True, error_messages ={
                    "unique":"The User Name Field you entered is unique."
                    })
    address     = models.TextField(default = 'Message...')
    files       = models.FilePathField(path="/img") #for image, file, any type of file.
    image       = models.ImageField(upload_to='uploads/products/', blank=True, null=True) # only for image
    employee_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    age      = models.IntegerField()
    GENDER_SELECT = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=11,choices=GENDER_SELECT)



    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Approved'),
    )
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)


    dof         = models.DateField('Birthday')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
      db_table = "table_name"
  
   	def __str__(self):
		  return "{} {}".formet(self.first_name, self.last_name)

    def __str__(self):      
        return self.first_name	#django admin mai admin frount mai name sa list show hogi 

    def __str__(self):
    	return f"Product ({self.pk}): {self.name}"  #  __str__() method is overridden to return a string representation of the Product object.

class Crudst(models.Model):
    categories = models.ManyToManyField('Category', related_name='posts')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)  # can login
    date_joined = models.DateTimeField(auto_now_add=True)    
    stmobile = models.IntegerField()
    
class Category(models.Model):
    name = models.CharField(max_length=20)
   

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
```


```python
python manage.py migrate --run-syncdb
```



#### Mutipale model files in one folder
```python
1. create the "models" folder in your app
2. create "__init__.py" file in models folder.
3. create "product.py" file in models folder.
4. create "category.py" file in models folder.
```
```python
=======put the code in __init__.py===============
from .product import Product
from .category import Category

=======product.py===========
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

==========category.py=================
from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
    	return self.name
```


### Database seeding fixture file like seeder
* first of all create the json file.
```python
# it is commend for export the data from the database
python manage.py dumpdata your_app_name.model_name  > country.json
python manage.py dumpdata app_name > filename.json

# for import the data in database.
1. we create the folder "fixtures" name in app (OR)
    cd your_app_name
    mkdir fixtures
2. create the json file in this folder and creat the data in this format below.
    country.json
[
    {
      "model": "ajaxCountryStateCity.countries",
      "pk": 1,
      "fields": {
        "shortname": "in",
        "name": "India",
        "phonecode": 91
      }
    },
    {
      "model": "ajaxCountryStateCity.countries",
      "pk": 2,
      "fields": {
        "shortname": "us",
        "name": "usa",
        "phonecode": 65
      }
    },
    {
      "model": "ajaxCountryStateCity.countries",
      "pk": 3,
      "fields": {
        "shortname": "The",
        "name": "gfj",
        "phonecode": 354
      }
    }
]
python manage.py loaddata city.json (OR)
python manage.py loaddata your_app_name/fixtures/city.json


note:- if error add code in model file.
class Cities(models.Model):
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()
    class Meta:
            app_label = 'ajaxCountryStateCity'
```


### Databse to Create model
```python
python manage.py inspectdb > app_name\models.py (OR)
python manage.py inspectdb table_name1 table_name2 ...> app_name\models.py (OR)
```