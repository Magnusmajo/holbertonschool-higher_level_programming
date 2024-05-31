#!/usr/bin/python3
"""
Writes a string to a text file and return the
numbers of characters written
"""

def write_file(filename="", text=""):
    """
        Writes a string to a text file and return the
        numbers of characters written
        """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
