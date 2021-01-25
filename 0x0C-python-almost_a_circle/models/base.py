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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of dictionaries of instances to save.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='UTF8') as s_file:
            if list_objs is None:
                s_file.write('[]')
            else:
                dic_list = []
                for ins in list_objs:
                    dic_list.append(ins.to_dictionary())
                s_file.write(Base.to_json_string(dic_list))

    @staticmethod
    def from_json_string(json_string):
        """Creates a list from a JSON string representation
        of list of dictionaries.

        Args:
            json_string (string): JSON string to convert to list.

        Return:
            list object from "json_string" argument.
        """
        if json_string is None or not bool(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set.

        Args:
            kwargs (dictionary): key/value pairs to set.

        Return:
            Instance of class with attributes settealready set.
        """
        if cls.__name__ == 'Rectangle':
            new_ins = cls(1, 1)
        if cls.__name__ == 'Square':
            new_ins = cls(1)
        new_ins.update(**dictionary)
        return new_ins
