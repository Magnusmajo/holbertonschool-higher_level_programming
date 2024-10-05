#!/usr/bin/python3
"""Save to JSON file module"""
import json


def save_to_json_file(my_obj, filename):
    """Save to JSON file function
    Args:
        my_obj: object to be saved
        filename: name of the file
        Returns:
        str: A Json string representation
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
