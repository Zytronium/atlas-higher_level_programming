#!/usr/bin/python3
"""
unittests for models/base
"""


import unittest
from io import StringIO
from unittest.mock import patch
try:
    from models.square import Square
except ModuleNotFoundError:
    from square import Square


def get_output(func):
    """
    returns the output from stdout printed in func
    :param func: function call which prints something to stdout
    :return: what is printed when the given function runs
    """
    with patch('sys.stdout', new=StringIO()) as captured_output:
        func()  # Call the function
        return captured_output.getvalue()

class SquareTestCase(unittest.TestCase):
    def test_0is_size(self):
        expected_error = ValueError("width must be > 0")
        raised_error = None
        try:
            square = Square(0)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

    def test_1auto_assign_id(self):
        s = Square(5)
        s2 = Square(5)
        self.assertEqual(s.id, s2.id - 1)

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

    def test_5update_args(self):
        s = Square(10, 8, 3, 3)
        s.update(40, 6, 4, 2)
        self.assertEqual(str(s), "[Square] (40) 4/2 - 6")
        self.assertEqual(s.to_dictionary(), {'id': 40, 'size': 6, 'x': 4, 'y': 2})

    def test_5update_kwargs(self):
        s = Square(10, 8    , 3, 3)
        s.update(size=6, id=35, x=4, width=50)
        # 'width' shouldn't update anything
        self.assertEqual(str(s), "[Square] (35) 4/3 - 6")
        self.assertEqual(s.width, 6)

    def test_6negative_size(self):
        expected_error = ValueError("width must be > 0")
        raised_error = None
        try:
            square = Square(-15)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

    def test_7negative_position(self):
        expected_error = ValueError("x must be >= 0")
        raised_error = None
        try:
            square = Square(100, -2, -5)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = ValueError("y must be >= 0")
        raised_error = None
        try:
            square = Square(100, 3, -5)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = None
        raised_error = None
        try:
            square = Square(100, 0, 0)
            square2 = Square(100, 2)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

    def test_8not_integers(self):
        expected_error = TypeError("width must be an integer")
        raised_error = None
        try:
            square = Square(5.5)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = TypeError("x must be an integer")
        raised_error = None
        try:
            square = Square(14, 3.5, 6.2)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = TypeError("y must be an integer")
        raised_error = None
        try:
            square = Square(14, 4   , False)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

    def test9_display(self):
        expected_output = ("##\n"
                           "##\n")
        self.assertEqual(get_output(Square(2, 0).display), expected_output)
        expected_output = ("    ###\n"
                           "    ###\n"
                           "    ###\n")
        self.assertEqual(get_output(Square(3, 4).display), expected_output)
        expected_output = ("\n\n"
                           " ##\n"
                           " ##\n")
        self.assertEqual(get_output(Square(2, 1, 2,  1).display), expected_output)

    def test9_1_area(self):
        self.assertEqual(Square(3, 2, 1).area(), 9)
        self.assertEqual(Square(10, 0, 2).area(), 100)
        self.assertEqual(Square(1, 0, 0, 5).area(), 1)

if __name__ == '__main__':
    unittest.main()
