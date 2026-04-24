#!/usr/bin/python3
"""
Rectangle class created
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize Rectangle class
        Args:

           width (int): Width of rectangle.
           height (int): Height of rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """Representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
