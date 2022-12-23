# MIT License New Year Updater

Updates MIT licenses in every user's repository.

## How to use

Create `config.py` file like this:
```py
TARGET_YEAR = 2023
GITHUB_ACCESS_TOKEN = "<github_access_token>"
LICENSE_PREFIX = \
"""MIT License

Copyright (c) """ # This prefix works for auto-generated by github MIT License
COMMIT_MESSAGE = "Updated years in a license"
```

Run following commands:
```sh
$ python3 -m pip install -r requirements.txt
$ python3 main.py
```