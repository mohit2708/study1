
|  No.  | View Questions                                                                                                     |
| :---: | ------------------------------------------------------------------------------------------------------------------ |
|       | [What is a View?](#what-is-a-view)                                                                                 |
|       | [Types of Views?](#types-of-views)                                                                                 |
|       | [How to view all items in a Model using Django QuerySet?](#how-to-view-all-items-in-a-model-using-django-queryset) |

### **What is a View?**
* A View in Django is a Python function or class that receives an HTTP request, processes the required application logic, interacts with models if needed, and returns an HTTP response to the client.
* HINDI:- A View Django ka wo part hai jo HTTP request receive karta hai aur HTTP response return karta hai.
* View application ka logic handle karta hai.
* View generally:
  * Request receive karta hai.
  * Request se data leta hai.
  * Business logic perform karta hai.
  * Model/database se data fetch karta hai.
  * Template ko data bhej sakta hai.
  * Response return karta hai.

### **Types of Views?**
* Django mein mainly 2 types commonly use hote hain:

#### Function-Based View (FBV)
```python
def home(request):
    return HttpResponse("Hello")
```

#### Class-Based View (CBV)
```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):

    def get(self, request):
        return HttpResponse("Hello")
```

#### Difference between FBV and CBV?

| FBV                                                | CBV                                              |
| -------------------------------------------------- | ------------------------------------------------ |
| Function-based                                     | Class-based                                      |
| Simple functions                                   | Classes and methods                              |
| Easy to understand                                 | Slightly more complex                            |
| Less abstraction                                   | More abstraction                                 |
| Reusability manually implement karni pad sakti hai | Inheritance se easily reusable                   |
| HTTP methods manually handle kar sakte hain        | `get()`, `post()`, `put()` etc. separate methods |
| Small/simple views ke liye good                    | Complex/reusable views ke liye good              |
| Generic Views use nahi karte directly              | Django Generic Views mostly CBV based hain       |

| FBV                                   | CBV                                      |
| ------------------------------------- | ---------------------------------------- |
| View **function** hota hai            | View **class** hota hai                  |
| `def` use karte hain                  | `class` use karte hain                   |
| Simple logic ke liye easy             | Complex/reusable logic ke liye better    |
| GET/POST ko `if` se handle karte hain | `get()`, `post()` methods use karte hain |
| Inheritance nahi hoti                 | Inheritance use kar sakte hain           |
| Code generally simple hota hai        | Code reusable hota hai                   |
| Generic Views ka direct benefit nahi  | Generic Views use kar sakte hain         |


* FBV Example — GET + POST
```python
def employee(request):

    if request.method == "GET":
        return HttpResponse("GET request")

    if request.method == "POST":
        return HttpResponse("POST request")
```

* CBV Example — GET + POST
```python
from django.views import View

class EmployeeView(View):

    def get(self, request):
        return HttpResponse("GET request")

    def post(self, request):
        return HttpResponse("POST request")
```

### Advantages of CBV (Class-Based Views)?
* CBV provides code **reusability**, **inheritance**, **mixins support**, **better organization**, and **built-in generic views** for CRUD operations. It helps reduce code duplication and makes large Django applications easier to maintain.

1. **Code Reusability:-** Ek baar class bana kar multiple views me reuse kar sakte hain.
```python
from django.views import View

class UserView(View):
    pass
```

2. **Less Code with Generic Views:-** Django ke built-in generic views (ListView, CreateView, UpdateView, DeleteView) CRUD operations ko bahut easy bana dete hain.
```python
from django.views.generic import ListView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
```

3. **Better Organization:-** Related methods (GET, POST, PUT, DELETE) ek hi class ke andar rehte hain.
```python
class UserView(View):
    
    def get(self, request):
        return HttpResponse("GET Request")
    
    def post(self, request):
        return HttpResponse("POST Request")
```

4. **Inheritance Support:-** Parent class se common functionality inherit kar sakte hain.
```python
class BaseView(View):
    def common_method(self):
        pass

class UserView(BaseView):
    pass
```

5. **Mixins Support:-** Authentication, permissions, pagination jaise features easily add kar sakte hain.
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, View):
    pass
```

6. **Easy CRUD Operations:-** CreateView, UpdateView, DeleteView, DetailView, ListView ready-made milte hain.
```python
from django.views.generic import CreateView

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'salary']
```

### What is Mixin?
* Mixins are reusable classes that provide additional functionality to Class-Based Views through multiple inheritance. For example, LoginRequiredMixin adds authentication checks without rewriting code.
* Mixin ek chhoti reusable class hoti hai jo kisi class me extra functionality add karti hai.
* 👉 "Mixin = Additional feature jo inheritance ke through class me add kar sakte hain."

#### Common Django Mixins
| Mixin                     | Use                        |
| ------------------------- | -------------------------- |
| `LoginRequiredMixin`      | User login hona chahiye    |
| `PermissionRequiredMixin` | Specific permission check  |
| `UserPassesTestMixin`     | Custom condition check     |
| `SuccessMessageMixin`     | Success message show karna |

#### Example: LoginRequiredMixin
* Agar kisi page ko login user hi access kar sake:
```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee

#   Yahan:
    # ListView → Employee list dikhata hai.
    # LoginRequiredMixin → Login check karta hai.
# Agar user login nahi hai to login page par redirect ho jayega.
```

### What is Generic View?
* Generic Views are built-in Class-Based Views provided by Django that handle common web development tasks such as listing, creating, updating, viewing, and deleting objects with minimal code.
* Generic Views Django ki pre-built Class-Based Views (CBVs) hoti hain jo common tasks ko kam code me perform karne ke liye use hoti hain.
* **Simple words:** Generic View = Django ka ready-made view jo common functionality ka code already provide karta hai.

#### Common Generic Views
| Generic View   | Purpose                  |
| -------------- | ------------------------ |
| `ListView`     | Multiple records ki list |
| `DetailView`   | Single record ki details |
| `CreateView`   | New record create        |
| `UpdateView`   | Existing record update   |
| `DeleteView`   | Record delete            |
| `TemplateView` | Simple template render   |

#### Example
* Without Generic View:
```python
class EmployeeListView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, "employees.html", {
            "employees": employees
        })
