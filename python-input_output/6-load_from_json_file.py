#!/usr/bin/python3
"""Create an Object JSON file"""


def load_from_json_file(filename):
    """Create an Object JSON file
    Args:
        filename: name of the file
    Returns:
        object: object created
    """
    import json

    with open(filename, 'r') as f:
        return json.load(f)
