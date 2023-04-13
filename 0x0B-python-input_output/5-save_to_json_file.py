#!/usr/bin/python3
"""Contains the json module"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON rep"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
