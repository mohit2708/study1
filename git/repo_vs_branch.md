### Difference between repo vs branch?
- 👉 A repository is the complete Git project, while a branch is an independent line of development within that repository.

| Feature    | Repository (Repo)                       | Branch                                       |
| ---------- | --------------------------------------- | -------------------------------------------- |
| Definition | Complete project with full history      | A parallel line of development inside a repo |
| Scope      | Whole project                           | Part of the project                          |
| Contains   | Files, commits, branches, tags, history | Commits related to a feature or task         |
| Purpose    | Store and manage the entire codebase    | Work on features without affecting main code |
| Created by | `git init` or clone                     | `git branch <name>`                          |
| Default    | Only one repo per project               | Multiple branches inside one repo            |
| Example    | Laravel project repo                    | `main`, `dev`, `feature-login`               |
