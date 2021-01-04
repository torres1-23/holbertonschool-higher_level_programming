#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list.
    Args:
        my_list (list): list to print.
        x (int): number of items on the list to print.
    Returns:
        the real number of elements printed.
    """

    cont = 0
    try:
        for item in my_list:
            if cont == x:
                break
            cont += 1
            print(item, end="")
        print()
        return cont
    except TypeError:
        pass
