### Go to AWS Console
- Open 👉 https://console.aws.amazon.com
- Search EC2 → Click Launch Instance

### Configure Instance Name
- **Name:** fastapi-server
- **AMI:** Choose 👉 Ubuntu Server 22.04 LTS
- **Instance type:** t2.micro (Free tier)

### Create Key Pair (IMPORTANT)
- Click Create key pair
- Name: fastapi-key
- Type: RSA
- Format:
  - .pem → Mac/Linux
  - .ppk → Windows (PuTTY)
- Download and keep safe.

### Network Settings (Security Group)
- Allow these ports:

| Type       | Port                        |
| ---------- | --------------------------- |
| SSH        | 22                          |
| HTTP       | 80                          |
| Custom TCP | 8000 (optional for testing) |

- **Final:** Click Launch Instance


### Connect to EC2