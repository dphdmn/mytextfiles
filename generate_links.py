import os
import subprocess
import webbrowser

# Your GitHub username and repository name
GITHUB_USERNAME = "dphdmn"
GITHUB_REPO = "mytextfiles"
BRANCH = "main"

# Get the latest committed files
result = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"], capture_output=True, text=True)
files = result.stdout.strip().split("\n")

# Filter out empty results
files = [f for f in files if f]

if not files:
    print("No recent changes detected.")
    exit()

# Generate raw GitHub links
links = [f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/refs/heads/{BRANCH}/{file}" for file in files]

# Open each link in the default web browser
for link in links:
    print(f"Opening: {link}")
    webbrowser.open(link)
