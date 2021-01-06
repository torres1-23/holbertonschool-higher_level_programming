#!/usr/bin/python3

""" Define class Square. """


class Square:
    """ Represents a square. """

    def __init__(self, size=0):
        """ Initializes instance of square.
        Args:
            size (int): size of square.
        Attributes:
            __size (int): size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
