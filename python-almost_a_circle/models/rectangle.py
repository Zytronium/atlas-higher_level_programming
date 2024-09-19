#!/usr/bin/python3
"""
a module containing a rectangle class
"""
from base import Base



class Rectangle(Base):
    """
    a class representing a rectangle.
    """

    def __init__(self, width: int, height: int, x: int=0, y: int=0, id:int=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
