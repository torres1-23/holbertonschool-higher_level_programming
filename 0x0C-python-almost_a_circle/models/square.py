#!/usr/bin/python3
"""This module defines a class "class Square"."""
from models.rectangle import Rectangle
keys = ['id', 'size', 'x', 'y']


class Square(Rectangle):
    """This class defines instaces of square, inherits from class
        "Rectangle".
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of square.

        Args:
            size(int): size of each instance.
            x (int, optional): attribute x of each instance,
            0 by default.
            y (int, optional): attribute y of each instance,
            0 by default.
            id (int, optional): id of each instance,
            None by default.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Computes string representation of each Square instance.

        Return:
            String representation of each Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Gets size attribute of each instance.

        Return:
            Size of each instance.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets size attribute of each instance.

        Args:
            value (int): value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute or
        a key/value argument to attributes.

        Args:
            args (tuple): arguments to update.
            kwargs (dictionary): key/value pairs to update.
        """
        if args and len(args) > 0:
            i = 0
            for arg in args:
                if i is 0 and arg is None:
                    continue
                else:
                    try:
                        exec('self.{} = arg'.format(keys[i]))
                        i += 1
                    except IndexError:
                        break
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in keys:
                    if key == 'id' and value is None:
                        continue
                    else:
                        exec('self.{} = {}'.format(key, value))

    def to_dictionary(self):
        """Creates dictionary representation of Square.

        Return:
            dictionary with each attribute of square instance.
        """
        dic = {}
        for key in keys:
            exec('dic[key] = self.{}'.format(key))
        return dic
