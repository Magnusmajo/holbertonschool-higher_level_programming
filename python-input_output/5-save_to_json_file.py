#!/usr/bin/python3
"""Save to JSON file module"""


def save_to_jason(my_obj, filename):
    """Save to JSON file function
    Args:
        my_obj: object to be saved
        filename: name of the file
    """
    import json

    with open(filename, 'w') as f:
        json.dump(my_obj, f)