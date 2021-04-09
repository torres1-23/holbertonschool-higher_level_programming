#!/usr/bin/python3
"""This module that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response.

Usage:
   This module accepts two console arguments, execute it like this:
    "./6-post_email.py <URL> <email>".
"""
import sys
import requests

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], data)
    print(request.text)
