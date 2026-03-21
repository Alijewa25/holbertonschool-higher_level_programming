#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square class with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square

        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square using # with position"""
        if self.__size == 0:
            print()
            return

        # vertical offset (y)
        for _ in range(self.__position[1]):
            print()

        # print square
        for _ in range(self.__size):
            # horizontal offset (x)
            print(" " * self.__position[0] + "#" * self.__size)
