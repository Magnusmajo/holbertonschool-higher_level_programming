#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """A class named Square that defines a square."""
    def __init__(self, size=0):
        """Initializes the Square instance.
        Args:
            size (float or int): The size of the square initialized in zero.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args:
            value (float or int): The size of the square.
            Raises:
                TypeError: If size is not a number.
                ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that calculates the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on area."""
        return self.area() <= other.area()
