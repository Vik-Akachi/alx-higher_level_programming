#!/usr/bin/python3
"""Reads a file to the standard output"""


def read_file(filename=""):
    """a given text file can be read using this algorithm"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
