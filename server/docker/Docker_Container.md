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

#### Run a Container
```docker
docker run nginx

# Run in background
docker run -d nginx 

# Port mapping (host → container)
docker run -p 8080:80 nginx

# Run with custom name
docker run --name mycontainer nginx
```

#### Run Interactive Mode
```docker
docker run -it ubuntu bash
```

#### Stop Container
```docker
docker stop container_id
```

#### Start Container
```docker
docker start container_id
```

#### Restart Container
```docker
docker restart container_id
```

#### Remove Container
```docker
docker rm container_id

# Force Remove Running Container
docker rm -f con_id

# Delete all containers
docker rm $(docker ps -aq)
```


#### Docker Exec (Enter Inside Container)
```docker
docker exec -it container_id bash
docker exec -it container_id sh
```
