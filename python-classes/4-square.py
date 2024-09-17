#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """A class named Square that defines a square."""
    def __init__(self, size=0):
        """Initializes the Square instance.
        Args:
            size (int): The size of the square initialized in zero.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args:
            value (int): The size of the square.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method that Calculates the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size ** 2
