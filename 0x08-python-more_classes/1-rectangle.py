#!/usr/bin/python3
""" A class oject: Rectangle"""


class Rectangle:
    """ Initialising the given Rectangle with attributes
        private 'width' and
        private height

        Args:
        self.__width = width
        self.__height = height
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

        """ Giving main Attributes to the class: Rectangle"""
    @property
    def width(self):
        return self.width
    
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
