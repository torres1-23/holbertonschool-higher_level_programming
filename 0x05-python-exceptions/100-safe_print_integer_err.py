#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ Prints an integer.
    Args:
        value (int): integer to print.
    Returns:
        True if value has been correctly printed, False otherwise.
    """

    try:
        print("{:d}".format(value))
        return True
    except ValueError as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
        return False
