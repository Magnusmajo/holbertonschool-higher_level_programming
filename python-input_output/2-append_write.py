#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """Append text to a file.

    This function appends the given text to the specified file.
    If the file does not exist, it will be created. The function
    uses the 'a' mode when opening the file, which stands for
    "append" and means that the text will be added to
    the end of the file.

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
