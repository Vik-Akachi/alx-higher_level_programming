#!/usr/bin/python3
""" Will return the number of bytes"""


def write_file(filename="", text=""):
    """this code returns the byte count of the strings"""
    with open(filename, 'w', encoding="utf=8") as f:
        return f.write(text) 
