#!/usr/bin/python3
Rectangle = __import__('10-square').Rectangle
BaseGeometry = __import__('10-square').BaseGeometry
Square = __import__('10-square').Square

print(issubclass(Rectangle, BaseGeometry))
print(f"{Rectangle.__name__} is a subclass of {Rectangle.__bases__[0].__name__}")

print(issubclass(Square, Rectangle))
print(f"{Square.__name__} is a subclass of {Square.__bases__[0].__name__}")

r = Rectangle(6, 4)

print(r)
print(str(r))
