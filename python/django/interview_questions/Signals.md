### 🎯 **What are Django Signals?**
* Django Signals allow decoupled applications to get notified when certain events occur, such as saving or deleting a model instance.
* We can connect a **receiver** function to a signal and execute custom logic automatically when that event occurs.
* Django Signals ek mechanism hai jo humein allow karta hai ki kisi particular event ke hone par automatically koi function execute ho jaye.
* Simple words:
  * Signal = Event hone par automatically action perform karna.

#### Important Django Signals
1. Model Signals
| Signal        | Kab trigger hota hai?                 |
| ------------- | ------------------------------------- |
| `pre_save`    | Model save hone se pehle              |
| `post_save`   | Model save hone ke baad               |
| `pre_delete`  | Model delete hone se pehle            |
| `post_delete` | Model delete hone ke baad             |
| `m2m_changed` | Many-to-Many relation change hone par |

2. Request/Response Signals
* Request ke events ke liye:
| Signal                  | Meaning                              |
| ----------------------- | ------------------------------------ |
| `request_started`       | Request start hone par               |
| `request_finished`      | Request complete hone par            |
| `got_request_exception` | Request ke during exception hone par |

3. Authentication Signals
* User authentication ke events ke liye:
| Signal              | Meaning              |
| ------------------- | -------------------- |
| `user_logged_in`    | User login hone par  |
| `user_logged_out`   | User logout hone par |
| `user_login_failed` | Login fail hone par  |

#### Example
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### 🎯 **Why use signals?**
* We use Django Signals to automatically execute specific actions when certain events occur. They help keep event-driven logic separate from the main application logic and reduce repetitive code.
* Common Use Cases
  * User create hone par Profile create karna
  * User delete hone par related data clean karna
  * Order create hone par notification/email bhejna
  * Login hone par activity/log record karna
  * Model update hone par audit log maintain karna
  * Many-to-Many relation change hone par koi action lena