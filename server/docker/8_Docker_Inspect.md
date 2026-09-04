### **What is docker inspect?**
* The docker inspect command is used to view detailed low-level information about:
  * a container
  * an image
  * a volume
  * a network, etc.
* It shows information in JSON format that Docker uses internally.
```bash
docker inspect <container_name_or_id>
docker inspect <image_name_or_id>
docker inspect <volume_name>
docker inspect <network_name>
```