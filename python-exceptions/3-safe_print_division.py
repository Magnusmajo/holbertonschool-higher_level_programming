#!/usr/bin/python3

def safe_print_division(a, b):
    resultaat = 0
    try:
        resultaat = a / b
    except ZeroDivisionError:
        resultaat = None
    finally:
        print("Inside resultaat: {}".format(resultaat))
        return resultaat
