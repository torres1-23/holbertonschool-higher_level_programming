#!/usr/bin/python3

"""This module defines a function "def load_from_json_file(filename)",
that reads a file and gets a JSON string.

Usage:
    "def load_from_json_file(...)" reads a file "filename" and
    gets a JSON string.
"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): Name of the file.

    Return:
        JSON string.
    """
    with open(filename, encoding='UTF8') as s_file:
        return json.load(s_file)
