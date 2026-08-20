### What is Serverless?
* Serverless is a cloud computing model where we run applications without managing the underlying servers. The cloud provider manages the servers, infrastructure, scaling, and availability for us.
* For example, with AWS Lambda, we only provide our code, and AWS automatically runs and scales it when required.
* Serverless एक cloud computing model है जिसमें developer को server को manually manage करने की जरूरत नहीं होती।
* मतलब हमें इन चीज़ों की चिंता नहीं करनी पड़ती:
  * Server setup करना
  * Server maintain करना
  * Scaling करना
  * Hardware manage करना
  * Server की availability manage करना
* ये सब काम AWS जैसे cloud provider खुद manage करते हैं।

#### Note
* Serverless does NOT mean there are no servers.
* Servers are still used, but AWS manages them for us.
* Server होते हैं, लेकिन उन्हें AWS manage करता है, developer नहीं।

### What is AWS Lambda?
* AWS Lambda is a **serverless**, event-driven compute service provided by AWS that lets us run code without managing servers.
* We upload our code as a Lambda function, and AWS automatically handles:
  * Server provisioning
  * Scaling
  * Availability
  * Infrastructure management
* Lambda executes the function when an event occurs, such as an API request, S3 file upload, SQS message, or CloudWatch event.

#### Example
* If a user uploads an image to S3, an S3 event can trigger a Lambda function to process that image automatically.

#### How does AWS Lambda work?
* “AWS Lambda is an **event-driven service**. When an event occurs, such as an API request, S3 upload, or SQS message, the event triggers a Lambda function. AWS creates or reuses an execution environment, runs our code, and automatically manages scaling and infrastructure. We only need to provide the function code and configuration.”
* AWS Lambda event-driven तरीके से काम करता है। जब कोई event होता है, Lambda उस event के response में आपका function execute करता है।

* Example: S3 + Lambda
```python
# मान लो user ने S3 bucket में image upload की:
User uploads image
        ↓
    S3 Bucket
        ↓
   S3 Event Trigger
        ↓
   AWS Lambda
        ↓
Image Processing Code
        ↓
    Result
```
* Lambda automatically function को execute करेगा। आपको server start करने या manually application run करने की जरूरत नहीं है।


### 🎯 **What is Lambda Cold Start?**
* A Lambda cold start occurs when AWS has to create and initialize a new execution environment before executing a function. This adds some latency to the first request. Subsequent requests can reuse the existing warm environment and are usually faster.
* **IN HINDI:-**
* Cold start तब होता है जब AWS Lambda को किसी request को handle करने के लिए नया execution environment create और initialize करना पड़ता है।
* इस initialization में थोड़ा extra time लगता है, इसलिए पहली request थोड़ी slow हो सकती है।
* **assan lang:-**
* Cold Start = Lambda को पहली बार environment तैयार करने में लगने वाला extra time.
* example:-नया computer start करने में time लगता है → लेकिन computer पहले से ON है तो application जल्दी open होती है।

#### Cold Start कब ज्यादा हो सकता है?
* Function लंबे समय से invoke नहीं हुआ हो
* नई execution environment की जरूरत हो
* Large deployment package हो
* Heavy dependencies हों
* Runtime initialization ज्यादा हो
<div style="page-break-before: always;"></div>


### 🎯 **What is Lambda Timeout?**
* Lambda timeout is the maximum amount of time that AWS Lambda allows a function to run. If the function does not complete within the configured timeout, Lambda terminates the execution and returns a timeout error.
* **In HINDI:-**
* Lambda timeout वह maximum time है जितने समय तक AWS Lambda किसी function को execute होने देता है।
* अगर function इस time limit के अंदर complete नहीं होता, तो AWS Lambda execution को stop/terminate कर देता है।
* Lambda Timeout = Function को पूरा होने के लिए मिलने वाला maximum time.
* **Example**
* मान लो आपने Lambda का timeout 10 seconds रखा:
  * अगर function 7 seconds में complete हो गया → ✅ Success
  * अगर function 15 seconds लेता है → ❌ Timeout
* **IMP POINT**
* AWS Lambda में timeout को function configuration में set किया जाता है और इसका maximum limit 15 minutes (900 seconds) है।
<div style="page-break-before: always;"></div>


### **What is Lambda Concurrency?**
* Lambda concurrency is the number of Lambda function invocations that are running simultaneously at a given time. AWS Lambda automatically creates execution environments to handle concurrent requests.
* **IN HINDI:-**
* Lambda concurrency का मतलब है कि किसी समय पर कितने Lambda function invocations (executions) एक साथ चल रहे हैं।
* मान लो आपकी Lambda function को एक साथ 100 requests आती हैं: अगर सभी requests एक साथ process हो रही हैं, तो concurrency = 100 होगी।
* अगर requests बढ़ती हैं:
  * Lambda जरूरत के अनुसार multiple execution environments create करके concurrent requests को handle कर सकता है।
<div style="page-break-before: always;"></div>

### **What is Lambda Layer?**
* AWS Lambda Layer is a reusable package that contains libraries, dependencies, custom runtime components, or shared code. We can attach the same layer to multiple Lambda functions, which helps reduce duplication and makes dependency management easier
* **IN HINID:-**
* AWS Lambda Layer एक package है जिसमें हम reusable code, libraries, dependencies या configuration files रख सकते हैं, जिन्हें multiple Lambda functions में share किया जा सकता है।
* **EXAMPLE:-**
* मान लो आपके पास 5 Lambda functions हैं और सभी को pandas library चाहिए।
* हर Lambda में pandas अलग-अलग package करने के बजाय, आप उसे एक Lambda Layer में रख सकते हैं।
```python
              Lambda Layer
          ┌─────────────────┐
          │ pandas          │
          │ common utilities│
          │ shared libraries│
          └────────┬────────┘
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
   Lambda 1    Lambda 2    Lambda 3
```

#### Benefits
* Code reuse — same dependency multiple functions में
* Less duplication — libraries बार-बार package नहीं करनी पड़तीं
* Easy dependency management
* Smaller deployment packages
* Multiple Lambda functions में shared libraries

#### How do you create a Lambda Layer?
1. Dependencies install करो
```python
mkdir python
pip install requests -t python/
```
* Important: Python Lambda Layer में dependencies आमतौर पर python/ directory के अंदर रखी जाती हैं।

2. ZIP बनाओ
```python
zip -r lambda-layer.zip python/

# Structure
lambda-layer.zip
└── python/
    └── requests/
        └── ...
``` 

3. AWS Console में Layer create करो
* AWS Console → Lambda → Layers → Create layer
  * Layer name: my-python-layer
  * ZIP file upload करो
  * Compatible runtime select करो, जैसे Python 3.x
  * Create पर click करो

4. Lambda function में Layer attach करो
```python
Lambda Function
      ↓
Layers
      ↓
Add a layer
      ↓
Custom layers
      ↓
my-python-layer
      ↓
Add
```


<!-- What is serverless?
How does AWS Lambda work?
What are Lambda triggers?
What is a Lambda function?
Lambda vs EC2?
What is Lambda cold start?
What is Lambda timeout?
What is Lambda concurrency?
What is Lambda Layer?
How do you deploy a Lambda function?
How do you monitor Lambda?
How can Lambda connect to a database?
What is API Gateway + Lambda?
What are Lambda environment variables?
What are Lambda limitations? -->