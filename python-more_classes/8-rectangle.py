#!/usr/bin/python3
"""module for a rectangle class
"""


class Rectangle:
    """a class representing a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

    def __str__(self):
        return "" if self.__width == 0 or self.__height == 0 else ((str(
            self.print_symbol) * self.__width + '\n'
            ) * self.__height).removesuffix('\n')

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")  # This rectangle's out of shape, permanently
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """
        calculates the area of the rectangle
        :return: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        :return: the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height) if \
            self.__height != 0 and self.__width != 0 else 0

    def bigger_or_equal(rect_1, rect_2):
        """
        calculates the largest rectangle of the two given rectangles.
        note: rect_1 is the 'self' parameter, and will be referred to as 'this'
        :param rect_1: this rectangle, aka the first rectangle to check.
        Must be a Rectangle
        :param rect_2: the second rectangle to check. Must be a Rectangle
        :return: the rectangle with the biggest area,
        or the first one (this rectangle) if they are equal
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area >= rect_2.area else rect_2
