|  No.  | Questions                                                                       |
| :---: | ------------------------------------------------------------------------------- |
|       | [if found ssl error?](#ssl-error)                                               |
|       | [Check Configure and set the Configure](#check-configure-and-set-the-configure) |
|       | [Initialize Git](#initialize-git)                                               |
|       | [Clone the project](#clone-the-project)                                         |
|       | [git status](#git-status)                                                       |
|       | [Git Adding New Files](#git-adding-new-files)                                   |
|       | [Removing Files from the Staging Area](#removing-files-from-the-staging-area)   |


```python

```


### ssl error
* when we got the ssl error
```git
git config --global http.sslVerify false
```


## Starting a project

### Initialize Git
```git
git init 
```


##

### git status
* To check the status for file upload 
* red files are Untracked files: i.e abhi add nahi hui hai hai.
* green files are tracked file i.e add ho chuki hai
```git
git status
```

### Create new file
```git
touch newfile.txt
```

### Git Commit
```git
git commit -m "initial commit"
```

### Git Commit Log
```git
git log
```

### show the all file of the folder
```git
ls
# all file - show hidden file also
ls -a
```


### Commit History
* Display the most recent commits and the status of the head:
```git
$ git log

Type q to exit this screen. Type h to get help.
```
* Display the output as one commit per line:
```sql
git log --oneline
```
* Displays the files that have been modified:
```git
$ git log -stat
```
* Display the modified files with location:
```git
$ git log -p
```
### What is git-blame?
* Annotates each line in a file with information about the last commit that modified the line.
* This information includes the commit hash, the author, the date of the change, and optionally, the line number. By using git-blame.
* We can track the origin of each line of code, making it easier to understand the history and context of changes.
```git
git blame <file-name>
```


### Push Command
```git
git push -u origin master
```