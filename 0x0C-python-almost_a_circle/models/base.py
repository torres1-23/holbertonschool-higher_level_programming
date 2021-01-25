#!/usr/bin/python3
"""This module defines a class "class Base"."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Creates the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.

        Return:
            JSON string rep of list_dictionaries.
        """
        if list_dictionaries is None or not bool(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)
