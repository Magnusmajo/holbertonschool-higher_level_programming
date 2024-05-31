#!/usr/bin/python3
"""
Class to JSON
"""

def class_to_json(obj):
    """
    Function: class_to_json
    This function takes an object as an argument and returns a
    dictionary representation of the object, which can be easily
    serialized into JSON format. The dictionary contains only
    simple data structures, such as lists, dictionaries, strings,
    integers, and booleans.

    :param obj: The object to be converted into a dictionary.
    :return: A dictionary representation of the object, containing only simple data structures.
    """
    return {key: value for key, value in obj.__dict__.items()}
