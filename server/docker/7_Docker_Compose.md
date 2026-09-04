|  No.  | Docker Compose                                            |
| :---: | --------------------------------------------------------- |
|       | [What is a Docker Compose?](#what-is-docker-compose)      |
|       | [Benefits of Docker Compose](#benefits-of-docker-compose) |

### 🐳 **What is Docker Compose?**
* Docker Compose is a tool used to define and run multiple Docker containers using a single YAML file (docker-compose.yml).
* Instead of running many docker run commands manually, you can define all services in one file and start them together.
* **HINDI:-** Docker Compose ka use multiple containers ko ek saath manage karne ke liye hota hai.

#### Example
```bash
# Example
Agar aapki application me:
* FastAPI App
* MySQL Database
* Redis

ye sab containers hain, to ek hi file (docker-compose.yml) se sabko start kar sakte ho.

Example:
version: '3'

services:
  app:
    build: .
    ports:
      - "8000:8000"

  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
Commands:
docker-compose up
docker-compose up -d
docker-compose down
```


#### Benefits of Docker Compose
* Manage multiple containers together
* Single configuration file
* Easy startup and shutdown
* Automatic networking between services
* Ideal for development and testing

```bash
services:
  web:
    image: nginx
    ports:
      - "8080:80"

  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
```

### Docker compose
```docker
docker compose -f file_name.yaml up -d
docker compose -f file_name.yaml down
```