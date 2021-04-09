#!/usr/bin/python3
"""This module fetches info from https://intranet.hbtn.io/status using the
package requests.

Usage:
   Execute it like this:
    "./4-hbtn_status.py".
"""
import requests

if __name__ == "__main__":
    request = requests.get('https://intranet.hbtn.io/status')
    print(("Body response:\n"
           "\t- type: {}\n"
           "\t- content: {}").format(type(request.text),
                                     request.text))
