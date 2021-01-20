#!/usr/bin/python3

"""This module defines a function "def save_to_json_file(my_obj, filename)",
that writes a python object to a file using JSON representation.

Usage:
    "def save_to_json_file(...)" writes a python object "my_obj" to a file
    "filename" as a JSON string.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes a python object as a JSON string in a file.

    Args:
        my_obj (object): object to convert to JSON.
        filename (string): file to write in.
    """
    with open(filename, mode='w', encoding='UTF8') as s_file:
        json.dump(my_obj, s_file)
