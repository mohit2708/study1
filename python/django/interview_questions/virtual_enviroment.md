### **Ques. What is virtual Enviroment**
- A virtual environment is an isolated(Completely separate and independent) environment in Python that allows you to install and manage dependencies separately for each project without affecting the global Python installation.

### How do you activate a virtual environment?
```python
python -m venv venv_name
```

### How do you activate a virtual environment?
```python
# Windows
venv_name\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### Why do we need virtual environments?
- Avoid **dependency conflicts**
- Use **different package versions** for different projects
- Keep the global Python environment clean
- Improve project portability and reproducibility


### What problems occur without virtual environments?
- Package version conflicts
- One project breaking another
- Difficult dependency management
- Production issues due to mismatched versions




6. How do you deactivate a virtual environment?
Answer:
Copy code
Bash
deactivate
7. What is venv?
Answer:
venv is a built-in Python module (Python 3.3+) used to create lightweight virtual environments.
8. Difference between venv and virtualenv?
Feature
venv
virtualenv
Built-in
Yes
No
Python versions
Python 3.3+
Supports Python 2 & 3
Speed
Slower
Faster
Installation
No extra install
Needs pip install
9. What is pip in virtual environments?
Answer:
pip is a package manager used to install libraries inside the virtual environment, isolated from global packages.
10. What is requirements.txt?
Answer:
It is a file that lists all project dependencies and versions.
Example:
Copy code
Txt
django==4.2
requests==2.31.0
11. How do you generate requirements.txt?
Answer:
Copy code
Bash
pip freeze > requirements.txt
12. How do you install dependencies from requirements.txt?
Answer:
Copy code
Bash
pip install -r requirements.txt
13. How do you check installed packages in a virtual environment?
Answer:
Copy code
Bash
pip list
14. How do you know a virtual environment is active?
Answer:
Environment name appears in terminal
Example:
Copy code
Bash
(venv) $
which python or where python shows venv path
15. Can we use one virtual environment for multiple projects?
Answer:
Not recommended.
Each project should have its own virtual environment to avoid dependency conflicts.
16. Is virtual environment required in production?
Answer:
Yes. It ensures:
Correct package versions
Stable deployments
Consistent environments across servers
17. What happens if you delete a virtual environment?
Answer:
Only the environment is removed
Project code remains safe
Dependencies can be reinstalled using requirements.txt
18. Difference between virtual environment and Docker?
Answer:
Virtual Environment
Docker
Python-level isolation
OS-level isolation
Lightweight
Heavier
Dependency management
Full application container
Faster setup
More configuration
19. Where are packages installed in a virtual environment?
Answer:
Inside the virtual environment folder, usually:
Copy code
Bash
venv/lib/pythonX.X/site-packages
20. Interview one-line answer (Important ⭐)
Answer:
A Python virtual environment is an isolated setup that allows independent dependency management for each project.
If you want, I can also provide:
Short 1-line interview answers
Real-time project explanation
MCQ questions
Hindi explanations
Just tell me 👍