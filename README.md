# GitHub Automation Bot – Educational Project

This project is an **educational solution** designed as part of a course on GitHub API fundamentals. It allows students to explore and manipulate core GitHub functionalities programmatically by building a simple **automation bot** in Python.

Students will learn how to:
- Modify files and push code via Git
- Create and merge pull requests automatically
- Open and close GitHub issues
- Interact directly with the **GitHub REST API**

---

## Learning Objectives

This project helps students:
- Understand how to authenticate and interact with the GitHub REST API
- Automate common Git workflows (branches, commits, PRs, issues)
- Use `GitPython` to control a local repository via code
- Perform HTTP requests with Python's `requests` library
- Simulate developer activity for testing CI/CD or automation workflows

---

## Features

| Feature                 | Description |
|-------------------------|-------------|
| Random File Changes     | Edits a file with random content and commits it |
| Branching & PRs         | Can create a branch, commit changes, open a PR, and auto-merge it |
| Issue Automation        | Automatically opens and closes a GitHub issue |
| Activity Simulation     | Mimics the behavior of a real contributor with randomized actions |

---

## Technologies Used

- **Python 3**
- [`GitPython`](https://gitpython.readthedocs.io/en/stable/)
- [`requests`](https://docs.python-requests.org/)
- [`python-dotenv`](https://github.com/theskumar/python-dotenv)
- **GitHub REST API**

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/GitHub-Cheat-Code.git
cd GitHub-Cheat-Code
```
### 2. Install the dependencies

Make sure you have Python 3 installed.

```bash
pip install -r requirements.txt
```

This will install the required Python libraries:
- `requests` for HTTP calls to the GitHub API  
- `gitpython` for local Git operations  
- `python-dotenv` for environment variable management  

---

### 3. Configure the bot

Copy the environment file template:

```bash
cp .env.example .env
```

Then open `.env` and fill in your credentials and settings:

```env
GITHUB_TOKEN=ghp_yourGitHubTokenHere
GITHUB_REPO=yourUsername/yourRepository
LOCAL_REPO_PATH=C:\\path\\to\\your\\local\\repo
TARGET_BRANCH=main
```

> **Important**: Never share your GitHub token or commit it to the repository.

---

### 4. Run the bot

Once everything is set up, run the script:

```bash
python main.py
```

The bot will randomly choose actions to simulate GitHub contributor activity:
- Modify and commit changes to a file  
- Push to a new or existing branch  
- Create and merge a pull request  
- Open and close an issue  
- Or do nothing (based on probability)  

Each execution is different, helping simulate a variety of API use cases.

---

## Project Structure

```text
.
├── main.py               # Main automation script
├── change-me.txt         # Target file for simulated edits
├── README.md             # Project documentation
├── requirements.txt      # Python dependency list
├── .env.example          # Environment variable template
├── setup.sh              # Setup script for macOS/Linux
└── setup.bat             # Setup script for Windows
```