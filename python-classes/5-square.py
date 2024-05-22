class Square:
    """_
    A class definition
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        _init_
        main construction function for square
        Args:
            size (int, arg): Size for the square. Defaults to 0.
            position (tuple, arg): Position of the square. Defaults to (0, 0).
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """
        size: It defines the size of the square
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        The value for the size function

        Raises:
            TypeError: Size not int
            ValueError: Size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        The position of the square
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        The position of the square

        Raises:
            TypeError: Position not tuple
            ValueError: Position not tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value)!= 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for pos in value:
            if not isinstance(pos, int) or pos < 0:
                raise ValueError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        The area

        Returns:
            int: Area of square
        """
        return self._size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        """
        if self._size == 0:
            print("")
        else:
            for i in range(self._position[1]):
                print()
            for i in range(self._size):
                for j in range(self._position[0]):
                    print(" ", end='')
                for j in range(self._size):
                    print("#", end='')
                print()