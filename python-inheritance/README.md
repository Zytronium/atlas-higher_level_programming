# Python - Inheritance

---
This project is all about inheritance.

Inheritance is basically where a class is a subclass of another class.
For example, if I recall correctly, in the high-level language, Kotlin, a Number is
a type or class which has several subclasses, such as integer, double, or float.
Another Kotlin example would be an IndexOutOfBoundsException, which is a subclass of
RuntimeException, which is a subclass of Exception, which is a subclass of Throwable.
A Python example would be a TypeError is a subclass of Exception, which is a
subclass of BaseException, which is a subclass of object. Similarly, bool is a
subclasses of int, which is a subclass of object.

The same goes for custom classes. You can make a class called BaseGeometry, and
then make a subclass called Rectangle, and then another subclass of that called
Square. Here is a relatively bare-bones example of how you would do this:

```Python
class BaseGeometry:
    pass

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(width=size, height=size)
        self.size = size

```
