#!/usr/bin/python3
"""This module defines a class "class Base"."""


class Base:
    """This class manage the attribute "id" in all clases
    in order to avoid duplicating the same code.

    Attributes:
        __nb_objects (int): number of base instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instance of base.

        Args:
            id (int, optional): id of each instance, None by default.

        Attributes:
            id (int): id of each instance.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
