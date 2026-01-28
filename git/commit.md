### Commit changes:
```git
git commit -m "Your commit message"
```

### Commit all changes (including untracked files):
```git
git commit -am "Your commit message"
```

### Amend the last commit:
```git
git commit --amend
```
- This commits changes to tracked files and skips the git add step for modified files, but doesn't add new untracked files.


### Amend the last commit:
```git
git commit --amend
```
- This allows you to modify the previous commit. You can change the commit message or add new changes to the last commit. If you only want to modify the commit message, run:
```git
git commit --amend --no-edit
```

### Commit with a different message for the last commit (after amending):
```git
git commit --amend -m "New commit message"
```
- This allows you to amend the commit and also provide a new commit message directly.

### Git Commit for Specific Files:
```git
git commit <file> -m "Your commit message"
```

This commits a specific file with a provided message, assuming it's already staged.

Undoing or Reverting Commits:

Undo the last commit (but keep the changes in the working directory):

git reset --soft HEAD~1


This removes the last commit but leaves your working directory changes intact.

Undo the last commit and reset the working directory (no changes left):

git reset --hard HEAD~1


This removes the last commit and resets your working directory to match the previous commit.

Undo the commit and unstage the changes:

git reset HEAD~1


This undoes the commit and removes the changes from the staging area, but keeps the modifications in your working directory.

Revert a specific commit (creates a new commit that undoes changes):

git revert <commit-hash>


This creates a new commit that undoes the changes made by the specified commit.

Interactive Rebase for Commit History:

Start an interactive rebase:

git rebase -i HEAD~n


Replace n with the number of commits you want to go back. For example, HEAD~3 would let you interactively edit the last three commits.

Once in the editor, you can:

pick – keep the commit.

edit – make changes to the commit.

squash – combine this commit with the previous one.

drop – remove the commit from the history.

After making your changes, save and close the editor. Git will apply the rebase.

Working with Multiple Commits:

Squash commits (combine multiple commits into one):

git rebase -i HEAD~n


This allows you to squash multiple commits into one by changing pick to squash (or s) for the commits you want to merge.

Fix a commit message for a specific commit (during rebase):
After starting an interactive rebase (git rebase -i), change pick to reword for the commit you want to change the message for.

Commit Signing:

Commit with a GPG signature (if you've set up GPG signing):

git commit -S -m "Signed commit message"


This signs your commit with your GPG key (assuming you’ve configured GPG signing).

Enable commit signing globally:

git config --global commit.gpgSign true


This ensures that every commit you make is signed by default.

Other Commit-Related Commands:

Show the commit history:

git log


This shows the commit history in your current branch. Use options like git log --oneline or git log --graph for more compact or graphical views.

Show the commit diff:

git diff <commit-hash> <commit-hash>


This shows the difference between two commits. You can also use git diff HEAD~1 to compare the working directory with the previous commit.

Show the commit history of a specific file:

git log <file>


This shows the commit history for a specific file, including the hash, author, and message.

View the commit diff for a file:

git show <commit-hash>:<file>


This shows the state of a file at a specific commit.

Push a commit to a remote repository:

git push origin <branch-name>


This pushes your commit(s) to the remote repository (replace <branch-name> with your current branch).

Push to a remote repository and force push (e.g., after amending commits or rebasing):

git push --force origin <branch-name>


Be cautious with this command as it rewrites history.

Reverting Commits (Soft Reset & Hard Reset):

Soft Reset to a specific commit (keeps changes staged):

git reset --soft <commit-hash>


Hard Reset to a specific commit (discards changes):

git reset --hard <commit-hash>