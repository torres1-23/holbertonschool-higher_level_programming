#!/usr/bin/python3
"""This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage:
   This module accepts a console argument, execute it like this:
   "./8-json_api.py <letter to send>".
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    try:
        request = requests.post('http://0.0.0.0:5000/search_user', data)
        if request.json():
            json = request.json()
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError as error:
        print('Not a valid JSON')
