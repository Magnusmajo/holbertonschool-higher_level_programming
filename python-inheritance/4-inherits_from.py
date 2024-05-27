#!/usr/bin/python3
"""
A inherit function
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an 
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return True if issubclass(type(obj), a_class) \
        and type(obj) is not a_class else False
