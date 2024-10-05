#!/usr/bin/python3
"""inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
    Args:
        filename: name of the file
        search_string: string to search
        new_string: string to insert
    """
    text = ""
    with open(filename) as r:
        for lines in r:
            text += lines
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
