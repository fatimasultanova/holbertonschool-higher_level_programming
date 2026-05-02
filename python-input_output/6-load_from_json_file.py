#!/usr/bin/python3
"""
Load data from json file
"""
import json


def load_from_json_file(filename):
    """
    Load data from json file
    Args:
        filename:
    """
    with open(filename, 'r') as f:
        return json.load(f)
