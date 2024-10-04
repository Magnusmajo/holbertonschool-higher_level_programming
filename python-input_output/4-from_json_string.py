#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """Convert an object to a JSON string.
    Args:
        my_obj (object): The object to convert to a JSON string.
    Returns:
        str: A JSON string representation of the input object.
    """
    return json.loads(my_str)
