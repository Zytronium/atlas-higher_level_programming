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
    
    def test_float(self):
        list = [-2, -1, 0, 1, 2, 3.14159, 4, 5, 10]
        self.assertEqual(max_integer(list), 10)
        
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
