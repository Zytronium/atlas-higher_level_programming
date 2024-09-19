#!/usr/bin/python3
# __path__ = ['/home/SmartFridge/PycharmProjects/atlas-higher_level_programming/python-almost_a_circle/']
import unittest
from models.base import Base
# Base = __import__('python-    almost_a_circle.models.base.py').Base

class MyTestCase(unittest.TestCase):
    def test_something(self):
        b = Base(10)
        self.assertEqual(b.id, 10)  # add assertion here
        b.id = 3
        self.assertEqual(b.id, 3)
        print("test")


if __name__ == '__main__':
    unittest.main()
