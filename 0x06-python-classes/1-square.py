#!/usr/bin/python3
"""Class prints a Square with attribute Size"""


class Square:
    """Represents a Square with size"""

    def __init__(self, size):
        """Initialises a new suare.

        Args:
            size(int): the size of the given square
            """
        self.__size = size
