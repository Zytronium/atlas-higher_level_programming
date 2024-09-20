#!/usr/bin/python3
"""
unittests for models/base
"""


import unittest
try:
    from models.base import Base
except ModuleNotFoundError:
    from base import Base

class MyTestCase(unittest.TestCase):
    def test_auto_assigning_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b2.id = 3
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_auto_assigning_two_bases(self):
        b = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_reassign_id(self):
        b = Base()
        b.id = 3
        self.assertEqual(b.id, 3)

    def test_custom_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_auto_assign_to_existing_id(self):
        """
        my gosh, this needs a shorter name badly
        """
        b = Base()
        b.id = 2
        self.assertEqual(b.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, b.id)


if __name__ == '__main__':
    unittest.main()
