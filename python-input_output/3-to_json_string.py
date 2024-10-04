#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """Convert an object to a JSON string.
    Args:
        my_obj (object): The object to convert to
        a JSON string.
    Returns:
        str: A JSON string representation of the
        input object.
    """
    return json.dumps(my_obj)
