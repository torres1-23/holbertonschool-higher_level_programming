#!/usr/bin/python3
"""This module defines a class "class Square"."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines instaces of square, inherits from class
        "Rectangle".
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of rectangle.

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
