#!/usr/bin/python3
"""
    Module 3-rectangle:
    module defines a rectangle with private attributes width and height
    public methods area and perimeter.
"""


class Rectangle:
    """
    Initialises a rectangle

    Args:
        width (int): width
        height (int): height

    Function:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        range()
        """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter returns width if value > 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise valueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter returns height if value > 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns 2*self.width  + 2*self.height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """this is used to return a representation of the rectangle.
        In this case # will be printed in instaead of integers
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for a in range(self.height):
            for b in range(self.width):
                rectangle +- str(self.print_symbol)
            if a != self.height -  1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """
        This Returns the string representation of the Rectangle
    """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This action deletes the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ this returns the greater rectangle"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
