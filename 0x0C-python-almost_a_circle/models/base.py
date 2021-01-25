#!/usr/bin/python3
"""This module defines a class "class Base"."""
import json
import csv


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
        """Creates an instance with all attributes already set
        from a dictionary.

        Args:
            kwargs (dictionary): key/value pairs to set.

        Return:
            Instance of class with attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            new_ins = cls(1, 1)
        if cls.__name__ == 'Square':
            new_ins = cls(1)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """Loads a JSON string from file, obtains list rep
        and creates each instance passed.

        Return:
            list of Rectangle or Square instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            ins_list = []
            with open(filename, mode='r', encoding='UTF8') as s_file:
                new_list = Base.from_json_string(s_file.read())
                for instance in new_list:
                    ins_list.append(cls.create(**instance))
                return ins_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): List of dictionaries of instances to save.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', encoding='UTF8') as s_file:
            if list_objs is None:
                s_file.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    key_list = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == 'Square':
                    key_list = ['id', 'size', 'x', 'y']
                for ins in list_objs:
                    writer = csv.DictWriter(s_file, fieldnames=key_list)
                    writer.writerow(ins.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads a CSV string from file, obtains list rep
        and creates each instance passed.

        Return:
            list of Rectangle or Square instances.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='UTF8') as s_file:
                ins_list = []
                if cls.__name__ == 'Rectangle':
                    key_list = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == 'Square':
                    key_list = ['id', 'size', 'x', 'y']
                dic = csv.DictReader(s_file, fieldnames=key_list)
                for dictio in dic:
                    ins_list.append(cls.create(**dictio))
                return ins_list
        except FileNotFoundError:
            return []
