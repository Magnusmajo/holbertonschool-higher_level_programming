#!/usr/bin/python3
"""
Square:
A class that defines a square
"""


class Square:
    """_init_
    name of the class
    """
    def __init__(self, size=0):
        """
        Args:
            size (int, optional): Size for the square. Defaults to 0.

        Raises:
            TypeError: If not int
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            The area of the square
        """
        return self.__size * self.__size
