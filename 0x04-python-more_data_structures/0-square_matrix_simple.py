#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix. """
    return [[pow(n, 2) for n in row] for row in matrix]
