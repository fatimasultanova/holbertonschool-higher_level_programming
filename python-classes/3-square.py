#!/usr/bin/python3
"""
This module defines an empty class Square.
The Square class is used to represent a geometric square shape.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize a Square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size * self.__size
