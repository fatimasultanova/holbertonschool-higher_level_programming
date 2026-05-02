#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
        Creates a Pascal's triangle of size n.
    Args:
        n:

    Returns:

    """
    if n <= 0:
        return []
    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
