## Without clone connect to repo
### Open
```git
git init
git checkout -b develop // create branch and move to branch
git add .
git commit -m "Initial commit"
git remote add origin <repo-url>
git push -u origin develop
```

### Fix option 1 (MOST COMMON): add a file
```git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin develop
```

### option 2: Empty commit (no files needed)
```git
git commit --allow-empty -m "Initial empty commit"
git push -u origin develop
```
