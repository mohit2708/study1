|  No.  | [Docker Volume](#docker-container)                                                     |
| :---: | -------------------------------------------------------------------------------------- |
|       | [What is a Docker Volume?](#what-is-a-docker-volume)                                   |
|       | [Why do we need Volumes?](#why-do-we-need-volumes)                                     |
|       | [Create a Volume](#create-a-volume)                                                    |
|       | [Volume list](#volume-list)                                                            |
|       | [Delete a volume](#delete-a-volume)                                                    |
|       | [Container run with volume](#container-run-with-volume)                                |
|       | [What is Data Persistence?](#what-is-data-persistence)                                 |
|       | [How do you mount a volume to a container?](#how-do-you-mount-a-volume-to-a-container) |
|       | [Difference between Volume and Bind Mount?](#difference-between-volume-and-bind-mount) |
|       | [Volume example with mysql](#volume-example-with-mysql)                                |
<div style="page-break-before: always;"></div>


### **What is a Docker Volume?**
* Docker Volume is a mechanism to store data permanently outside the container.
* Normally, when a container is deleted, all data inside that container is lost. A Volume keeps the data safe even if the container stops or is removed.
* **HINDI:-** Docker Volume ek aisi storage jagah hai jahan container ka data permanently store hota hai.
* **HINDI:-** Agar aap container ke andar data save karte hain aur baad me container delete ho jata hai, to uska data bhi delete ho jata hai. Lekin agar data Volume me store hai, to container delete hone ke baad bhi data safe rehta hai.

#### Why do we need Volumes?
* **Persistent data storage:-** Container delete hone ke baad bhi data safe rehta hai.
* **Container Recreation:-** Agar container crash ho jaye ya naya container create karna pade, to purana data volume se wapas mil jata hai.
* **Data Sharing:-** Ek hi volume ko multiple containers use kar sakte hain.
* **Backup and Restore:-** Volumes ka backup lena aur restore karna aasaan hota hai.
* **Better Data Management:-** Application code aur data ko alag rakhne mein help karta hai.
* Data survives container deletion
* Share data between multiple containers
* Better performance than storing data inside containers
* OR
* Data persistence: When a container is removed, its writable layer is deleted too, so data stored inside the container disappears. Volumes keep the data intact.
* Sharing data: Volumes let you share data between multiple containers.
* Performance: Volumes are generally more efficient than storing data inside the container’s filesystem.
* Backup and migration: Volumes can be backed up or migrated more easily than container data.
* डेटा सुरक्षित रखना: अगर आप कोई कंटेनर बंद या हटा देते हो, तो कंटेनर के अंदर जो भी डेटा होता है, वो चला जाता है। लेकिन अगर वो डेटा volume में रखा हो, तो वो सुरक्षित रहता है।
* डेटा शेयरिंग: एक volume को एक से ज्यादा कंटेनर में शेयर किया जा सकता है।
* बैकअप और ट्रांसफर करना आसान: Volume का डेटा होस्ट मशीन पर होता है, इसलिए इसका बैकअप लेना या दूसरे सिस्टम पर ट्रांसफर करना आसान होता है।
* फास्ट और सुरक्षित: Docker volume, कंटेनर के फाइल सिस्टम के मुकाबले ज्यादा तेज और सुरक्षित होता है।

### Create a Volume
```bash
docker volume create vol_name
```

### Volume list
```bash
docker volume ls

# Output:-
DRIVER    VOLUME NAME
local     myvolume
```

### **Delete a volume**
```docker
docker volume rm <volume_name>

# Remove unused local volumes
docker volume prune //for anonymous volumes
```

### Container run with volume
```bash
# Pehle volume create karo:
docker volume create mysql-data

# then run
docker run -d --name mysql-container -v mysql-data:/var/lib/mysql mysql
```

#### Alternative: Docker automatically Volume create kar sakta hai
```bash
docker run -d --name mycontainer -v myvolume:/app/data nginx
# Docker myvolume ko automatically create kar dega.
```

### What is Data Persistence?
* Data persistence means keeping data available even after an application, server, or container is stopped, restarted, or deleted. In Docker, volumes and bind mounts are commonly used for data persistence.
* HINDI:- Data Persistence ka matlab hai ki data ko permanently save rakhna, taaki application, server ya container stop/restart/delete hone ke baad bhi data available rahe.

### How do you mount a volume to a container?
* Docker Volume ko container ke saath attach/mount karne ke liye **-v** ya **--mount** option use karte hain.
1. Using -v — Simple & Common
```bash
docker run -d --name mycontainer \
-v myvolume:/app/data \
nginx


# Explain
-v myvolume:/app/data
   │        │
   │        └── Container ke andar ka path
   └─────────── Docker Volume

# Matlab myvolume ka data container ke /app/data folder mein available hoga.
```

2. Using --mount
* Same kaam:
```bash
docker run -d --name mycontainer \
--mount source=myvolume,target=/app/data \
nginx
```

### Difference between Volume and Bind Mount?
* Docker khud storage location manage karta hai.
| Feature          | Docker Volume                    | Bind Mount                             |
| ---------------- | -------------------------------- | -------------------------------------- |
| Managed By       | Docker                           | Host OS                                |
| Storage Location | Docker decides location          | User specifies exact path              |
| Easy to Use      | ✅ Yes                            | ⚠️ Slightly complex                     |
| Portability      | ✅ Better                         | ❌ Less portable                        |
| Performance      | ✅ Optimized by Docker            | Depends on host filesystem             |
| Share Host Files | ❌ Not directly                   | ✅ Yes                                  |
| Common Use       | Databases, logs, persistent data | Development, config files, source code |


### Volume example with mysql
* pull mysql
```bash
docker image pull mysql:latest
```

* check karo 
```bash
docker images

# Output:- 
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
mysql        latest    xxxxxxxx       ...            ...
```

* Docker Volume Create karo
```bash
docker volume create mysql-data

# Check
docker volume ls
DRIVER    VOLUME NAME
local     mysql-data
```

* MySQL Container Run karo
```bash
docker run -d \
  --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=root123 \
  -v mysql-data:/var/lib/mysql \
  mysql

# Output:-
a7f8c9d1234567890abcdef...
```

* Check Container
```bash
docker ps

# Output:-
CONTAINER ID   IMAGE   COMMAND                  STATUS         PORTS     NAMES
a7f8c9d12345   mysql   "docker-entrypoint..."   Up 10 seconds  3306/tcp  mysql-container
```

* Volume Container mein Mount Hua ya Nahi Check karo
```bash
docker inspect mysql-container

"Mounts": [
    {
        "Type": "volume",
        "Name": "mysql-data",
        "Destination": "/var/lib/mysql"
    }
]
```

* MySQL ke andar Login karke Database Create karo
```bash
docker exec -it mysql-container mysql -uroot -p

# password
root123

# Ab MySQL prompt milega:
mysql>SHOW DATABASES;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| testdb             |
+--------------------+
```