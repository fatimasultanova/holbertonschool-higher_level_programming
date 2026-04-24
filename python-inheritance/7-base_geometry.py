#!/usr/bin/python3
"""
Geometry class created
"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        """Calculate area of BaseGeometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate integer value

        Args:
            name (str): Name of integer.
            value (int): Integer value.
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
