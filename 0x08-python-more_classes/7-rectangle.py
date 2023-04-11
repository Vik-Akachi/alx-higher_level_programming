#!/usr/bin/python3
"""                                                                                                                                              Module 3-rectangle:
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
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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

        rectangle = []
        for a in range(self.__height):
            [rectangle.append('#') for b in range(self.__width)]
            if a != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """
        This Returns the string representation of the Rectangle
        """
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """ This action deletes the rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
