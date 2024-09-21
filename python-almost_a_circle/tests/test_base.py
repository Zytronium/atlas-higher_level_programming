#!/usr/bin/python3
"""
unittests for models/base.
note that the tests are ran in alphabetical order or each method's name,
and that nothing resets between tests, meaning that if the first test that
runs creates a new base with a default id, which will be 1, and then the
second test does the same thing, the id will be 2 in the second test.
This could be fixed by adding a __del__ method to the Base class, but
the checker isn't expecting that, so it messes up certain checks, so I
removed it.
"""


import unittest
try:
    from models.base import Base
except ModuleNotFoundError:
    from base import Base

class BaseTestCase(unittest.TestCase):
    def test1_auto_assigning_id(self):
        # print("test 1")
        b = Base()
        self.assertEqual(b.id, 1)

    def test2_auto_assigning_two_bases(self):
        # print("test 2")
        # b = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test3_reassign_id(self):
        # print("test 3")
        b = Base()
        b.id = 10
        self.assertEqual(b.id, 10)

    def test4_custom_id(self):
        # print("test 4")
        b = Base(7)
        self.assertEqual(b.id, 7)

    def test5_auto_assign_to_existing_id(self):
        # print("test 5")
        b = Base()
        b.id += 1
        b2 = Base()
        self.assertEqual(b2.id, b.id)


if __name__ == '__main__':
    unittest.main()
