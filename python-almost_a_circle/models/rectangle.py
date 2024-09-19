#!/usr/bin/python3
"""
a module containing a rectangle class
"""
try:
    from models.base import Base
except ModuleNotFoundError:
    from base import Base


class Rectangle(Base):
    """
    a class representing a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        gets the width of the rectangle
        :return: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets the width of the rectangle
        :param width: the value to set as the new width of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        gets the height of the rectangle
        :return: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets the height of the rectangle
        :param height: the value to set as the new height of the rectangle
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        gets the x value of the rectangle
        :return: the coordinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        sets the x value of the rectangle
        :param x: the value to set as the new x coordinate of the rectangle
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        gets the y value of the rectangle
        :return: the y coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        sets the y value of the rectangle
        :param y: the y coordinate of the rectangle
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        calculates the area of the rectangle
        :return: the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        displays the rectangle by printing it to stdout
        """
        print(("#" * self.__width + '\n') * self.__height, end='')


if __name__ == "__main__":
    r = Rectangle(10, 4, 0, 0)
    print(r.width)
    r.display()
