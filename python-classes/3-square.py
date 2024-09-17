#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """A class named Square that defines a square."""
    def __init__(self, size=0):
        """Initializes the Square instance.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
