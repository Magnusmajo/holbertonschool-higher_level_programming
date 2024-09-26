#!/usr/bin/python3
"""
A function
"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class
    Args:
        obj: The object to check
        a_class: The class to check against
    Returns:
        True if obj is an instance of a_class, False otherwise
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
