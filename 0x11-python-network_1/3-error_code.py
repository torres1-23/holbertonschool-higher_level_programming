#!/usr/bin/python3
"""This module akes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).

Usage:
    This module accepts a console argument, execute it like this:
    "./3-error_code.py <URL>".
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    request_obj = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request_obj) as response:
            print((response.read()).decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
