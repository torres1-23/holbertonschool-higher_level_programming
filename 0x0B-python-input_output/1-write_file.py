#!/usr/bin/python3

"""This module defines a function "def write_file(filename="", text="")",
that writes into a file and return the number of characters written.

Usage:
    "def write_file(...)" writes into a file, and returns the number of
    characters printed, it creates the file if it doesn't exist or overwrite
    its contents.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (string, optional): name of the file to write to,
        empty string by default.
        text (string, optional): text to write to file,
        empty string as default.

    Return:
        Number of characters written.
    """
    with open(filename, mode='w', encoding='UTF8') as s_file:
        return s_file.write(text)
