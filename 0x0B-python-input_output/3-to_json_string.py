#!/usr/bin/python3
"""A function that returns a json represenation of an object"""

import json
"""imports the module for jason"""


def to_json_string(my_obj):
    """This code returns a sereilaized object(string)"""
    json.dumps(my_obj)
