#!/usr/bin/python3
"""
This module defines an empty class Square.
"""


class Rectangle:
    """Rectangle class is used to represent a geometric square shape."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width of the square."""
        return self.__width

    @property
    def height(self):
        """Getting the height of the square."""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setting the width of the square.
        Args:
            value:
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setting the height of the square.
        Args:
            value:
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating the area of the square."""
        return self.width * self.height

    def perimeter(self):
        """Calculating the perimeter of the square."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
