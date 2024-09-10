#!/usr/bin/python3
"""Module for a rectangle class
"""


class Rectangle:
    """a class representing a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """
        retrieves the width of the rectangle
        :return: the width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        :param value: the value to set the width of the rectangle to
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """
        retrieves the height of the rectangle
        :return: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle
        :param value: the value to set the height of the rectangle to
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
