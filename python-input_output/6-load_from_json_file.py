#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Load a JSON file and return the corresponding Python object.

    This function opens the specified file, reads its content,
    and parses it as a JSON object. The resulting Python object
    is then returned.

    Args:
        filename (str): The name of the file to load.

    Returns:
        object: The Python object corresponding to the JSON
        data in the file.
    """
    
    with open(filename, 'r') as f:
        return json.load(f)
