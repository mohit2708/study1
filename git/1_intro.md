### Ques. What is git?
* Git is a popular version control system. It was created by Linus Torvalds in 2005, and has been maintained by Junio Hamano since then.
* It is used for:
  * Tracking code changes
  * Tracking who made changes
  * Coding collaboration


### Git:-
* git is a **version control system.** It was created by **Linus Torvalds** in 2005, and has been **maintained** by **Junio Hamano** since then.
* git helps you keep track of code changes.
* git is used to collaborate on code.
* Who made changes.
* Syntx:
```git
git --version
```


### How to check git version?
```git
git --version
```

### What is the difference between Git and GitHub?
|                                   Git                                    |                                GitHub                                |
| :----------------------------------------------------------------------: | :------------------------------------------------------------------: |
| Git is a version control system used to track changes in files over time | GitHub is a platform where Git repositories can be stored and shared |
|                     It runs locally on your computer                     |                     It is a cloud-based service                      |



### What is .gitignore?
* The '.gitignore' file tells Git which files and folders to ignore when tracking changes.
* When sharing your code with others, there are some files we don't want to share to other then we use the .gitignore to do that.
* Create the text file **.gitignore** under the root folder
```git
# Ignore all text files
*.txt       # * means all the text files

# Ignore all logs files
*.log       # * means all the log files

# ignore ALL files in ANY directory named temp
temp/
```