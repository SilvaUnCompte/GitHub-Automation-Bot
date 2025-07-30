import os
import random
import requests
import string
import time
from git import Repo
from dotenv import load_dotenv

load_dotenv()  # charge les variables du .env

# SETTINGS
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
LOCAL_REPO_PATH = os.getenv("LOCAL_REPO_PATH")
TARGET_BRANCH = os.getenv("TARGET_BRANCH", "main")
FILE = "change-me.txt"

# HEADERS GITHUB API
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github+json'
}

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


# ------------------------------------------------------

def random_modification(use_new_branch=False):
    repo = Repo(LOCAL_REPO_PATH)
    
    if use_new_branch:
        branch_name = f"auto-branch-{random_string()}"
        repo.git.checkout(TARGET_BRANCH)
        repo.git.pull()
        repo.git.checkout('-b', branch_name)
        print(f"Branch created: {branch_name}")
    else:
        repo.git.checkout(TARGET_BRANCH)
        repo.git.pull()
        branch_name = None
        
    modify_random_file()
    commit_and_push(repo, branch_name)
    if use_new_branch:
        create_pr_and_merge(branch_name)


def modify_random_file():
    file_path = os.path.join(LOCAL_REPO_PATH, FILE)

    with open(file_path, 'r+', encoding='utf-8', errors='ignore') as f:
        f.truncate(0)
        f.seek(0)
        f.write(random_string())


def commit_and_push(repo, branch_name=None):
    repo.git.add([FILE])
    repo.index.commit(f"Random update on {branch_name or TARGET_BRANCH}")
    origin = repo.remote(name='origin')
    origin.push(refspec=f"{branch_name}:{branch_name}" if branch_name else None)
    print(f"{FILE} file commited and pushed.")


def create_pr_and_merge(branch_name):
    # Create MR
    pr_url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls"
    pr_data = {
        "title": f"Auto PR from {branch_name}",
        "head": branch_name,
        "base": TARGET_BRANCH
    }
    pr_response = requests.post(pr_url, json=pr_data, headers=HEADERS)
    if pr_response.status_code != 201:
        print("WARNING: Error creating MR")
        return

    pr = pr_response.json()
    pr_number = pr['number']
    print(f"MR #{pr_number} created.")

    # Wait a bit for the MR to be available for merging
    time.sleep(2)

    # Merge the MR
    merge_url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls/{pr_number}/merge"
    merge_data = {"commit_title": f"Merge auto {branch_name}", "merge_method": "merge"}
    merge_response = requests.put(merge_url, json=merge_data, headers=HEADERS)
    if merge_response.status_code == 200:
        print(f"MR #{pr_number} merged.")
    else:
        print("WARNING: Error merging MR.")


def create_and_close_issue():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/issues'
    title = f"Issue auto #{random.randint(1000, 9999)}"
    data = {"title": title}

    # Create the issue
    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 201:
        issue_number = response.json()["number"]
        print(f"Issue #{issue_number} created.")

        # Close the issue
        close_url = f'{url}/{issue_number}'
        close_data = {"state": "closed"}
        close_resp = requests.patch(close_url, json=close_data, headers=HEADERS)
        if close_resp.status_code == 200:
            print(f"Issue #{issue_number} closed.")
        else:
            print("WARNING: Error closing the issue.")
    else:
        print("WARNING: Failed to create the issue.")


def submit_review():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/pulls'
    pulls = requests.get(url, headers=HEADERS).json()

    if not pulls:
        print("WARNING: No pull request.")
        return

    pr = random.choice(pulls)
    comments_url = pr["_links"]["comments"]["href"]
    comment_body = {
        "body": f"Automated comment: MR #{pr['number']} 👍"
    }

    response = requests.post(comments_url, json=comment_body, headers=HEADERS)
    if response.status_code == 201:
        print(f"Comment added to MR #{pr['number']}")
    else:
        print(f"WARNING: Failed to add comment to MR #{pr['number']}")


def main():
    # random_modification(False)
    # random_modification(True)
    # create_and_close_issue()
    # submit_review()
    
    nb = random.randint(1, 5)
    
    actions = random.choices(
        ['modification', 'issue', 'review', 'merge'],
        weights=[60, 5, 10, 25],
        k=nb
    )

    print(f"> Actions to perform: {actions}")

    for i, action in enumerate(actions):
        match action:
            case 'modification':
                print(f"[{i}] Modification selected.")
                random_modification()
            case 'merge':
                print(f"[{i}] Merge selected.")
                random_modification(use_new_branch=True)
            case 'issue':
                print(f"[{i}] Issue selected.")
                create_and_close_issue()
            case 'review':
                print(f"[{i}] Review selected.")
                submit_review()
            case _:
                print(f"[{i}] Unknown action: {action}")

if __name__ == '__main__':
    main()