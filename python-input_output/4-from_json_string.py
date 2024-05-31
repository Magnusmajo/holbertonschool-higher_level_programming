#!/usr/bin/python3
"""
From JSON string to Object
"""
import json


def from_json_string(my_str):
    """Convert an object to a JSON string.

    This function takes an object as input and returns a JSON string representation
    of the object. The function uses the json module's dumps function to convert
    the object to a JSON string.

    Args:
        my_obj (object): The object to convert to a JSON string.

    Returns:
        str: A JSON string representation of the input object.
    """
    return json.loads(my_str)
