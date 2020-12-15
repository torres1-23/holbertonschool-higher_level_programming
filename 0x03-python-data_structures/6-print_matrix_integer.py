#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ Prints a matrix of integers. """
    if matrix != [[]]:
        for row in matrix:
            for n in row:
                print("{:d}".format(n), end=" ")
            print("")
    else:
        print("")
