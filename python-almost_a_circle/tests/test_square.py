import unittest
"""
unittests for models/base
"""


import unittest
try:
    from models.square import Square
except ModuleNotFoundError:
    from square import Square

class SquareTestCase(unittest.TestCase):
    def test_auto_assign_id(self):
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_assign_id(self):
        s = Square(1, id=3)
        self.assertEqual(s.id, 3)

    def test_reassign_id(self):
        s = Square(1, id=3)
        s.id += 98
        self.assertEqual(s.id, 101)


if __name__ == '__main__':
    unittest.main()
