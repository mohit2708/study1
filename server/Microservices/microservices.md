### What are Microservices?
- Microservices एक software architecture style है जिसमें बड़ी application को छोटे-छोटे independent services में बाँट दिया जाता है।
- हर service अपना अलग काम करती है और API के through दूसरी services से बात करती है।

#### Example
- मान लो एक E-commerce app है।
- Monolithic में सब कुछ एक ही codebase में होगा (user, order, payment, product).
- लेकिन Microservices में:
  - User service
  - Product service
  - Order service
  - Payment service
  - सब अलग-अलग होंगे।
- हर service:
  - अलग database रख सकती है
  - अलग language में बन सकती है
  - independently deploy हो सकती है

#### Benifits
- छोटी-छोटी services → एक काम के लिए एक service
- Independent deployment → एक service बदलो, पूरी app deploy नहीं करनी
- Loose coupling → services एक-दूसरे पर ज़्यादा dependent नहीं
- API communication → HTTP / REST / Message queue से बात
- Team अलग-अलग service पर काम कर सकती है
- Fault isolation (एक service down हो तो पूरी app बंद नहीं)

#### Disadvantage
- Setup complex होता है
- Network calls ज़्यादा होती हैं → latency
- Monitoring और debugging मुश्किल
- DevOps knowledge चाहिए


### Monolithic in hindi
- Monolithic architecture एक ऐसा software design है जिसमें पूरी application का code
  - एक ही project
  - एक ही codebase
  - एक ही server
  - एक ही database में होता है।
- यानी सारा system एक साथ जुड़ा हुआ (single unit) होता है।
- Monolithic में ये सब एक ही application में लिखे होते हैं। अगर तुम्हें payment में छोटा सा change करना है तो 👉 पूरी application को फिर से build और deploy करना पड़ेगा।

#### Advantage
- Single codebase
- Single deployment
- Single database
- सारे modules tightly coupled होते हैं
- शुरुआत में बनाना आसान
- Testing simple होती है
- Performance अच्छा (internal calls, network नहीं)
- छोटे projects के लिए best

#### Disadvantage
- Code बहुत बड़ा हो जाता है
- एक छोटा change → पूरी app deploy
- Scaling मुश्किल (पूरी app scale करनी पड़ती है)
- एक bug → पूरी app crash हो सकती है

### What are Microservices?
- Microservices, also known as microservice architecture, is an architectural style that structures an application as a collection of small, **independent services**. 
- Each service is designed to perform a specific business capability and can be developed, tested, deployed, and scaled independently of other services in the application.

#### In a microservices-based system, each service:
1. Has its own codebase and repository.
2. Is built using a specific programming language, framework, or technology stack.
3. Exposes APIs (Application Programming Interfaces) for communication with other services.
4. Has its own database schema or data storage mechanism.
5. Can be deployed independently on different servers, containers, or cloud platforms.

### The benefits of microservices include:
1. **Scalability:** Each service can be scaled independently to handle increased traffic or demand.
2. **Flexibility:** Services can be written in different programming languages and use various technology stacks.
3. **Resilience:** If one service experiences issues, it won't bring down the entire application.
4. **Easier maintenance:** Each service has a smaller codebase, making it easier to maintain and update.

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