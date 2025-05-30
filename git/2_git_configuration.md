|  No.  | Questions                                                        |
| :---: | ---------------------------------------------------------------- |
|       | [List of branch?](#show-all-remote-and-local-branch-names)       |

### Git configuration

#### Check a git username
```git
$ git config --global user.name
> Mohit saxena
```

#### Set a Git username
```git
git config --global user.name "Mohit Saxena"
```

#### Check a git email
```git
$ git config --global user.email
> mksaxena27@yopmail.com
```

#### Set a Git email
```git
git config --global user.name "mksaxena27@yopmail.com"
```

#### check origin
```git
PS D:\gitOcean> git remote -v
origin  https://git.chetu.com/ChetuInc/OceansideBeachService-HOTT.git (fetch)
origin  https://git.chetu.com/ChetuInc/OceansideBeachService-HOTT.git (push)
```

#### Set origin
```git
git remote add origin https://git.chetu.com/ChetuInc/OceansideBeachService-HOTT.git
```

#### Check all config list
```git
git config -list
```