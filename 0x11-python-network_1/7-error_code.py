#!/usr/bin/python3
"""This module that takes in a URL, sends a request to the URL and displays
the body of the response.

Usage:
   This module accepts a console arguments, execute it like this:
    "./7-error_code.py <URL>".
"""
import sys
import requests

if __name__ == "__main__":
    try:
        request = requests.get(sys.argv[1])
        request.raise_for_status()
        print(request.text)
    except requests.exceptions.HTTPError as error:
        print("Error code: {}".format(request.status_code))
