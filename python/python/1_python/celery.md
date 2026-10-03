### **What is Celery?**
* Celery is a distributed task queue used to execute background and long-running tasks asynchronously using workers and a message broker such as Redis or RabbitMQ.
* Celery ek distributed task queue hai jo background mein tasks execute karne ke liye use hota hai.


#### Celery architecture
```python
FastAPI
   │
   │ Task
   ↓
Message Broker
(Redis / RabbitMQ)
   │
   ↓
Celery Worker
   │
   ├── Send Email
   ├── Generate PDF
   ├── Process Image
   └── Heavy Data Processing
```

#### Celery kab use karte hain?
* 📧 Email sending
* 📄 PDF/report generation
* 🖼️ Image/video processing
* 📊 Large data processing
* 🔄 Scheduled/periodic jobs
* 🔔 Notifications
* Long-running background tasks

### Celery vs async/await
| `async/await`                                    | Celery                                     |
| ------------------------------------------------ | ------------------------------------------ |
| Same application/event loop ke andar concurrency | Background/distributed task execution      |
| Mostly I/O-bound operations                      | Long-running/heavy/background jobs         |
| Event loop use karta hai                         | Separate worker processes                  |
| API ke andar useful                              | API se task ko bahar execute kar sakta hai |
| Example: async API/DB call                       | Example: PDF generation, email, report     |


### Implement Celery on your project?
* In FastAPI, I can use BackgroundTasks for lightweight operations such as logging or simple notifications. For production-level background processing, I prefer Celery with Redis or RabbitMQ. The API sends the task to the broker, and a Celery worker consumes and executes the task asynchronously. Celery also provides features like retries, task queues, distributed workers, and scheduled tasks.

1. Architecture
```python
Client
   ↓
FastAPI
   ↓
Celery Task
   ↓
Redis (Broker)
   ↓
Celery Worker
   ↓
Email / Report / File Processing
```
* यहाँ:
  * FastAPI → API request handle करेगा
  * Celery → background task manage करेगा
  * Redis → task/message queue की तरह काम करेगा
  * Celery Worker → actual task execute करेगा

1. Install package
```python
pip install celery redis
```

1. Project Structure
* आपके बड़े-module architecture के हिसाब से:
```python
fastapi_project/
│
├── app/
│   ├── core/
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── celery_app.py
│   │   └── email_tasks.py
│   │
│   └── main.py
│
└── requirements.txt
```

1. Celery configuration
```python
celery_app.py

from celery import Celery

celery_app = Celery(
    "fastapi_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
```
* यहाँ:
  * broker = Redis
  * backend = Redis
* **Broker** task को queue में रखता है।
* **Backend** task का result/status store कर सकता है।

5. Celery Task बनाएं
* email_tasks.py
```python
from app.tasks.celery_app import celery_app


@celery_app.task
def send_email(email: str):
    print(f"Sending email to {email}")

    return {
        "status": "success",
        "email": email
    }
```
* अब send_email() एक Celery task बन गया।

6. FastAPI से task trigger करें
* main.py
```python
from fastapi import FastAPI
from app.tasks.email_tasks import send_email

app = FastAPI()


@app.post("/register")
def register(email: str):

    # Send task to Celery
    task = send_email.delay(email)

    return {
        "message": "User registered successfully",
        "task_id": task.id
    }
```
* सबसे important line:
```python
send_email.delay(email)
```
* यह email function को directly execute नहीं करता।
* यह task को Redis queue में भेजता है।


7. Celery Worker Start करें
* अब एक अलग terminal खोलें।
* Windows पर:
```python
celery -A app.tasks.celery_app.celery_app worker --loglevel=info --pool=solo
```
* Worker start होने के बाद वह Redis से tasks उठाएगा।
* Flow:
```python
POST /register
       ↓
FastAPI
       ↓
send_email.delay()
       ↓
Redis
       ↓
Celery Worker
       ↓
send_email()
```

8. API call करें
* Request:
```python
POST /register?email=mohit@gmail.com
```
* Response तुरंत:
```python
{
    "message": "User registered successfully",
    "task_id": "a8b7c6..."
}
```
* और Celery worker में:
```python
Sending email to mohit@gmail.com
```
* इसका मतलब API को email processing complete होने का wait नहीं करना पड़ा।

9. delay() क्या करता है?
* यह interview में बहुत important है।
```python
send_email.delay("mohit@gmail.com")
```
* Essentially Celery को कह रहे हैं:
  * "इस function को अभी मेरे API process में मत चलाओ। इसे task queue में डाल दो और Celery worker इसे execute करेगा।"

10.  delay() vs Normal Function
```python
Normal function
send_email("mohit@gmail.com")

Flow:

FastAPI
   ↓
send_email()
   ↓
Email complete
   ↓
Response

API को wait करना पड़ेगा।

Celery
send_email.delay("mohit@gmail.com")

Flow:

FastAPI
   ↓
Redis
   ↓
Response immediately

Celery Worker
   ↓
send_email()

इसलिए API responsive रहती है।
```

11.  Real Email Example
* Actual project में task के अंदर SMTP/email service use कर सकते हैं:
```python
@celery_app.task
def send_welcome_email(email: str, username: str):

    # SMTP / Email service
    send_email(
        to=email,
        subject="Welcome",
        body=f"Welcome {username}"
    )

    return "Email sent successfully"

API:

@app.post("/register")
def register(
    email: str,
    username: str
):

    send_welcome_email.delay(
        email,
        username
    )

    return {
        "message": "Registration successful"
    }
```


12. BackgroundTasks vs Celery
```
अब दोनों को अच्छे से differentiate कर सकते हैं:

FastAPI
│
├── BackgroundTasks
│      ↓
│   Simple tasks
│
└── Celery
       ↓
    Redis/RabbitMQ
       ↓
    Celery Worker
       ↓
    Heavy / long-running tasks

```