#!/usr/bin/python3
import unittest
try:
    from models.base import Base
except ModuleNotFoundError:
    from base import Base


class MyTestCase(unittest.TestCase):
    def test_auto_assigning_id(self):
        b = Base()
        self.assertEqual(b.id, 1)  # add assertion here
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b2.id = 3
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 3)


if __name__ == '__main__':
    unittest.main()
