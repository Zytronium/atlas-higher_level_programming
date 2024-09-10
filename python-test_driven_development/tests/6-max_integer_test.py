#!/usr/bin/python3
"""
    Unittest for max_integer()
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_pos(self):
        list = [1, 2, 3, -10, 4, 2]
        self.assertEqual(max_integer(list), 4)

    def test_neg(self):
        list = [-2, -3, -4, -1, -5, -100 / 2]
        self.assertEqual(max_integer(list), -1)

    def test_first_num(self):
        list = [10, 9, 8, 7, 6, 5, 2, 3, 4, 1, 0]
        self.assertEqual(max_integer(list), 10)

    def test_float(self):
        list = [-2, -1, 0, 1, 2, 3.14159, 4, 5, 10]
        self.assertEqual(max_integer(list), 10)

    def test_list_of_one(self):
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_largest_is_float(self):
        self.assertEqual(max_integer([1, 2, 3.14159, 4, 5, 6.666, -7.5, -8, 2]), 6.666)

if __name__ == '__main__':
    unittest.main()
