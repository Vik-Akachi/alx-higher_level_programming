#!/usr/bin/python3
"""Code to append texts to existing texts"""


def append_write(filename="", text=""):
    """this returns the number of bytes of characters from appendedn texts"""
    with open(filename, 'a', encoding="utf=8") as f:
        return f.write(text)
