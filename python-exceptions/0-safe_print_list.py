#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    getal = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            getal += 1
    except IndexError:
        pass
    print("")
    return getal
