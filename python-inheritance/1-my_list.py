#!/usr/bin/python3
"""
Python Inheritance Rules
"""


class MyList(list):
    """Mylist class crated"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
