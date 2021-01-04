#!/usr/bin/python3


def safe_print_integer(value):
    """ Prints a formatted integer.
    Args:
        value (int): integer to print.
    Returns:
        True if value has been correctly printed, False otherwise.
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
