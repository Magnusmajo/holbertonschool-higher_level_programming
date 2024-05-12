#!/usr/bin/python3
def uppercase(str):
    for caracter in str:
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            caracter = chr(ord(caracter) - 32)
        print("{}".format(caracter), end="")
    print("")
