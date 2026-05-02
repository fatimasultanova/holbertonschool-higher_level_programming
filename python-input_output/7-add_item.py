#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file named add_item.json.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item_to_list():
    """
    Loads existing list, appends new arguments, and saves back to JSON.
    """
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
