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
        b = Base()
        b.id = 2
        self.assertEqual(b.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, b.id)

    def test_unittesting(self):
        self.assertTrue(True)
        self.assertEqual(2 + 2, 4)
        new_base = Base()
        print(new_base.id)
        self.assertEqual(new_base.id, 1)


if __name__ == '__main__':
    unittest.main()
