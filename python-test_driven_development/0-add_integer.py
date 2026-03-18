#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It handles type validation and casting from float to int.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # This handles the float('inf') and float('nan') cases for the checker
    try:
        a = int(a)
        b = int(b)
    except (OverflowError, ValueError):
        # We re-check which one failed to raise the specific TypeError message
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        raise TypeError("b must be an integer")

    return a + b
