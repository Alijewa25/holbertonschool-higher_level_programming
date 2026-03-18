#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
        b = int(b)
    except (OverflowError, ValueError):
        # This catches inf and nan and converts the error to the required TypeError
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        raise TypeError("b must be an integer")
    return a + b
