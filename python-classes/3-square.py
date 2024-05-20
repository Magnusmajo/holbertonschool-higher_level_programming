#!/usr/bin/python3
"""
Square:
A class that defines a square
"""


class Square:
    """
    Check if the side is an integer
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size of the square
        """
        if not isinstance(size, int):
            """
            Raise a TypeError if size is not an integer
            """
            
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """
        Returns: the current square area
        """
        return self.__size * self.__size
