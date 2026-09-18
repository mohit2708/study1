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
