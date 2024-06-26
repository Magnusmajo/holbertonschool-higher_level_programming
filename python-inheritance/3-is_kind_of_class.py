#!/usr/bin/python3
"""
An inherist function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or
    if the class is in the object's inheritance tree.
    Args:
    obj: The object to check.
    a_class: The class to check against.
    Returns: True if obj is an instance of a_class or if
    a_class is in obj's inheritance tree, False otherwise.
    """
    return isinstance(obj, a_class)
