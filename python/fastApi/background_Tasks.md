### What are BackgroundTasks?
* BackgroundTasks is a FastAPI utility used to execute tasks after returning a response to the client. It is commonly used for email notifications, logging, file processing, and other non-blocking operations, improving API response time and user experience.
* BackgroundTasks FastAPI का एक फीचर है, जिसका उपयोग किसी काम को response भेजने के बाद background में execute करने के लिए किया जाता है।
* इससे user को तुरंत response मिल जाता है और time-consuming task बाद में चलता रहता है।
```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email(email):
    print(f"Sending email to {email}")

@app.post("/register")
def register(email: str, background_tasks: BackgroundTasks):

    background_tasks.add_task(send_email, email)

    return {"message": "User registered successfully"}
```
* Heavy tasks (large reports, video processing, ML jobs, etc.) के लिए आमतौर पर Celery + Redis/RabbitMQ जैसे tools इस्तेमाल किए जाते हैं।
* **BackgroundTasks → Lightweight tasks**
* **Celery → Heavy & Distributed tasks**

#### IN django
* Django में background tasks के लिए आमतौर पर:
  * Celery + Redis
  * Django-RQ
  * Django-Q
  * Threading (small tasks)
* use किए जाते हैं।

#### Real Use Cases
1. Email Sending
2. SMS Sending
3. Log File Writing
4. Report Generation
5. File Processing

### How do you send emails in the background?
* To send emails in the background, I use asynchronous task processing so that the user does not have to wait for the email to be sent. In FastAPI, for lightweight tasks, I use BackgroundTasks. For production applications and heavy workloads, I use Celery with Redis or RabbitMQ. The API returns the response immediately, and the email is sent asynchronously in the background.


### Difference between BackgroundTasks and Celery?
* दोनों का purpose background में task चलाना है, लेकिन दोनों का architecture और use case अलग है।
| Feature                | FastAPI `BackgroundTasks` | Celery                             |
| ---------------------- | ------------------------- | ---------------------------------- |
| Type                   | FastAPI built-in utility  | Separate task queue system         |
| Setup                  | बहुत आसान                 | Broker + Worker setup चाहिए        |
| Queue                  | ❌ Dedicated queue नहीं    | ✅ Task queue                       |
| Worker                 | ❌ Separate worker नहीं    | ✅ Celery Worker                    |
| Redis/RabbitMQ         | ❌ Required नहीं           | ✅ Usually required                 |
| Heavy tasks            | ❌ Suitable नहीं           | ✅ Suitable                         |
| Distributed processing | ❌                         | ✅                                  |
| Retry mechanism        | Limited/manual            | ✅ Built-in                         |
| Scheduled tasks        | ❌                         | ✅ Celery Beat                      |
| Best for               | Small/light tasks         | Heavy & production background jobs |
