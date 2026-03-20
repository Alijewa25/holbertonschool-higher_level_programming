#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the current square's area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2
