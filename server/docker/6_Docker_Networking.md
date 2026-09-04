|  No.  | Docker Networking                                          |
| :---: | ---------------------------------------------------------- |
|       | [What is a Docker Networking?](#-what-is-docker-networking) |
|       | [Why Docker Networking?](#why-docker-networking)           |
|       | [Types of Docker Networks](#types-of-docker-networks)      |

### 🌐 **What is Docker Networking?**
* Docker Networking allows Docker containers to communicate with:
  * Other containers
  * The Docker host machine
  * External networks (Internet)
* By default, every container gets its own isolated network namespace, IP address, and network interfaces.
* Docker Networking containers ko ek dusre se communicate karne ki facility deta hai.

#### Example
* Suppose you have:
  * Container A → FastAPI App
  * Container B → MySQL Database
* Docker networking allows FastAPI to connect to MySQL using the container name instead of an IP address.
```bash
mysql://root:password@mysql_container:3306/mydb
```

### Why Docker Networking?
* Container-to-container communication
* Access applications from browser
* Connect containers to databases
* Isolate different applications

### Types of Docker Networks

1. **Bridge Network (Default)**
* Bridge is the default Docker network that enables communication between containers running on the same host.
* When you create a container without specifying a network, Docker uses the bridge network.
* Single host par containers ko connect karta hai.

```bash
docker run -d nginx
# or
docker run -d --network bridge nginx

# Check networks:
docker network ls

# Output:-
NETWORK ID     NAME      DRIVER
xxxxxx         bridge    bridge
xxxxxx         host      host
xxxxxx         none      null
```

2. Host Network
* Container shares the host's network stack.
* No separate container IP is created.
* Container host machine ka network use karta hai.
```bash
docker run --network host nginx
```
* Advantage:
  * Better performance
* Disadvantage:
  * Less isolation


3. None Network
* Container has no network access.
* Used for maximum isolation.
* No network access.
```bash
docker run --network none nginx
```

4. Custom Bridge Network
* Most commonly used in real projects.
* Create network:
```bash
docker network create my-network
```
* Run containers:
```bash
docker run -d --name mysql --network my-network mysql

docker run -d --name fastapi --network my-network myapp
```

5. Overlay Network
* Multiple Docker hosts ke containers connect karne ke liye.
```bash
Docker Swarm me use hota hai.
```

* Now FastAPI can access MySQL using:
```bash
mysql:3306

# without knowing the IP address.
```


#### List all networks
```docker
docker network ls
```

#### Create a network
```docker
docker network create <network_name>
```

#### Remove a network
```
docker network rm <network_name>
```

#### Remove all unused networks
```docker
docker network prune
```



```


```