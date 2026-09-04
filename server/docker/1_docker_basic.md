|  No.  | Questions                                                                                        |
| :---: | ------------------------------------------------------------------------------------------------ |
|       | [What is Docker?](#what-is-docker)                                                               |
|       | [Docker Installation?](#docker-installation)                                                     |
|       | [Why Docker is Used?](#why-docker-is-used)                                                       |
|       | [Advantages of Docker?](#advantages-of-docker)                                                   |
|       | [TO check version?](#to-check-version)                                                           |
|       | [Check the all docker Commands](#check-the-all-docker-commands)                                  |
|       | [Difference Between Docker and Virtual Machine?](#difference-between-docker-and-virtual-machine) |
<div style="page-break-before: always;"></div>

### **What is Docker**
* Docker is an open-source platform that allows developers to package, deploy, and run applications as containers. A container is a lightweight, portable environment that houses an application and all of its dependencies.
* The application can be run anywhere (Windows, Linux, Cloud) in the same way.
* We can run code and dependencies in containers without installing them directly on your system.
* 
* Docker is an **open-source containerization platform** that allows developers to package, deploy, and run applications inside containers.
* A container is a lightweight, portable, and isolated(Isolated ka matlab hota hai alag ya separate environment me chalna) environment that contains an application along with all its required dependencies, libraries, and configurations.
* Docker ensures that the application runs consistently across different environments such as Windows, Linux, and cloud platforms.
* It allows us to run applications and their dependencies inside containers without installing those dependencies directly on the host operating system.

#### Why Docker is Used?
1. Consistent Environment
2. Dependency Management
3. Easy Deployment
4. Faster Startup
5. Scalability
6. Isolation
7. CI/CD Integration

#### Advantages of Docker
1. Lightweight
2. Fast Startup
3. Portability
4. Consistency
5. Efficient Resource Utilization
6. Easy Scaling
7. Isolation
8. Simplified Dependency Management
9. Better CI/CD
10. Microservices Friendly


### **Docker Installation**
* search **get docker** on google (OR) hit "https://docs.docker.com/get-started/get-docker/"
* click on Docker desktop for window then click on **Docker Desktop for Windows - x86_64**

#### **TO check version**
- Shows installed Docker version
```docker
docker --version
docker -v
```
- Shows client + server version
```docker
docker version
```
- Shows full system info (images, containers, CPU, storage, etc.)
```docker
docker info
```

#### **Check the all docker Commands**
```docker
# opne cmd
docker
```

### **Difference Between Docker and Virtual Machine**
* Docker host OS ka kernel(Kernel Operating System ka core (heart) hota hai jo hardware aur software ke beech communication karwata hai.) share karta hai, jabki VM har instance ke liye alag Guest OS chalata hai.
* Docker lightweight hota hai, jabki VM heavy hoti hai.
* Docker seconds me start ho jata hai, VM ko start hone me zyada time lagta hai.
* Docker kam RAM aur CPU use karta hai, VM zyada resources consume karti hai.
* Docker me containers run hote hain, VM me virtual machines run hoti hain.
* Docker ki performance generally better hoti hai kyunki full OS load nahi hota.
* VM stronger isolation provide karti hai kyunki har VM ka apna OS hota hai.
* Docker applications ko package aur deploy karne ke liye use hota hai, VM poora operating system virtualize karti hai.