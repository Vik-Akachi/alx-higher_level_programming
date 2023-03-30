#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """"Initiates the Square Attributes"""

    def __init__(self, size=0):
        """initialising a new square.

        Args:
            (int)size: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """calling the methods to be applied on the attribute"""

    def area(self):
        """ Returns the current area of the square"""
        return (self.__size * self.__size)
