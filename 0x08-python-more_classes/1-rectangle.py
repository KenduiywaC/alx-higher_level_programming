#!/usr/bin/python3
"""1-rectangle, built for 0x08. Python - More Classes and Objects task 1.
"""


class Rectangle:
 """Class creates two private instance attributes by
    using two arguments.


 Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height



    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
