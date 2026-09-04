# 🎯 [Docker Interview Questions](/server/docker/)
### 🧠 [**Docker Basic Questions**](/server/docker/1_docker_basic.md)
1. [What is **docker**?](/server/docker/docker_basic.md#what-is-docker)
2. Why Docker is Used?
3. Advantages of Docker?
4. Docker Installation?
5. TO check version?
6. Check the all docker Commands
7. Difference Between Docker and Virtual Machine?

### 🧠 [**Docker images Questions**](/server/docker/2_docker_images.md)
1. What is a Docker Image?
2. list all images?
3. Download/Pull image from Docker Hub
4. Delete Docker Image
5. What Are Docker Image Layers?
6. How do you create a Docker image?
7. we upload the image on docker hub?

### 🧠 [**Docker container Questions**](/server/docker/3_docker_container.md)
1. What is a Docker Container?
2. Show running containers?
3. Image to container?
4. create Container?
5. container run in background/detached mode
6. Run Interactive Mode
7. Explain of -it
8. Port mapping (host → container)
9. Run with custom name
10. Start Container
11. Stop Container
12. Restart Container
13. Pause Container
14. unpause container
15. inactive mode Container
16. Rename Container
17. Remove Container
18. container logs
19. Check stats
20. Docker Exec (Enter Inside Container)
21. Docker Run and inspect
22. diff between docker rm and docker rmi
23. Difference between Image and Container?

### 🧠 [**Docker Volume Questions**](/server/docker/4_Docker_Volume.md)
1. What is a Docker Volume?
2. Why do we need Volumes?
3. Create a Volume
4. Check Volume
5. Container run with volume?
6. What is Data Persistence?
7. How do you mount a volume to a container?
8. Difference between Volume and Bind Mount?
9. Volume example with mysql?

### 🧠 [**Docker registary Questions**](/server/docker/5_docker_registary.md)
1. What is docker registary?

### 🧠 [**Docker Networking Questions**](/server/docker/6_Docker_Networking.md)
1. What is a Docker Networking?
2. Why Docker Networking?
3. Types of Docker Networks?
   1. What is Bridge Network?
   2. What is Host Network?
   3. What is Overlay Network?
   4. What is None Network?

### 🧠 [**Docker Compose Questions**](/server/docker/7_Docker_Compose.md)
1. What is a Docker Compose?
2. Benefits of Docker Compose?

### 🧠 [**Docker inspect Questions**](/server/docker/8_Docker_Inspect.md)
1. What is docker inspect?


```bash
Interview Answer:

Docker Networking allows containers to communicate with each other and with external systems through different network drivers such as bridge, host, overlay, and none.

⚔️ Dockerfile vs Docker Compose
Feature	Dockerfile	Docker Compose
Purpose	Image create karna	Multiple containers run karna
File Name	Dockerfile	docker-compose.yml
Use For	Build image	Manage services
Contains	Build instructions	Service definitions
Command	docker build	docker-compose up
Multiple Containers	❌ No	✅ Yes
Dockerfile Example
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

👉 Ye image banata hai.

Docker Compose Example
services:
  app:
    build: .

  db:
    image: mysql:8

👉 Ye app aur db dono containers ko run karta hai.

Interview One-Liner

Dockerfile

Dockerfile is used to create a Docker image by defining build instructions.

Docker Compose

Docker Compose is used to run and manage multiple containers using a single YAML file.

Docker Networking

Docker Networking enables communication between containers and external networks using network drivers like bridge, host, and overlay.
```





# saf
* delete the container first related to image
```docker
docker rmi nginx
docker rmi IMAGE_ID # Delete image by ID
docker rmi mohit2708/myfastapiapp:latest  # delete with specific name
docker rmi -f IMAGE_ID  # Force delete
docker image prune    # Remove unused images
docker rmi $(docker images -q)  # Delete all images
```


#### Create/build image from Dockerfile
- -t = tag
- . = Current Directory
```docker
docker build -t myapp .

# Download a specific version
docker build -t myapp:v1 .

#build without cache
docker build -t <image_name>:<version> . -no-cache
```


### Docker all comands
```bash

```


Command	Use
docker logs con_id	View container logs
docker logs -f con_id	Live logs
docker stats	CPU, RAM usage
docker top con_id	Running processes inside container
docker inspect con_id	Full JSON details of container



#### 🧾 **What kind of information does it show?**
* For a container, it shows:

| Info Type         | Description                                      |
| ----------------- | ------------------------------------------------ |
| `Config`          | The original config used to create the container |
| `State`           | Is it running, paused, or exited                 |
| `Mounts`          | Volumes attached                                 |
| `NetworkSettings` | IP address, ports, bridge info                   |
| `Env`             | Environment variables                            |
| `Image`           | Image ID used to start container                 |
| `Path`, `Args`    | The command used to start the container          |
| `RestartCount`    | How many times it's been restarted               |

#### Example:-
```bash
docker inspect my-container


[
  {
    "Id": "a1b2c3d4...",
    "State": {
      "Status": "running",
      "Running": true,
      "StartedAt": "2025-06-20T10:20:00Z"
    },
    "NetworkSettings": {
      "IPAddress": "172.17.0.2"
    },
    "Mounts": [
      {
        "Type": "volume",
        "Name": "my-volume",
        "Destination": "/data"
      }
    ]
  }
]

```

#### 🔧 Real-World Uses

### Project Setup through docker

### **Build the Docker image file**
```docker
docker build -t myfastapiapp .
```


<!-- 🧰 🧱 🪵 🧪 🧯 📜 🔎 🧹 💣 🛑 ❌ 👉 👈 🧠 ✅ 📌 🔧 🔍 -->

# Docker troubleshooting commands


### **Get Inside a Running Container (Debug)**
```bash
docker exec -it <container_name> bash

# Or use sh if bash is not available:
docker exec -it <container_name> sh

```

### Dockerizing our app
```docker
FROM    # project run karne ke liye s/w requiments like node, pyhon
WORKDIR
COPY
RUN
CMD
EXPOSE
ENV
```

### Publising Images
```docker
docker build -t devapnacollege/testapp  # image build

# Login docker
docker login -u <username>

docker push devapnacollege/testapp  # push in docker
```


```bash
What is Docker Engine?
What is Docker Hub?
What is containerization?
Docker Architecture
Explain Docker Architecture.
What are Docker Client and Docker Daemon?
What is container runtime?
How does Docker communicate with the OS kernel?
What is the role of namespaces and cgroups in Docker?
What is a Dockerfile?
How do you create a Docker image?
What is the docker build command?
What is the difference between COPY and ADD?
What is the difference between CMD and ENTRYPOINT?
Difference between RUN, CMD, and ENTRYPOINT?
What is image layering?
How do Docker image layers work?
How do you reduce Docker image size?
What is Multi-Stage Build?
Docker Containers
How do you create a container?
How do you start, stop, and restart a container?
Difference between docker run and docker start?
How do you view running containers?
How do you access a running container?
What is detached mode (-d)?
What is interactive mode (-it)?
How do containers communicate with each other?
What is Port Mapping?
Difference between EXPOSE and Publish Port (-p)?
Difference between Volume and Bind Mount?
What is data persistence?
How do you mount a volume to a container?
Docker Compose
What is Docker Compose?
Why do we use Docker Compose?
What is a docker-compose.yml file?
How do you start services using Docker Compose?
Difference between Docker and Docker Compose?
How do multiple containers communicate in Compose?

Docker Commands
docker ps
docker images
docker pull
docker push
docker build
docker run
docker stop
docker start
docker restart
docker logs
docker exec
docker inspect
docker system prune
Docker Security
How is Docker secure?
What are Docker namespaces?
What are cgroups?
What is the principle of least privilege?
Why should containers not run as root?
How do you scan Docker images for vulnerabilities?

Scenario-Based Questions
A container stops immediately after starting. Why?
How would you debug a failing container?
How do you check container logs?
A container cannot connect to the database. How would you troubleshoot?
How do you share data between containers?
How do you deploy a Django/FastAPI application using Docker?
How do you containerize a Python application?
How would you update an application without downtime?
Python/FastAPI Related Docker Questions
How do you Dockerize a FastAPI application?
Why is Uvicorn used inside a Docker container?
How do you connect FastAPI and MySQL containers?
How do you pass environment variables to Docker containers?
What is a .env file in Docker?
How do you run database migrations in Docker?
How do you use Docker Compose with FastAPI and MySQL?

Frequently Asked Interview Questions
Difference between Docker and Kubernetes?
What problem does Docker solve?
What happens when you run docker run nginx?
What is the difference between a container and a VM?
Why is Docker faster than a VM?
What is a Docker Layer Cache?
What is a Docker Volume and when would you use it?
How do you optimize Docker image size?
What is the purpose of Docker Compose?
Explain the complete Docker lifecycle from Image → Container.
```