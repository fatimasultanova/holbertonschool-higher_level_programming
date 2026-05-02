#!/usr/bin/python3
"""
It includes a function for writing text to a file in append mode, ensuring that
the text is encoded in UTF-8.
"""


def append_write(filename='', text=''):
    """
        Write text to a file
    Args:
        filename:
        text:
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
