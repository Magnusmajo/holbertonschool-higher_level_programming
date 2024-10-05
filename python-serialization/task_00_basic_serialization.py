#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the data and save it to the specified file."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """ Load and deserialize data from the specified file."""

    with open(filename, 'r') as f:
        data = json.load(f)
    return data
