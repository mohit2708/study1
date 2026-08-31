## Monolithic vs Microservices Architecture?
#### Monolithic
* Monolithic architecture is a software design approach where all components of an application, such as user management, business logic, and database access, are built and deployed as a single unified application.
* Monolithic architecture is simpler and suitable for small applications.
* **HINDI:-** Monolithic architecture mein poora application ek single codebase aur deployment unit mein hota hai. Agar application ka koi ek module change hota hai to poori application redeploy karni padti hai.

#### Microservices
* Microservices architecture is a software design approach where an application is divided into multiple small, independent services. Each service is responsible for a specific business function and can be developed, deployed, and scaled independently.
* microservices architecture is more scalable and suitable for large, complex, and enterprise-level applications.
* **HINDI:-** Microservices architecture mein application ko multiple independent services mein divide kiya jata hai. Har service apna codebase, database aur deployment maintain karti hai. Isse independent scaling aur deployment possible hota hai.

#### Advantages
1. Easy Development:- Ek hi codebase.
2. Easy Deployment:- Sirf ek application deploy karni hoti hai.
3. Debugging Easy:- Sab logs ek jagah milte hain.
4. Faster Initial Development:- Startup projects ke liye best.

#### Disadvantages
1. Large Codebase:- Application badi hote hi manage karna mushkil.
2. Single Point of Failure:- Agar app crash hua to poora system down.
3. Scaling Problem:- Sirf Orders module busy hai to bhi poori application scale karni padegi.
4. Slow Deployment:- Chhoti change ke liye bhi poora app deploy karna padega.

### How do microservices communicate?  
* Microservices communicate with each other using **APIs** or **messaging systems**. The most common communication methods are synchronous communication using REST APIs or gRPC, and asynchronous communication using message brokers such as RabbitMQ, Apache Kafka, or Amazon SQS.
1. Synchronous Communication (REST API)
2. Asynchronous Communication (Message Queue)

### How do Microservices communicate with each other?
- Microservices communicate with each other using various mechanisms, including:
1. **RESTful APIs (Representational State of Resource):** Services expose RESTful APIs that allow other services to interact with them using HTTP verbs (e.g., GET, POST, PUT, DELETE).
2. **Message queues:** Messages are sent between services using message brokers like RabbitMQ, Apache Kafka, or Amazon SQS.
3. **Event-driven architecture:** Services publish and subscribe to events, allowing them to react to changes in the system without direct communication.
4. **gRPC (Google Remote Procedure Call):** A high-performance RPC framework that allows services to communicate with each other using protocol buffers.
5. **GraphQL:** A query language for APIs that allows services to expose their data and functionality in a flexible, schema-driven way.

#### Some popular technologies for building microservices include:
1. Docker (containerization)
2. Kubernetes (orchestration)
3. Service Meshes like Istio or Linkerd
4. API gateways like NGINX or Amazon API Gateway


### SOLID Principles
* SOLID object-oriented programming ke 5 important design principles hain. Inka purpose code ko clean, maintainable, scalable aur loosely coupled banana hai.
  * **S — Single Responsibility:** A class should have only one responsibility.
  * **O — Open/Closed:** Code should be open for extension but closed for modification.
  * **L — Liskov Substitution:** A child class should be able to replace its parent class without breaking the code.
  * **I — Interface Segregation:** A class should not be forced to implement unnecessary methods.
  * **D — Dependency Inversion:** Classes should depend on abstractions, not concrete classes.
<div style="page-break-before: always;"></div>

1. **S — Single Responsibility Principle (SRP):-**
* A class should have only one responsibility.(Matlab ek class ko sirf ek responsibility handle karni chahiye.)
```php
# ❌ Bad:
class User
{
    public function createUser() {}
    public function sendEmail() {}
    public function generateReport() {}
}

# ✅ Better:
class UserService
{
    public function createUser() {}
}

class EmailService
{
    public function sendEmail() {}
}

class ReportService
{
    public function generateReport() {}
}
```
<div style="page-break-before: always;"></div>

2. **O — Open/Closed Principle (OCP)**
* Classes should be open for extension but closed for modification.
* Existing code ko baar-baar modify karne ke bajay new functionality extend karni chahiye.
```python
interface Payment
{
    public function pay();
}

class StripePayment implements Payment
{
    public function pay()
    {
        echo "Stripe payment";
    }
}

class PaypalPayment implements Payment
{
    public function pay()
    {
        echo "Paypal payment";
    }
}

```
* Kal agar Razorpay add karna ho:
```python
class RazorpayPayment implements Payment
{
    public function pay()
    {
        echo "Razorpay payment";
    }
}
```
* Existing classes ko modify karne ki zarurat nahi.
<div style="page-break-before: always;"></div>

3. **L — Liskov Substitution Principle (LSP)**
* Child class should be replaceable with its parent class without breaking the application.
* Agar kisi parent class ki jagah uski child class ko use karein, to application ka behavior nahi badalna chahiye aur code break nahi hona chahiye.
```php
class Bird
{
    public function eat()
    {
        echo "Eating";
    }
}

class Sparrow extends Bird
{
    public function fly()
    {
        echo "Flying";
    }
}
```
* Yahan Sparrow, Bird ka child hai. Jahan Bird object use ho sakta hai, wahan Sparrow bhi use ho sakta hai.
```php
# WRONG Example
class Bird
{
    public function fly()
    {
        echo "Flying";
    }
}

class Penguin extends Bird
{
    public function fly()
    {
        throw new Exception("Penguin can't fly");
    }
}
```
<div style="page-break-before: always;"></div>

* Problem:
  * Parent Bird bol raha hai ki sab birds fly kar sakte hain.
  * Penguin fly nahi kar sakta.
  * Isliye Penguin ko Bird ki jagah use karne par code break ho sakta hai.

* Correct code
```php
interface Flyable
{
    public function fly();
}

class Sparrow implements Flyable
{
    public function fly() {}
}

class Penguin
{
    public function eat() {}
}
```
<div style="page-break-before: always;"></div>

4. **I — Interface Segregation Principle (ISP)**
* A class should not be forced to implement methods that it does not need.
```php
❌ Bad:
interface Worker
{
    public function work();
    public function eat();
    public function sleep();
}
```

* Agar Robot ko implement karna hai, to robot ko eat() aur sleep() ki zarurat nahi.
```php
✅ Better:
interface Workable
{
    public function work();
}

interface Eatable
{
    public function eat();
}

interface Sleepable
{
    public function sleep();
}
```

* Ab Robot sirf:
```php
class Robot implements Workable
{
    public function work() {}
}
```
<div style="page-break-before: always;"></div>

5. D — Dependency Inversion Principle (DIP)
* High-level modules should depend on abstractions, not concrete implementations.
```php
❌ Bad:
class OrderService
{
    private StripePayment $payment;

    public function __construct()
    {
        $this->payment = new StripePayment();
    }
}
# OrderService directly StripePayment par dependent hai.
```

```php
✅ Better:

interface Payment
{
    public function pay();
}

class OrderService
{
    public function __construct(
        private Payment $payment
    ) {}

    public function order()
    {
        $this->payment->pay();
    }
}
# Ab hum easily Stripe, PayPal, Razorpay kuch bhi inject kar sakte hain.
```