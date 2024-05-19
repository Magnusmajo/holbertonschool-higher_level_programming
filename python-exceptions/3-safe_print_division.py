#!/usr/bin/python3

def safe_print_division(a, b):
    resultaat = None
    try:
        resultaat = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside resultaat: {}".format(result))
    return resultaat
