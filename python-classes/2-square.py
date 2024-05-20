#!/usr/bin/python3
    """_summary_

    Raises:
        TypeError: _description_
        ValueError: _description_
    """
class Square:
    """
    This is the constructor method for the 'Square' class. 
    It initializes the size of the square.
    """
    def __init__(self, size=0):
        """
        The size of the square is stored as a private instance variable.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
