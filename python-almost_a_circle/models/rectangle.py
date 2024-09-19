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

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

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
        top_space = '\n' * self.__y
        left_space = ' ' * self.__x
        row = "#" * self.__width + '\n'
        print(top_space, end='')
        print((left_space + row) * self.__height, end='')

    def update(self, *args, **kwargs):
        """
        updates the shape with specified args by assigning each given
        key/value argument to the associated attribute.
        Either args or kwargs must be given.
        kwargs can be a dictionary in any order, but must contain the keys
        "id", "width", "height", "x", and "y".
        args should be given in this order:

        1st argument: id

        2nd argument: width

        3rd argument: height

        4th argument: x

        5th argument: y

        :param args: no-keyword argument containing the arguments
        to update the shape with
        :param kwargs: key-worded argument containing the arguments
        to update the shape with
        """
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            if kwargs.__contains__('id'):
                self.id = kwargs.get('id')
            if kwargs.__contains__('width'):
                self.__width = kwargs['width']
            if kwargs.__contains__('height'):
                self.height = kwargs['height']
            if kwargs.__contains__('x'):
                self.x = kwargs['x']
            if kwargs.__contains__('y'):
                self.y = kwargs['y']


if __name__ == "__main__":
    r = Rectangle(10, 4, 0, 0)
    print(r.id, r.width)
    r.update(id=5, width=12, hawiuhdiufha=53, height=10)
    print(r.id, r.width)
