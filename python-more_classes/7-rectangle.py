#!/usr/bin/python3
"""
This module defines an empty class Square.
"""


class Rectangle:
    """Rectangle class is used to represent a geometric square shape."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        """Printing different forms of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            rect_str += (self.print_symbol * self.__width) + "\n"

        return rect_str.strip()

    def __repr__(self):
        """Printing rectangle sizes."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deleting rectangle sizes."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
