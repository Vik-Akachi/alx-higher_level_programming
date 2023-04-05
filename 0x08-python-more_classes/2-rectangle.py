#!/usr/bin/python3
"""
    module 2-rectangle with a private attribute width and height
                    public methods area and perimeter.
"""


class Rectangle:
    """
    Defines the class Rectangle with private attributes width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """Initialises Rectangles"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if the value > 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """Getter returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if the value > 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the width * 2 + heighty * 2"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
