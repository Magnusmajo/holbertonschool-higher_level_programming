#!/usr/bin/python3
"""
A function that returns the list of options
"""


def lookup(obj):
    """
    This function takes an object as input
    and returns a dictionary with the object's
    attributes as keys and their corresponding values as values.
    """
    return dir(obj)
