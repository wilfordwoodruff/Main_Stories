# Contributing to Public Stories

Thank you for your interest in contributing to Public Stories! Your contributions are vital to the continuous growth and development of this project.

Before you contribute, please read through this guide to understand the process and guidelines.

## Reading Data
[Main Data Repo](https://github.com/wilfordwoodruff/Main-Data)
- how to read derived data
```{python}
import pandas as pd

URL 
```

- How to read raw data
```{python}
import requests
import json
import re
import pandas as pd


def get_files(user, repo, path):
    url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
    r = requests.get(url)
    data = json.loads(r.text)

    # Filter the files
    csv_files = [file for file in data if re.search(r'\d{4}-\d{2}-\d{2}-places-export\.csv', file['name'])]

    # This will return an array of all the matching files with details
    return csv_files


user = "wilfordwoodruff"
repo = "Main-Data"
path = "data/raw"
csv_files = get_files(user, repo, path)

# Sort files by date in the filename, get the latest
csv_files.sort(key=lambda x: x['name'], reverse=True)
latest_file = csv_files[0]

# Construct the raw GitHub URL
raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/main/{latest_file['path']}"

# Read the latest CSV file
df = pd.read_csv(raw_url)

# Now df holds the content of the latest CSV file
print(df.head())
```
- How to grab data

## Getting Started

- Make sure you have a [GitHub](https://github.com) account.
- Fork the Public Stories repository to your account. This creates your own copy of the project where you can make changes.

## Making Contributions

- Create a new branch in your forked repository to keep your changes separate.
- Work on your changes. Ensure that they are well-thought-out and necessary. Remember, it's quality over quantity.
- Once you're satisfied with your changes, commit them with a clear and concise commit message. This message should describe what changes were made and why.
- After committing your changes, push your branch to your forked repository on GitHub.
- From there, you can create a pull request on the original Public Stories repository. This will notify us of your changes, which we can then review and potentially merge into the project.

## Coding Standards

Please follow the coding standards below to ensure consistency throughout the project:

- Comment your code wherever necessary.
- If you're adding Python code, adhere to PEP 8 style guide.
- Keep your changes as concise as possible.

## Submitting an Issue

If you encounter a bug or have a suggestion for improvement, please submit it as an issue on GitHub. Check to see if your issue or suggestion has already been submitted by another user to avoid duplicates.

[Issue Tracker](https://github.com/wilfordwoodruff/Public_Stories//issues)

## Questions or Concerns

If you have any questions or concerns about contributing, please submit them here [Issue Tracker](https://github.com/wilfordwoodruff/Public_Stories//issues). We value your feedback and will do our best to assist you.

Thank you for your interest in our project. We appreciate your contributions and look forward to collaborating with you!
