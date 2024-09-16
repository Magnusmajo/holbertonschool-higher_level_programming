#!/usr/bin/python3
"""take max integer"""


def max_integer(list=[]):
    """
    Compares list and returns max integer
    """
    if not list:
        return None
    result = list[0]
    for i in range(len(list)):
        if list[i] > result:
            result = list[i]
    return result
