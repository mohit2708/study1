|  No.  | [Docker images](#docker-images)                                             |
| :---: | --------------------------------------------------------------------------- |
|       | [list all images?](#list-all-local-images)                                  |
|       | [Download/Pull image from Docker Hub](#downloadpull-image-from-docker-hub)  |
|       | [Delete Docker Image](#delete-docker-image)                                 |
|       | [What Are Docker Image Layers?](#what-are-docker-image-layers)              |
|       | [How do you create a Docker image?](#how-do-you-create-a-docker-image)      |
|       | [we upload the image on docker hub](#now-we-upload-the-image-on-docker-hub) |

<div style="page-break-before: always;"></div>

### 🎯 **What is a Docker Image?**
* A Docker Image is a **read-only template** that contains everything needed to run an application, such as:
  * Application code
  * Runtime (Python, Java, Node.js, etc.)
  * Libraries and dependencies
  * Environment variables
  * Configuration files
* When you run an image, Docker creates a Container from it.

### Ek hi image se multiple containers create kiye ja sakte hain.
```bash
nginx Image
   │
   ├── Container 1
   ├── Container 2
   └── Container 3
```

### 🎯**List all local images**
```bash
docker images
# (OR) 
docker image ls

# Output:-
REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
myapp           latest    a1b2c3d4e5f6   2 minutes ago   180MB
nginx           latest    f7g8h9i0j1k2   3 days ago      192MB
python          3.12      l3m4n5o6p7q8   1 week ago      1.02GB
```

### 🎯**Download/Pull image from Docker Hub**
```shell
docker pull <image_name>
# (OR)
docker image pull <image_name>
```
```docker
docker pull nginx
docker pull hello-world
docker pull mysql

# Download a specific version
docker pull python:3.12
docker pull mysql:8.0
```

### 🎯**Delete Docker Image**
* Docker image ko delete karne ke liye docker rmi <image_name> ya docker image rm <image_name> command use karte hain. Agar image kisi container se linked ho to -f flag se force delete kar sakte hain.
* ❌ rm image par kaam nahi karta (jab tak docker image rm na likho)

* By Image name/ image id
```bash
docker rmi image_name/image_id
docker image rmi image_name/image_id
docker image rm image_name/image_id
```

* **Force Delete:-** Agar image kisi container dwara use ho rahi ho:
```bash
docker image rmi -f nginx
# OR
docker image rm -f nginx
```

* remove unused images remove
```bash
docker image prune
```

### 🧱 **What Are Docker Image Layers?**
* A Docker Image is made up of multiple read-only layers stacked on top of each other.
* Each instruction in a Dockerfile creates a new layer.
* Each layer represents a change or addition made to the image, like:
  * installing software
  * copying files
  * setting environment variables
* These layers are read-only and are created during the build process, usually from a Dockerfile.
* **HINDI:-**
* Docker Image एक single file नहीं होती, बल्कि कई layers (परतों) से मिलकर बनी होती है।
* Dockerfile में लिखी गई लगभग हर instruction एक नई layer बनाती है।

#### Example
```bash
FROM ubuntu:22.04
RUN apt update
RUN apt install -y nginx
COPY . /app
CMD ["nginx", "-g", "daemon off;"]

#
Layer 1: Ubuntu Base Image
Layer 2: apt update
Layer 3: nginx installation
Layer 4: Copy application files
Layer 5: CMD instruction
```

#### Why Layers are Useful?
1. **Fast Build (Caching)**
* अगर आपने सिर्फ code बदला:
```bash
COPY . /app
```
* तो Docker केवल इस layer को rebuild करेगा।
* apt install वाली layer दोबारा नहीं चलेगी।
* इससे build बहुत तेज हो जाता है।

2. **Storage Save** होता है
* मान लो दो images हैं:
  * Image A = Ubuntu + Python
  * Image B = Ubuntu + Nginx
* दोनों Ubuntu वाली layer को share करेंगी।
* Ubuntu layer दो बार store नहीं होगी।

3. **Faster Download**
* जब नई image pull करते हैं:
```bash
docker pull nginx
```
* तो Docker सिर्फ नई/बदली हुई layers डाउनलोड करता है।
* बाकी layers local cache से ले लेता है।

### 🧠 **Why Layers Matter**
* ✅ 1. **Reusability & Caching:** Docker caches layers, so if you rebuild the image and some layers haven't changed, it reuses them — making builds much faster.
  * For example: If you only changed files in your app folder, only the COPY . /app layer will be rebuilt.
* ✅ 2. **Efficiency:-** Multiple containers can share the same layers on disk, saving space.
* ✅ 3. **Transparency** Each layer has a unique ID and can be inspected (docker history image_name) to see what changes were made at each step.


### **How do you create a Docker image?**
* A Docker Image is created **using a Dockerfile**.

#### Steps
1. Create a Dockerfile
* File name: Dockerfile,  Koi extension nahi lagani (Dockerfile.txt ❌)
```bash
my_fastapi_project/
│
├── app/
│   ├── main.py
│   └── routes/
│
├── requirements.txt
├── Dockerfile
└── .env
```

* Inside the dokerfile
```bash
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

2. Build the Image
```bash
docker build -t myapp:1.0 .

# docker build → Build an image
# -t → Assign a name/tag
# myapp:1.0 → Image name and version
# . → Current directory (contains Dockerfile)
```

3. Verify the Image
```bash
docker images

# Output:-
REPOSITORY   TAG     IMAGE ID
myapp        1.0     abc123
```

4. Run a Container from the Image
```bash
docker run -d -p 8000:8000 myapp:1.0
```

#### ⭐ Important
* Agar aap baad mein main.py change karte ho:
```bash
print("Hello New")
```

* to purani image automatically change nahi hogi. Aapko dobara build karna padega:
```bash
docker build -t myapp .
```

#### **Now we upload the image on docker hub**
1. Docker Hub par Login karo
```bash
docker login

# Username aur password enter karo.
```

2. Apni Image Check karo
```bash
docker images

# Output:-
REPOSITORY   TAG
myapp        latest
```

3. Image ko Tag karo
* Docker Hub par push karne ke liye image ka naam:
```bash
syntex:- docker tag myapp:latest username/myapp:latest

docker tag myapp:latest mohitsaxena/myapp:latest
```

4. Push karo
```bash
syntex:- docker push username/myapp:latest

docker push mohitsaxena/myapp:latest
```

5. Verify on Docker Hub
* Docker Hub par login karke repository check karo. Image wahan dikh jayegi.