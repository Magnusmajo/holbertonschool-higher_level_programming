#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize and save data to the specified file.

    This function takes in a Python object (data) and
    a filename as arguments. It opens the file specified
    by the filename in write mode ('w') and uses
    the json.dump() function to serialize the data
    and write it to the file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.

    This function takes in a filename as an argument.
    It opens the file specified by the filename in read
    mode ('r') and uses the json.load()
    function to deserialize the data from the file.
    It returns the deserialized data.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data