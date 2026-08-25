### What is Kubernetes?
* Kubernetes is an **open-source container orchestration platform** used to automate the deployment, scaling, load balancing, and management of containerized applications.
* **HINDI:-** Kubernetes (K8s) ek container orchestration platform hai jo Docker containers ko manage, deploy, scale aur monitor karne ke liye use hota hai.
* Simple words mein:
  * Docker ek container banata hai.
  * Kubernetes bahut saare containers ko manage karta hai.


#### Why Kubernetes?
* Auto Scaling – Load ke according containers increase/decrease
* Self Healing – Failed container automatically restart
* Load Balancing – Traffic distribute karta hai
* Rolling Updates – Downtime ke bina deployment
* Service Discovery – Services ko locate karna easy


#### Real-Life Example
* Maan lo aapke paas ek e-commerce application hai:
  * 5 containers → Backend
  * 3 containers → Frontend
  * 2 containers → Database
* Agar koi container crash ho jaye to Kubernetes:
  * ✅ Automatically restart kar dega
  * ✅ Traffic ko healthy containers par bhej dega
  * ✅ Load badhne par naye containers create kar dega
  * ✅ Load kam hone par containers reduce kar dega

### Difference Between Docker and Kubernetes
| Docker                              | Kubernetes                                     |
| ----------------------------------- | ---------------------------------------------- |
| Containerization platform           | Container orchestration platform               |
| Container create aur run karta hai  | Containers ko manage karta hai                 |
| Single machine par chal sakta hai   | Multiple machines (cluster) manage karta hai   |
| Auto-scaling nahi                   | Auto-scaling support karta hai                 |
| Self-healing nahi                   | Failed containers ko restart karta hai         |
| Basic networking                    | Advanced networking & load balancing           |
| Small applications ke liye suitable | Large production environments ke liye suitable |
