|  No.  | Questions                                                        |
| :---: | ---------------------------------------------------------------- |
|       | [List of branch?](#show-all-remote-and-local-branch-names)       |
|       | [List of Local branch?](#show-all-remote-and-local-branch-names) |
|       | [List of remote branch?](#all-remote-branch-names)               |
|       | [Create a new branch](#create-a-new-branch)                      |


### Branch
* The current local branch will be marked with an asterisk.
  
#### Show All Remote and Local Branch Names
```git
git branch
OR
git branch -a
```

#### all remote branch names
```git
git branch -r
```

#### Create a new branch
```git
git branch branch_name
```

#### Switch to the new branch
```git
git checkout branch_name
```

#### create and switch to the new branch in one step
```git
git checkout -b branch_name
```

#### current branch details
```git
git branch -vv
```

#### branch details local and global
```git
git branch -vva
```

#### Rename a Branch
* Make sure you are in the another branch
```git
git branch -m old-branch new-branch
```

#### Delete remote Branches
```git
git push origin --delete my-branch-name
```

#### Delete local Branches
```git
git branch -d my-branch-name
OR
git branch -D my-branch-name
```