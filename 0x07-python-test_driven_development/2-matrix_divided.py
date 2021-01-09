#!/usr/bin/python3

"""This module defines an integer division of all elements of a matrix
   by a divisor, function "matrix_divided(matrix, div)"

Usage:
    "matrix_divided(...)" returns a matrix with each division, must receive a
    valid matrix and a valid divisor.
"""


def matrix_divided(matrix, div):
    """Function that divides each element of a matrix.

    Args:
        matrix (list): matrix wich numbers will be divided.
        div (int): divisor for each matrix element.

    Raises:
        TypeError: if not valid matrix
        TypeError: if not valid element of matrix.
        TypeError: if div is not an int or float.
        ZeroDivisionError: if div is 0.

    Returns:
        list: Matrix already divided.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(error_msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(error_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
