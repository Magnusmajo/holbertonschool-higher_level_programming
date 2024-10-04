#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """Append text to a file.
    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
