#!/usr/bin/python3

"""This script writes to a .json file the arguments given in the stdin

Usage:
    All the arguments in the stdin after the executable name will be added to
    a list and then added to a file "add_item.json", if the file was already
    created, the list will be appended.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    lst = load_from_json_file("add_item.json")
except Exception:
    lst = []
lst += sys.argv[1:]
save_to_json_file(lst, "add_item.json")
