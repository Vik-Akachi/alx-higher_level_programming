#!/usr/bin/python3
"""contains a json file"""

import json


def from_json_string(my_str):
    """ Returns an object(python data structure) represented ny json"""
    return json.loads(my_str)
