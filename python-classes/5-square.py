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

    def area(self):
        """
        The area

        Returns:
            int: Area of square
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()