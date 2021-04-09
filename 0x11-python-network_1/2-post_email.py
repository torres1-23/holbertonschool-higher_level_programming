#!/usr/bin/python3
"""This module takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)

Usage:
    This module accepts two console arguments, execute it like this:
    "./2-post_email.py <URL> <email>".
"""
import sys
import urllib.request

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")
    request_obj = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request_obj) as response:
        print((response.read()).decode('utf-8'))
