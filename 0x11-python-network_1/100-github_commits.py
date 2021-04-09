#!/usr/bin/python3
"""This module takes takes a GitHub repository commits history and list the
last 10commits.

Usage:
   This module accepts two console arguments, execute it like this:
   "./100-github_commits.py <repository name> <owner name>".
"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    request = requests.get(url)
    coms = request.json()
    for i in range(10):
        print('{}: {}'.format(coms[i].get('sha'), coms[i].get('commit')
                              .get('author').get('name')))
