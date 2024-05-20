#!/usr/bin/python3
"""
Square:
A class that defines a square
"""


class Square:
    """_init_
    main function for square
    """
    def __init__(self, size=0):
        """
        Args:
            size (int, optional): Size for the square. Defaults to 0.
        """
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """
        The square 
        Raises:
            TypeError: Size not int
            ValueError: Size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """
        Returns:
        int : Area of square
        """
        return self.__size * self.__size
