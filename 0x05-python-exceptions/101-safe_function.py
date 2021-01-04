#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    """ Executes a function safely.
    Args:
        fct (function):
        *args: arguments for the function.
    Returns:
        the result of the function, otherwise, returns None
    """

    try:
        return (fct(*args))
    except Exception as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
        return None
