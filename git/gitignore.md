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