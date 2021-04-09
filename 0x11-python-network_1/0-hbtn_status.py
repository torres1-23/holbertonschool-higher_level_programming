#!/usr/bin/python3
"""This module fetches info from an URL, using module urlib.

Usage:
    Execute this module to fetch info from "https://intranet.hbtn.io/status"
"""
import urllib.request

if __name__ == "__main__":
    request_obj = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(request_obj) as response:
        info = response.read()
    print(("Body response:\n"
           "    - type: {}\n"
           "    - content: {}\n"
           "    - utf8 content: {}").format(type(info),
                                            info,
                                            info.decode("utf-8")))
