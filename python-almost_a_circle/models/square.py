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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
