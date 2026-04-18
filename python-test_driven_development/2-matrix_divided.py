#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It ensures the matrix is valid and each row has the same size.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number (int or float) to divide by.

    Returns:
        A new matrix containing the division results.

    Raises:
        TypeError: If matrix is invalid or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        new_matrix.append(new_row)
    return new_matrix
