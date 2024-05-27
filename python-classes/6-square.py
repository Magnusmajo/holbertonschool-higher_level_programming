#!/usr/bin/python3
"""
Square:
    A class that defines a square
"""

class Square:
    """_
    A class definition
    """
    def __init__(self, size=0):
        """
        _init_
    main construction function for square
        Args:
            size (int, arg): Size for the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        size: It defines the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The value for the size function

        Raises:
            TypeError: Size not int
            ValueError: Size < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        position setter
        Args:
        value (tuple): A tuple of two positive integers
        Raises:
        TypeError: If value is not a tuple of two positive integers
        """

        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(j >= 0 for j in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        area: Calculate the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        my_print: Prints the square
        """

        if (self.__size == 0):
            print()
            return

        [print() for a in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end='') for j in range(self.__position[0])]
            [print("#", end='') for k in range(self.__size)]
            print()
