#!/usr/bin/python3
"""
A function
"""



def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a class.
    
    Return true if the object is exactly an instance of the specified class
    otherwise return false.
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
