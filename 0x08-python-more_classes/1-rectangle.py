#!/usr/bin/python3
"""A class oject: Rectangle"""


class Rectangle:
    """
    Rectangle initialised with the following attributes
    Private 'width' and
    private height
    Args:
        width (int) : width
        height (int) : height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """Giving main Attributes to the class: Rectangle"""
    @property
    def width(self):
        """ The getter will return Rectangle width"""
        return self.width

    @width.setter
    def width(self, value):
        """The setter sets with to always be > 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the getter will return Rectangle width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter makes sure that height is always > o"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
