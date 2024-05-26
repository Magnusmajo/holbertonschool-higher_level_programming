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
    if isinstance(obj, a_class):
        return True
    for i in obj.__class__.__bases__:
        if issubclass(i, a_class):
            return True
    return False
