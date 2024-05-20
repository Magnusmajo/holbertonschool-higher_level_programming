#!/usr/bin/python3
"""
Square:
# This is a Python class named 'Square' that represents a square shape.
"""


class Square:
    """
    This is the constructor method for the 'Square' class. 
    It initializes the size of the square.
    """
    def __init__(self, size):
        """
        The size of the square is stored as a private instance variable.
        Args:
            size (_type_): _description_
        """
        self.__size = size
