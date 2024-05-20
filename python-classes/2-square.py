#!/usr/bin/python3
"""
    Square:
    A class that defines a square
"""


class Square:
    """__init__
    Initialized method

    Attributes:
        __size (int): Size of square(atribute).
    """

    def __init__(self, size=0):
        """
        Args:
            size (int): leng of thr square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
