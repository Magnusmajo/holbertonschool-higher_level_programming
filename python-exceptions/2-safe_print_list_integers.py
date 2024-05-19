#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=None):
    if my_list is None or x is None:
        return 0
    tellen = 0
    for i in range(min(x, len(my_list))):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]), end="")
            tellen += 1
    print()
    return tellen
