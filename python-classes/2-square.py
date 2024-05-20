#!/usr/bin/pyton3
"""
    Square:
    A class that defines a square
"""


class Square:
    """
    A class that defines a square
    Args:
    size(int): The size of the square
    """
    def __init__(self, size=0):
        """
        Check if the side is an integer
        Args:
        size(int): The size of the square
        
        Raises:
        TypeError: If the size is not an integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
