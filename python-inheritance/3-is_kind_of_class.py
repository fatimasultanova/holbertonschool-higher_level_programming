#!/usr/bin/python3
"""
Python Inheritance Rules
"""


def is_kind_of_class(obj, a_class):
    """Check if a class is a subclass of another class"""
    return type(obj) is a_class or issubclass(obj, a_class)
