#!/usr/bin/python3
def best_score(a_dictionary):
    """ Returns a key with the biggest integer value. """
    if (a_dictionary):
        big_n = max(a_dictionary.values())
        for key in a_dictionary:
            if a_dictionary[key] == big_n:
                return key
    return None
