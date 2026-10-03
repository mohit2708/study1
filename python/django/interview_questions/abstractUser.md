### What is AbstractUser in Django?
* AbstractUser is a built-in abstract class in Django that provides the complete functionality of Django's default User model. We can inherit from AbstractUser to create a custom user model and add our own fields without implementing authentication functionality from scratch.
* AbstractUser Django की एक built-in abstract model class है, जिसका उपयोग करके हम अपना custom User model बना सकते हैं। यह Django के default User model की लगभग पूरी functionality पहले से provide करता है।
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```
* अब User हमारा custom user model है।
* इसके अलावा Django की authentication/permission functionality भी मिलती है।

#### इसमें क्या-क्या मिलता है?
* AbstractUser में Django के default user के commonly used fields और authentication features मिलते हैं, जैसे:
| Field          | Purpose                 |
| -------------- | ----------------------- |
| `username`     | User identification     |
| `first_name`   | First name              |
| `last_name`    | Last name               |
| `email`        | Email                   |
| `password`     | Hashed password         |
| `is_staff`     | Admin site access       |
| `is_active`    | Account active/inactive |
| `is_superuser` | Superuser permissions   |
| `last_login`   | Last login time         |
| `date_joined`  | Account creation time   |

* मान लीजिए आपको default Django User में अपना field add करना है:
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15)
    age = models.IntegerField(null=True, blank=True)
```
* अब आपके User में Django के existing user fields + आपके custom fields होंगे।

### **What is AbstractBaseUser in Django?**
* AbstractBaseUser Django की एक low-level base class है जिसका उपयोग करके हम पूरी तरह custom User model बना सकते हैं।
* इसमें Django आपको basic authentication functionality देता है, लेकिन User के fields और login identification का तरीका आपको खुद define करना पड़ता है।
```python
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
```
* अब user login के लिए username की जगह email use कर सकता है।

#### AbstractBaseUser क्या देता है?
* मुख्य रूप से:
  * Password hashing
  * set_password()
  * check_password()
  * last_login
  * Authentication-related basic functionality
* लेकिन आपको खुद define करना पड़ सकता है:
  * email
  * username
  * first_name
  * is_active
  * is_staff
  * is_superuser
  * Custom manager
  * USERNAME_FIELD
  * Permissions-related configuration


### AbstractUser vs AbstractBaseUser
| `AbstractUser`                                     | `AbstractBaseUser`                             |
| -------------------------------------------------- | ---------------------------------------------- |
| Default Django User की functionality काफी हद तक मिलती है | केवल core authentication functionality मिलती है    |
| Username, email, first_name आदि available           | Fields आपको खुद define करने पड़ते हैं                 |
| आसान और जल्दी implement होता है                          | ज्यादा customization                              |
| `UserAdmin` को आसानी से reuse कर सकते हैं                 | Admin configuration ज्यादा manually करना पड़ सकता है  |
| Most custom-user cases के लिए convenient             | पूरी तरह custom authentication requirements के लिए |

* Django documentation के अनुसार, AbstractUser, AbstractBaseUser को extend करता है और default User की full implementation provide करता है।
* **एक important point:** अगर आप AbstractUser से custom user बनाते हैं, तो AUTH_USER_MODEL को अपने custom model पर point करना होता है, और नए project में इसे migrations बनाने से पहले configure करना चाहिए।