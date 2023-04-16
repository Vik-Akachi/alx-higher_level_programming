#!/usr/bin/python3
""""
    module name: 0-add_integer
    module task: adds two integers. if they are flooats
                they are converted into integers before addin"""


def add_integer(a, b=98):
    """checks for variable type"""

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
