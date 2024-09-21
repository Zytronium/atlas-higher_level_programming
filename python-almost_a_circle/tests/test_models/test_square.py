#!/usr/bin/python3
"""
unittests for models/base
"""


import unittest
try:
    from models.square import Square
except ModuleNotFoundError:
    from square import Square

class SquareTestCase(unittest.TestCase):
    def test_1auto_assign_id(self):
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_2assign_id(self):
        s = Square(1, id=3)
        self.assertEqual(s.id, 3)

    def test_3reassign_id(self):
        s = Square(1, id=3)
        s.id += 98
        self.assertEqual(s.id, 101)

    def test_4string(self):
        s = Square(size=25, x=8, y=3, id=-15)
        self.assertEqual(str(s), "[Square] (-15) 8/3 - 25")


if __name__ == '__main__':
    unittest.main()
