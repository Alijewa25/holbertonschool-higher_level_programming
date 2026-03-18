#!/usr/bin/python3
"""
This module provides a function to add two numbers.
It includes strict type checking for integers and floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers after casting floats to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats, 
        or if they are NaN/Infinity.

    Returns:
        The sum of a and b as an integer.
    """
    # Explicitly check for float('inf') or float('nan')
    # Because int(inf) or int(nan) raises ValueError, not TypeError
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handling edge cases where float is valid type but cannot be cast to int
    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
