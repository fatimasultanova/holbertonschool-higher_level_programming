#!/usr/bin/python3
"""
Provides functionality to convert a Python object to its JSON string representation.
"""
import json


def to_json_string(amy_obj):
    """
        Converts a Python object to its JSON string representation.
    Args:
        amy_obj:
    """
    return json.dumps(amy_obj)
