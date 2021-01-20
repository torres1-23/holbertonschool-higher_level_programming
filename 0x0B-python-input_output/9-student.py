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

    def to_json(self):
        """Returns the dictionary description with simple
        data structure (list, dictionary, string, integer
        and boolean) for JSON serialization of an object

        Args:
            obj (object): class to retrieve its dictionary.

        Return:
            JSON string of dictionary.
        """
        return self.__dict__
