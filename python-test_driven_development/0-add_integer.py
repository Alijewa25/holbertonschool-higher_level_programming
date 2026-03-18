#!/usr/bin/python3
"""
This module provides a function to add two numbers.
It includes type checking and casting for floats to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integer if they are floats
    return int(a) + int(b)
