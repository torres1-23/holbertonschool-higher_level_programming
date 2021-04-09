#!/usr/bin/python3
"""This module takes takes GitHub credentials (username and password) and uses
the GitHub API to display your id

Usage:
   This module accepts two console arguments, execute it like this:
   "./8-json_api.py <username> <password>".
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    request = requests.get('https://api.github.com/user', auth=auth)
    print(request.json().get('id'))
