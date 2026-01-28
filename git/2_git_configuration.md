|  No.  | Questions                                        |
| :---: | ------------------------------------------------ |
|       | [Check a git username?](#check-a-git-username)   |
|       | [Set a Git username?](#set-a-git-username)       |
|       | [Check a git email?](#check-a-git-email)         |
|       | [Set a Git email?](#set-a-git-email)             |
|       | [check origin?](#check-origin)                   |
|       | [Set origin?](#set-origin)                       |
|       | [Check all config list?](#check-all-config-list) |

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