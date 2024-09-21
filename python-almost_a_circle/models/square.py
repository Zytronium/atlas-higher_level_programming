#!/usr/bin/python3
"""
module containing a square shape inherited form Rectangle
"""
try:
    from models.rectangle import Rectangle
except ModuleNotFoundError:
    from rectangle import Rectangle


class Square(Rectangle):
    """
    A shape representing a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        gets the size of the square
        :return: the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        sets the size of the square
        :param size: the value to set the new size of the square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        updates the shape with specified args by assigning each given
        key/value argument to the associated attribute.
        Either args or kwargs must be given.
        kwargs can be a dictionary in any order, but must contain the keys
        "id", "size", "x", and "y".
        args should be given in this order:

        1st argument: id

        2nd argument: size

        3rd argument: x

        4th argument: y

        note that id is first instead of last, unlike when initializing

        :param args: no-keyword argument containing the arguments
        to update the shape with
        :param kwargs: key-worded argument containing the arguments
        to update the shape with
        """
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if kwargs.__contains__('id'):
                self.id = kwargs.get('id')
            if kwargs.__contains__('size'):
                self.size = kwargs['size']
            if kwargs.__contains__('x'):
                self.x = kwargs['x']
            if kwargs.__contains__('y'):
                self.y = kwargs['y']


