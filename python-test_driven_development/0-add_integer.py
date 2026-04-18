#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    Args:
        a: The first number. Must be an integer or a float.
        b: The second number. Must be an integer or a float. Defaults to 98.
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
        b = int(b)
    except (OverflowError, ValueError):
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        raise TypeError("b must be an integer")
    return a + b
