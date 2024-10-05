#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    Class to JSON function
    Args:
        obj: object to be converted to dictionary
    Returns:
        dict: dictionary representation of a simple data structure
    """
    return {key: value for key, value in obj.__dict__.items()}
