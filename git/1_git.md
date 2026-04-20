### What is Git?
* git is a **version control system.** It was created by **Linus Torvalds** in **2005**, and has been **maintained** by **Junio Hamano** since then.
* git helps you keep track of code changes.
* git is used to collaborate on code.
* Who made changes.
* It is used for:
  * Tracking code changes
  * Tracking who made changes
  * Coding collaboration


### How to check git version?
```git
git --version
```

### What is the difference between Git and GitHub?
| Git                                                                      | GitHub                                                               |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------- |
| Git is a version control system used to track changes in files over time | GitHub is a platform where Git repositories can be stored and shared |
| It runs locally on your computer                                         | It is a cloud-based service                                          |

### What is a repository?
- A repository (repo) in Git is a storage space for your project where Git tracks all files, changes, and version history.
- It contains:
  - Your project files (code, images, docs, etc.)
  - A hidden .git folder → stores commits, branches, history, configuration
  - The complete version control timeline

#### Types of Git Repositories
1. Local Repository
- Stored on your own computer.
```git
git init
```

2. Remote Repository
- Stored on a server like:
  - GitHub
  - GitLab
  - Bitbucket
- Used for:
  - Backup
  - Team collaboration
  - CI/CD
```git
git remote add origin <repo-url>
```

#### What a Repository Helps You Do Advantage
- ✔ Track file changes
- ✔ Go back to previous versions
- ✔ Work with branches
- ✔ Collaborate with team
- ✔ Merge code safely