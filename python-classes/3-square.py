#!/usr/bin/python3
"""
This module defines a Square class with size validation and area calculation.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square side.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            The area of the square (size * size).
        """
        return self.__size * self.__size
