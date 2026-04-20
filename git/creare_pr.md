### How to creare pr in git?
- A Pull Request is a request to merge your feature branch into another branch (usually main or dev) for code review.
- A Pull Request is a request to merge code from one branch to another for review and collaboration.

#### Steps
- Go to repository → you will see:
- 👉 Compare & Pull Request button → click it
- Then:
  - Base branch → main (or dev)
  - Compare branch → feature-login
  - Add title
  - Add description
  - Click Create Pull Request

#### Steps in details
- Prepare your changes: Ensure your changes are committed and pushed to a branch in your repository (or your fork).
- Navigate to the repository: Go to the main page of the repository where you want to propose changes.
- Start the PR:
  - If you recently pushed a branch, a **yellow banner** may appear. Click **Compare & pull request**.
  - Otherwise, click the Pull requests tab, then the New pull request button.
- Set branches:
  - Base branch: The target branch you want to merge into (usually main).
  - Compare branch: The source branch containing your changes.
  - Note: If contributing to someone else's repo, click "compare across forks" to select your forked repository.
- **Review and Describe:** Add a clear Title and a Description explaining your changes. You can link to an issue by typing Closes #123 in the description.
- **Submit:** Click Create pull request. To keep it private while working, use the dropdown to select Create draft pull request.


#### PR Flow in Teams
- Developer creates feature branch
- Pushes code
- Creates PR
- Reviewer checks code
- Fix comments (if any)
- PR approved
- Merge into main

#### Best Practices for PR
- ✔ Small PR (easy to review)
- ✔ Proper title and description
- ✔ Link Jira/Task ID
- ✔ Rebase before PR (clean history)
- ✔ Resolve conflicts

#### PR via Command Line (GitHub CLI)
```git
gh pr create --base main --head feature-login --title "Login Feature" --body "Added login API"

# OR
gh pr create --title "Your PR Title" --body "Your PR Description"
```

| Part                   | Meaning                                 |
| ---------------------- | --------------------------------------- |
| `gh pr create`         | Create a new Pull Request               |
| `--base main`          | Target branch (where you want to merge) |
| `--head feature-login` | Your source branch (your changes)       |
| `--title`              | PR title                                |
| `--body`               | PR description                          |


#### how to assign reviewer via CLI
- This will create the PR and request review from those users on GitHub.
```git
gh pr create \
  --base main \
  --head feature-login \
  --title "Login Feature" \
  --body "Added login API" \
  --reviewer username1,username2
```

- If PR is already created:
```git
gh pr edit <PR-number> --add-reviewer username
gh pr edit 15 --add-reviewer user1,user2    // example
```

- Assign Team as Reviewer
```git
gh pr edit 15 --add-reviewer org-name/team-name
gh pr edit 15 --add-reviewer backend-team

```

#### Check PR Details
- To see PR number:
```git
gh pr list
```
- To view PR:
```git
gh pr view 15
```









how to approve/merge PR via CLI

request changes via CLI

merge PR via CLI 🚀