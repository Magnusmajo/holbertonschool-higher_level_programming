#!/usr/bin/python3
"""inserts a line of text to a file"""

def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
    Args:
        filename: name of the file
        search_string: string to search
        new_string: string to insert
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
