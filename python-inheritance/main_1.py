#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('8-rectangle').BaseGeometry

print(issubclass(Rectangle, BaseGeometry))

r = Rectangle(5, 4)
