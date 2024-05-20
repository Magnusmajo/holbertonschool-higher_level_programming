#!/usr/bin/python3

class Square:
    """
    A class that defines a square.
    """
    def __int__(self, size=0):
        """
        Initializes a new instance of the class.
        Args:
        size (int): The size of the square.
        """
    iftype(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
    
    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self._size
