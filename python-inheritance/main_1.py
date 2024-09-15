#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('8-rectangle').BaseGeometry

print(issubclass(Rectangle, BaseGeometry))
print(f"{Rectangle.__name__} is a subclass of {Rectangle.__bases__[0].__name__}")
