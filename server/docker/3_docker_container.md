|  No.  | [Docker container](#docker-container)                                              |
| :---: | ---------------------------------------------------------------------------------- |
|       | [What is a Docker Container?](#-what-is-a-docker-container)                        |
|       | [Show running containers?](#show-running-containers)                               |
|       | [Show all running containers?](#list-all-containers-running--stopped)              |
|       | [Run Interactive Mode](#-run-interactive-mode)                                     |
|       | [Explain of -it](#-explain-of--it)                                                 |
|       | [Delete Docker container](#removedelete-container)                                 |
|       | [container logs](#container-logs)                                                  |
|       | [diff between docker rm and docker rmi](#diff-between-docker-rm-and-docker-rmi)    |
|       | [Diff between Docker Image vs Container?](#diff-between-docker-image-vs-container) |


<div style="page-break-before: always;"></div>

### 🎯 **What is a Docker Container?**
* A Docker Container is a **lightweight**, **isolated runtime environment** that packages an application along with its dependencies, libraries, and configurations, ensuring consistent execution across different environments.

### 🎯 **List Containers**
### **Show running containers**
```bash
docker ps
docker container ls

# List All Containers (Running + Stopped)
docker ps -a    
docker container ls -a
```

### 🎯**Image to container/create Container**
```bash
docker Container run image_id/image_name
docker Container run nginx
```

### **Run in background**
### **container run in background/detached mode**
* docker run -d image_name में -d का मतलब है detached mode।
* -d (detached mode) का मतलब है कि कंटेनर background में चलेगा।
* आप कंटेनर को स्टार्ट करेंगे, लेकिन उसका टर्मिनल या आउटपुट आपके स्क्रीन पर नहीं दिखेगा।
* कंटेनर अपने आप काम करता रहेगा और आप अपना टर्मिनल फ्री रख सकते हैं।
```bash
docker container run -d nginx 
```
* ये कमांड Nginx वेब सर्वर कंटेनर को बैकग्राउंड में रन करता है।
* आप कंटेनर के लॉग देखने के लिए बाद में docker logs <container_id> चला सकते हैं।
* या कंटेनर को मैनेज करने के लिए docker ps से कंटेनर की लिस्ट देख सकते हैं।
* जब आपको कंटेनर को लगातार बैकग्राउंड में चलाना हो, जैसे कि वेब सर्वर, डेटाबेस, या कोई सर्विस।
* जब आपको कंटेनर के साथ इंटरैक्ट करने की जरूरत न हो, बल्कि वह अपने आप काम करता रहे।

#### Example
* In Docker, the **-e** option is used to set environment variables inside the container at runtime.
```docker
docker run -d --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:latest
```


### **Set environment variables in a container**
```docker
docker run -e <var_name>=<var_value> <container_name> (or <container_id)
```

### 🎯 **Run Interactive Mode**
### 🎯 **Explain of -it**
```docker
docker container run -it ubuntu bash
```
* तो इसमें -it दो ऑप्शन्स (flags) का मेल है:
  * -i (interactive):- इसका मतलब है कि कंटेनर का इनपुट (stdin) खुला रहेगा। यानी आप कंटेनर के अंदर टाइप कर सकेंगे, जैसे किसी कंप्यूटर पर कमांड टाइप करते हैं।
  * -t (tty) इसका मतलब है कि एक टर्मिनल (terminal) बनाया जाएगा। ये टर्मिनल आपके लिए इंटरैक्टिव (interactive) सेशन जैसा अनुभव देगा, मतलब स्क्रीन पर आउटपुट साफ़ दिखेगा और आप कमांड लिख सकेंगे।

#### **क्यों use करते हैं -it?**
* अगर आप सिर्फ docker run ubuntu लिखेंगे, तो कंटेनर चलेगा, लेकिन आप उसके अंदर सीधे कमांड टाइप नहीं कर पाएंगे। कंटेनर के अंदर इंटरैक्टिवली काम करने के लिए आपको -it देना पड़ता है ताकि आप कंटेनर में एक टर्मिनल खोलकर कमांड चला सकें।
* **मतलब:** -it से आप कंटेनर के अंदर सीधे बैठकर कमांड चला सकते हैं, जैसे कि आप अपने कंप्यूटर पर टर्मिनल में काम कर रहे हों।

#### उदाहरण 1: docker run ubuntu (बिना -it के)
* ये कमांड Ubuntu कंटेनर को रन करेगा, लेकिन आपको उसके अंदर इंटरैक्टिव शेल **(terminal) नहीं मिलेगा**।
* कंटेनर बिना टर्मिनल के चलता है और तुरंत बंद हो सकता है क्योंकि कोई कमांड नहीं दिया गया है जो कंटेनर को चलाए रखे।
* इसलिए आप कंटेनर के अंदर टाइप करके काम नहीं कर पाएंगे।

#### उदाहरण 2: docker run -it ubuntu
* ये कंटेनर को स्टार्ट करता है और एक टर्मिनल खोल देता है।
* आप कंटेनर के अंदर सीधे कमांड टाइप कर सकते हैं, जैसे कि bash शेल।
* उदाहरण के लिए, आप ls, pwd, या apt update जैसे कमांड चला सकते हैं।
* कंटेनर तब तक चलता रहेगा जब तक आप exit नहीं करते।

#### Port mapping (host → container)
* The first 8000 (before the colon) is the **host port** — the port on your computer.
* The second 8000 (after the colon) is the **container port** — the port inside the Docker container where your app is running.
* **-p** port mapping ke liye hota hai, while **-d** container ko detached/background mode me run karta hai.
```bash
docker container run -p 8080:80 nginx
docker container run -d -p 8080:80 nginx
```

#### Run with custom name
```bash
docker run --name <container_name> <image_name>
docker run --name mycontainer nginx
```

### **Start Container**
```docker
docker start container_id/container_name
```

### **Stop Container**
```docker
docker stop container_id/container_name
```

### **Restart Container**
```docker
docker restart container_id/container_name
```

### docker Pause
```bash
docker container pause cont_id
```

### docker unpause
```bash
docker container unpause cont_id
```

### Docker inactive mode
```bash
docker container kill cont_id
```

### Rename Container
```bash
# show the all conatiner
docker ps -a

# Rename container
docker container rename <old_name> <new_name>

# Container create karte waqt naam dena
docker run -d --name web_server nginx
```


### **Remove/delete Container**
```bash
# Step 1:- stop the container
docker stop <container_id_or_name>

# Step 2:- delete the container
docker rm container_id/container_name
```

* remove all containers
```bash
docker container rm <container_id_or_name> <container_id_or_name>
docker container prune # all container are deleted 
```

* Force Remove Running Container/stop and remove the container
```bash
docker rm -f con_id

# Delete all containers
docker rm $(docker ps -aq)
```

### **container logs**
```bash
docker container logs cont_id/cont_name
docker container logs -f cont_id # tarimanl ko hold rakehga
```

### Check stats
* mtb kitni memory le raha hai, kitna cpu hai
```bash
docker container stats --no-stream
```

### Docker Exec (Enter Inside Container)
```docker
docker exec -it container_id bash
docker exec -it container_id sh
```

### Docker Run and inspect
* mtb container ke andar jana hai
```bash
docker container run -d nginx:latest
# output mai container id milegi

# Now ab iske andar jana hai
docker inspect cont_id | grep -i ip
# Outpur isme ip milegi

# ab check kar
curl 172.17.0.2
# to ye hit ho jayega
```

### kaunse ports par services listen kar rahi hain?
* Haan, ye Linux command hai jo mainly check karti hai ki kaunse ports par services listen kar rahi hain.
```bash
netstat -tulpn | grep -i LIST
```

#### Breakdown
* -t → TCP connections
* -u → UDP connections
* -l → Listening ports
* -p → Process/PID information
* -n → Port ko number me show karta hai, name resolve nahi karta


### Work with ubuntu
```bash
docker container run -itd ubuntu:18.04

# create folder in local
mkdir m_folder

# create files inside folder
touch m_folder/files{1..10}.txt

# to check file go to m_folder
ls

# copy local file to container inside the temp folder
docker container cp m_folder cont_id:/temp

# to check file in container
docker container exec -it cont_id ls -lrth /temp/m_folder
```

### create image own container
```bash
docker container commit cont_id files:v1
```


### **Diff between docker rm and docker rmi?**
* docker **rm** is used to **remove containers**, whereas docker **rmi** is used to **remove Docker images**. A container is a running instance of an image, so generally the container must be removed before deleting the image.

### **Diff between Docker Image vs Container?**
#### Docker Image
* Read-only template.
* Contains application code, libraries, dependencies, and configuration.
* Used to create containers.
* Cannot run by itself.
* Created using a Dockerfile.
* Can be shared through Docker Hub or private registries.
* Example: nginx:latest, python:3.12

#### Docker Container
* Running instance of a Docker Image.
* Has its own process, network, and filesystem.
* Can be started, stopped, restarted, and deleted.
* Created from an image using docker run.
* Multiple containers can be created from the same image.
* Stores temporary runtime changes.
* Example: Running Nginx web server container.


#### Interview Answer (2 Lines)
* Docker Image is a **read-only template** that contains application code and dependencies. Docker **Container** is a **running instance of that image** where the application actually executes. 🚀

| Docker Image             | Docker Container          |
| ------------------------ | ------------------------- |
| Read-only template       | Running instance of image |
| Static                   | Dynamic                   |
| Created using Dockerfile | Created from image        |
| Cannot execute           | Executes application      |
