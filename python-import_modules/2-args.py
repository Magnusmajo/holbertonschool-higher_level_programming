#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cont = len(sys.argv) - 1
    if cont == 0:
        print("0 arguments.")
    elif cont == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cont))
    for i in range(cont):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
