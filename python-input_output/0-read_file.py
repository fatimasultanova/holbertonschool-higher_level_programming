#!/usr/bin/python3
"""
Reading file
"""


def read_file(filename=''):
    """
        Method for reading file
    Args:
        filename:
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
