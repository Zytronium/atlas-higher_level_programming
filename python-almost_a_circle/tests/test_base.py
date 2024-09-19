#!/usr/bin/python3

import unittest
from models.base import Base


class MyTestCase(unittest.TestCase):
    def test_something(self):
        b = Base(10)
        self.assertEqual(b.id, 10)  # add assertion here
        b.id = 3
        self.assertEqual(b.id, 3)


if __name__ == '__main__':
    unittest.main()
