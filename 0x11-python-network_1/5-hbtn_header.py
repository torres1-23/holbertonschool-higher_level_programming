#!/usr/bin/python3
"""This module takes in a URL, sends a request to the URL and displays the
value of the variable "X-Request-Id" in the response header

Usage:
   This module accepts a console argument, execute it like this:
    "./5-hbtn_header.py <URL>".
"""
import sys
import requests

if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    print(request.headers.get("X-Request-Id"))
