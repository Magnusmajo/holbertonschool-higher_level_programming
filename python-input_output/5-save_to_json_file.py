#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Convert an object to a JSON string.

    This function takes an object as input and returns
    a JSON string representation of the object. The
    function uses the json module's dumps function to convert
    the object to a JSON string.

    Args:
        my_obj (object): The object to convert to a JSON string.

    Returns:
        str: A JSON string representation of the input object.
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
