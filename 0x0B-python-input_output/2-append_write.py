#!/usr/bin/python3

"""This module defines a function "def append_write(filename="", text="")",
that appends into a file and return the number of characters written.

Usage:
    "def append_write(...)" appends into a file, and returns the number of
    characters printed, it creates the file if it doesn't exist.
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number of
    characters added.

    Args:
        filename (string, optional): name of the file to append to,
        empty string by default.
        text (string, optional): text to append to file,
        empty string as default.

    Return:
        Number of characters added.
    """
    with open(filename, mode='a', encoding='UTF8') as s_file:
        return s_file.write(text)
