### 🎯 **What is Redis?**
* Redis (Remote Dictionary Server) ek in-memory data store hai jo data ko RAM me store karta hai, isliye bahut fast hota hai.
* Redis ek **high-speed key-value database hai jo caching, session management, rate limiting, aur real-time applications me use hota hai**.
* Redis is an in-memory **key-value data store** used for caching, session management, rate limiting, and message queues. Since data is stored in **RAM**, Redis provides extremely fast read and write operations compared to traditional databases.

#### Redis ki Features
1. In-Memory Storage (RAM based)
2. Extremely Fast (microseconds response)
3. Key-Value Store
4. Supports Expiration Time (TTL)
5. Caching Support
6. Pub/Sub Messaging
7. Persistence Support (data disk me bhi save kar sakta hai)

#### Redis kahan use hota hai?
1. **Caching**
* Frequently used data Redis me store kar dete hain.
* Database ko baar-baar hit nahi karna padta.

2. **Session Storage**
* Login sessions Redis me store kiye jaate hain.

3. **Rate Limiting**
* FastAPI, Django APIs me use hota hai.
* Request count Redis me maintain hota hai.

4. **Queue System**
* Background jobs ke liye.
* Celery + Redis ka combination bahut common hai.

#### Why use Redis when we already have MySQL?
* MySQL stores **data** permanently on **disk**, while **Redis** stores data in **memory**, making it much faster. Redis is mainly used for caching, sessions, and rate limiting to reduce database load and improve application performance.