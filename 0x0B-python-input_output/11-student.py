#!/usr/bin/python3

"""This module defines a class "class Student".

Usage:
    "Student" instanciates students and can return its dictionary.
"""


class Student:
    """Represents instance of student."""
    def __init__(self, first_name, last_name, age):
        """Initializes student instances.

        Args:
            first_name (string): first name of student.
            last_name (string): last name of student.
            age (int): age of student.

        Attributes:
            first_name (string): first name of student.
            last_name (string): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple
        data structure (list, dictionary, string, integer
        and boolean) for JSON serialization of an object

        Args:
            attrs (list, optional): lists of attributes to get.

        Return:
            JSON string of dictionary.
        """
        dic = {}
        if (type(attrs) is list and all(type(element) is
                                        str for element in attrs)):
            for key in attrs:
                if hasattr(self, key):
                    dic[key] = getattr(self, key)
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dictionary): dictionary of attributes to change.
        """
        for key, value in json.items():
            setattr(self, key, value)
