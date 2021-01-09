#!/usr/bin/python3

"""This module defines a print function
   "def text_indentation(text):"
   that prints a text with 2 new lines after each of these characters:
   ., ? and :

Usage:
    "text_indentation(...)" must receive a string,
    prints two lines after the characters ".", "?" and ":".
"""


def text_indentation(text):
    """Prints a text with two lines after ".", "?" and ":" characters

    Args:
        text (str): text to print.

    Raises:
        TypeError: if "text" is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    fg = False
    tmp_str = ""
    for i in range(len(text)):
        if text[i] is " " and fg is False:
            continue
        else:
            fg = True
            tmp_str += text[i]
        if text[i] in (".", "?", ":"):
            print(tmp_str, end="")
            print("\n")
            tmp_str = ""
            fg = False
        elif i + 1 == len(text):
            print(tmp_str, end="")
            tmp_str = ""
            fg = False
