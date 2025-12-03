### What is a Docker Container?
- A container is a running instance of an image.

3. Docker Container Commands (Container = Running App)
Command	What it Does
docker ps	Show running containers
docker ps -a	Show all containers
docker run nginx	Create + start container
docker run -d nginx	Run in background
docker run -p 8080:80 nginx	Port mapping (host → container)
docker run --name mycon nginx	Run with custom name
docker run -it ubuntu bash	Run in interactive mode
docker stop con_id	Stop container
docker start con_id	Start stopped container
docker restart con_id	Restart container
docker rm con_id	Delete container
docker rm -f con_id	Force delete running container
docker rm $(docker ps -aq)	Delete all containers

✅ Interview Line:

Container is a running instance of an image.