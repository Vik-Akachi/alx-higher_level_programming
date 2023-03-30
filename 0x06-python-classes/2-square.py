#!/usr/bin/python3
"""Define a Square"""


class Square:
    """ Class Represents a square"""

    def __init__(self, size=0):
        """Initilising a Square.

        Args:
            size(int) = 0: the size of the new square
        """
        self.__size = size
        """Introducing Errors and Exceptions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
