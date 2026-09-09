### What is CI/CD?
* CI/CD is a software development practice that automates the process of integrating code, running tests, building applications, and delivering or deploying them to different environments.
* CI/CD का मतलब है Continuous Integration / Continuous Delivery (या Continuous Deployment)।
* CI/CD एक automated process है जिसमें code को automatically build, test और deploy किया जाता है।

#### CI — Continuous Integration
* जब developer code में changes करके GitHub पर push/PR करता है, तो automatically:
```bash
Code Push
   ↓
Build
   ↓
Tests
   ↓
Code Quality Check
```
* इससे पता चलता है कि नया code existing code को break तो नहीं कर रहा।

#### CD — Continuous Delivery / Deployment
* Tests successfully pass होने के बाद application को आगे environment में भेजा जाता है:
```bash
Tests Pass
   ↓
Build
   ↓
Staging
   ↓
Production
```
* Continuous Delivery: Production तक code automatically तैयार होता है, लेकिन deployment के लिए manual approval हो सकता है।
* Continuous Deployment: Tests pass होते ही Production में automatically deploy हो जाता है।

#### CI vs CD
| CI (Continuous Integration)           | CD (Continuous Delivery / Deployment) |
| ------------------------------------- | ------------------------------------- |
| Code को integrate, build और test करता है | Tested code को deploy करता है            |
| Developer के code push पर शुरू होता है      | CI successful होने के बाद शुरू होता है         |
| Focus: Code quality और bug detection  | Focus: Release और deployment          |
| Build + Test                          | Deploy                                |
| Early issue detection                 | Faster software delivery              |


### Continuous Delivery VS Continuous Deployment?
#### Continuous Delivery?
* **Continuous Delivery** में code को automatically build, test और production deployment के लिए ready किया जाता है।
* लेकिन **Production में deploy करने से पहले manual approval लिया जा सकता है।**
```bash
Code Push
   ↓
Build
   ↓
Test
   ↓
Staging
   ↓
Manual Approval
   ↓
Production
```

#### Continuous Deployment?
* Continuous Deployment में successful testing के बाद code automatically production में deploy हो जाता है। इसमें **normally manual approval की जरूरत नहीं होती।**
```bash
Code Push
   ↓
Build
   ↓
Test
   ↓
Staging
   ↓
Automatic Deployment
   ↓
Production
```




### CI/CD with Git Action — Complete Flow
#### Step 1. Git – Code Management
* Developer branch par code changes karta hai:
```bash
git clone <repository>              # pahle clone karega
git checkout -b feature/login       # phir us branch mai jayega
# code changes                      # Code change karke

git add .                           # add karega
git commit -m "Added login feature" # Commit kargea
git push origin feature/login       # Push karega feature branch mai
```


#### Step 2. Pull Request / Merge
* Developer **Pull Request (PR)** create karta hai. 
  * Code review         
  * Automated tests
  * Approval    
  * Feature branch → main/develop

#### Step 3. CI — Continuous Integration
* Git me code **push/merge hote hi** CI pipeline **automatically trigger** hoti hai.
* Example tools:
  * Jenkins
  * GitHub Actions
  * GitLab CI
  * Azure DevOps

* Typical CI steps:
```bash
Checkout Code
     ↓
Install Dependencies
     ↓
Build
     ↓
Unit Test
     ↓
SonarQube / Security Scan
     ↓
Create Artifact
```

#### Step 4. CD — Continuous Delivery/Deployment
* CI successful hone ke baad deployment hota hai:
```bash
Artifact / Docker Image
          ↓
       Dev
          ↓
        QA/UAT
          ↓
     Production
```

### **GitHub Actions**
* GitHub Actions Workflow एक automation process है जो GitHub repository में किसी event (जैसे code push, pull request, schedule) पर automatically run होता है।
* Workflow की configuration YAML (.yml) file में लिखी जाती है और यह **.github/workflows/** folder के अंदर रखी जाती है।
* GitHub Actions की YAML file का कोई भी नाम हो सकता है, बस वह .github/workflows/ folder के अंदर होनी चाहिए और extension .yml या .yaml होना चाहिए।
```bash
.github/workflows/
├── ci.yml
├── deploy.yml
├── test.yml
├── python-ci.yml
├── django-workflow.yml
```

#### Workflow Structure
```bash
name: Python CI         # Workflow का नाम hai

on:                     # Workflow कब trigger होगा
  push:
    branches:
      - main
      - dev
  pull_request:
    branches: [main]

jobs:                   # Workflow के अंदर tasks
  test:
    runs-on: ubuntu-latest      # किस machine पर run होगा

    steps:                      # Job के अंदर execution steps
      - name: Checkout Code
        uses: actions/checkout@v4   # Ready-made GitHub Action use करने के लिए

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Tests     # Shell command execute करने के लिए
        run: pytest
```



### Full Steps
```bash
Developer
   ↓
Git Clone / Pull
   ↓
Code Changes
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub / GitLab
   ↓
CI Pipeline Trigger
   ↓
Build
   ↓
Unit Tests
   ↓
Code Quality / Security Scan
   ↓
Create Artifact / Docker Image
   ↓
CD Pipeline
   ↓
Deploy to Dev / QA
   ↓
Approval (if required)
   ↓
Deploy to Production
   ↓
Monitoring
```


### what is Runner?
* Runner एक machine/server होता है जहाँ आपकी GitHub Actions workflow actually execute होती है।
* Agar aap self-hosted runner use karna chahte ho, tab apni machine/VM/server use karte ho.
```bash
jobs:
  test:
    runs-on: ubuntu-latest
```
* jobs: → क्या काम करना है
* runs-on: → किस Runner/machine पर काम करना है
* ubuntu-latest → GitHub का hosted Ubuntu Runner

#### Type of Runner?
1. GitHub-hosted Runner
* GitHub खुद machine provide करता है: आपको server maintain नहीं करना पड़ता।
```bash
runs-on: ubuntu-latest
```

2. Self-hosted Runner
* आप अपना server/machine देते हो और उस पर GitHub Actions Runner install करते हो।
```bash
runs-on: self-hosted
```