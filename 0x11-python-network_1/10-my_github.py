#!/usr/bin/python3
""" This takes GitHub credentials (username and password) and uses the GitHub API to display your id.
Uses Basic Authentication with a personal access token as password. """

import requests
import sys

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    auth = (username, token)

    response = requests.get('https://api.github.com/user', auth=auth)

    try:
        user_data = response.json()
        print(user_data['id'])
    except ValueError:
        print("None")
