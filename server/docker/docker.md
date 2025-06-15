|  No.  | Questions                          |
| :---: | ---------------------------------- |
|       | [What is Docker?](#what-is-docker) |

### **What is Docker**
* Docker is an open-source platform that allows developers to package, deploy, and run applications as containers. A container is a lightweight, portable environment that houses an application and all of its dependencies.
* The application can be run anywhere (Windows, Linux, Cloud) in the same way.* We can run code and dependencies in containers without installing them directly on your system.

### **Docker Installation**
* search **get docker** on google (OR) hit "https://docs.docker.com/get-started/get-docker/"
* click on Docker desktop for window then click on **Docker Desktop for Windows - x86_64**

### Project Setup through docker

### **Build the Docker image file**
```docker
docker build -t myfastapiapp .
```
#### Show doker
```docker
docker images
```

#### Run the container
* The first 8000 (before the colon) is the host port — the port on your computer.
* The second 8000 (after the colon) is the container port — the port inside the Docker container where your app is running.
```docker
docker run -d -p 8000:8000 myfastapiapp
```
#### Check container list
```docker
# all Runing containers
docker ps
# see all containers (running or stopped):
docker ps -a
```
#### Stoped the container
```docker
docker stop container_id
```

#### Delete the container
```docker
# Step 1:- stop the container
docker stop <container_id_or_name>
# Step 2:- delete the container
docker rm <container_id_or_name>
(OR)-- stop and remove the container-- -f forces the stop then removes the container.
docker rm -f <container_id_or_name>
(OR)-- Remove all stopped containers at once-- prune:- It removes things like stopped containers, unused networks, dangling images, or unused volumes.docker container prune
```
### Upload the image on docker hub
```docker
-- TO check login is correct
docker login
-- your-dockerhub-username : mohit2708
docker tag myfastapiapp <your-dockerhub-username>/myfastapiapp:latest
docker push <your-dockerhub-username>/myfastapiapp:latest
```

### TO check version
```docker
# opne cmd
docker -v
```

### Create doker image
```docker
docker pull hello-world
```
### Show doker
```docker
docker images
```
### Delte the images
```docker
docker rmi IMAGE_ID
(OR)docker rmi mohit2708/myfastapiapp:latest
-- Force delete
docker rmi -f IMAGE_ID
```

### image to container
```docker
docker run image_id/REPOSITORY_name
```