### Docker Image Commands
#### List all local images
```docker
docker images
docker image ls
```

#### Download image from Docker Hub
```docker
docker pull nginx
docker pull hello-world
docker pull mysql

# Download a specific version
docker pull python:3.12
docker pull mysql:8.0
```

#### Create/build image from Dockerfile
- -t = tag
- . = Current Directory
```docker
docker build -t myapp .

# Download a specific version
docker build -t myapp:v1 .
```

### Delete image
* delete the container first related to image
```docker
docker rmi nginx
docker rmi IMAGE_ID # Delete image by ID
docker rmi mohit2708/myfastapiapp:latest  # delete with specific name
docker rmi -f IMAGE_ID  # Force delete
docker image prune    # Remove unused images
docker rmi $(docker images -q)  # Delete all images
```