```
* Using Generic View:
```python
from django.views.generic import ListView

class EmployeeListView(ListView):
    model = Employee
    template_name = "employees.html"
    context_object_name = "employees"
```
* Yahan ListView already database se objects fetch karke template ko provide karne ka common logic handle karta hai.


### How to view all items in a Model using Django QuerySet?
* filter() is used to retrieve records that match one or more given conditions. It returns a QuerySet containing all matching objects.
* Django में किसी Model के सभी records/items निकालने के लिए objects.all() use करते हैं।
```python
ModelName.objects.all()
```

### How to Filter Items in Django QuerySet?
* Django में records को filter करने के लिए filter() method use करते हैं।
```python
Employee.objects.filter(salary=50000)

# Multipal condition
Employee.objects.filter(salary__gt=50000, name="Mohit")


```
* अगर किसी employee की salary 100000 नहीं है, तो: <QuerySet []>

### How to get a particular item in Django?
* अगर आपको एक particular record चाहिए, तो सबसे commonly get() method use करते हैं।
```python
employee = Employee.objects.get(id=1)


print(employee.name)
print(employee.salary)
```
* अगर record नहीं मिला? to **exception** आएगी।


### Difference between get() and filter() in Django?
* **get()** is used to retrieve a single object, while **filter()** is used to retrieve one or more matching objects as a QuerySet.
* **get()** raises an exception if no object or multiple objects are found, whereas **filter()** returns an empty or multiple-result QuerySet.

| `get()`                                         | `filter()`                              |
| ----------------------------------------------- | --------------------------------------- |
| **Single object** return करता है                  | **QuerySet** return करता है               |
| केवल **exactly one** record expected होता है        | **0, 1 या multiple** records मिल सकते हैं    |
| Record नहीं मिला → `DoesNotExist`                   | Record नहीं मिला → empty QuerySet `[]`      |
| Multiple records मिले → `MultipleObjectsReturned` | Multiple records मिलने पर कोई error नहीं     |
| Unique field के लिए useful                        | Multiple records search करने के लिए useful |

### **how to insert, update and delete object using queryset?**
* In Django, we can **create** records using **create()** or **save()**, **update** records using **filter().update()**, and **delete** records using **filter().delete()**.

#### Insert object using QuerySet?
* Using create
```python
Employee.objects.create(
    name="Mohit",
    salary=50000
)
```

* Using save
```python
employee = Employee(
    name="Mohit",
    salary=50000
)

employee.save()
```

* Insert Multipal record
```python
Employee.objects.bulk_create([
    Employee(name="Mohit", salary=50000),
    Employee(name="Rahul", salary=60000),
])
```

#### Update object using QuerySet?
```python
Employee.objects.filter(id=1).update(salary=70000)

# Or
user = User.objects.get(id=1)
user.name = "saxena"
user.save()
```

#### Delete object using QuerySet?
```python
Employee.objects.filter(id=1).delete()
```