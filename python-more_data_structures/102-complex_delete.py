#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        for n, n2 in dict(a_dictionary).items():
            if n2 == value:
                del a_dictionary[n]
    return a_dictionary
