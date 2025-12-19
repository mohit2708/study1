### What is a Docker Container?
### Docker Container Command
#### List Running Containers
- Container is a running instance of an image.
```docker
# Show running containers
docker ps

# List All Containers (Running + Stopped)
docker ps -a    
```

#### create and Run a Container
#### Image to container
```docker
docker run image_id/image_name
docker run nginx

# Run in background
docker run -d nginx 

# Port mapping (host → container)
docker run -p 8080:80 nginx

# Run with custom name
docker run --name <container_name> <image_name>
docker run --name mycontainer nginx
```

#### Run Interactive Mode
```docker
docker run -it ubuntu bash
```

#### Stop Container
```docker
docker stop container_id/container_name
```

#### Start Container
```docker
docker start container_id/container_name
```

#### Restart Container
```docker
docker restart container_id/container_name
```

#### Remove Container
```docker
# Step 1:- stop the container
docker stop <container_id_or_name>

# Step 2:- delete the container
docker rm container_id/container_name

# Force Remove Running Container/stop and remove the container
docker rm -f con_id

# Delete all containers
docker rm $(docker ps -aq)
```

#### Docker Exec (Enter Inside Container)
```docker
docker exec -it container_id bash
docker exec -it container_id sh
```
