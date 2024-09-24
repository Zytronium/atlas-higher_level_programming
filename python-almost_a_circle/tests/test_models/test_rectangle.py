import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle

def get_output(func):
    """
    returns the output from stdout printed in func
    :param func: function call which prints something to stdout
    :return: what is printed when the given function runs
    """
    with patch('sys.stdout', new=StringIO()) as captured_output:
        func()  # Call the function
        return captured_output.getvalue()

class MyTestCase(unittest.TestCase):
    def test0_general(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        r2d2 = Rectangle(1, 2)
        self.assertEqual(r.id + 1, r2d2.id)
        self.assertEqual(r.to_dictionary(), {'id': r2d2.id - 1, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test1_negative_or_0_or_not_int(self):
        expected_error = TypeError("width must be an integer")
        raised_error = None
        try:
            Rectangle(1.5, 2, 4, 4)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = ValueError("width must be > 0")
        raised_error = None
        try:
            Rectangle(0, -2, 4, 4)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = TypeError("height must be an integer")
        raised_error = None
        try:
            Rectangle(2, "2")
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = ValueError("height must be > 0")
        raised_error = None
        try:
            Rectangle(2, -2, 4, 4)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = ValueError("height must be > 0")
        raised_error = None
        try:
            Rectangle(2, 0, 1, 4)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = TypeError("x must be an integer")
        raised_error = None
        try:
            Rectangle(2, 2, "X", 4)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))

        expected_error = TypeError("y must be an integer")
        raised_error = None
        try:
            Rectangle(2, 2, 2, 4.5)
        except Exception as e:
            raised_error = e
        finally:
            self.assertEqual(repr(raised_error), repr(expected_error))
        r = Rectangle(11, 1, 1, 0, 4)
        self.assertEqual(str(r), "[Rectangle] (4) 1/0 - 11/1")
        r.update(id=5, width=12, hawiuhdiufha=53, height=10)
        self.assertEqual(str(r), str(Rectangle(12, 10, 1, 0, 5)))

    def test2_display(self):
        expected_output = "##\n"
        self.assertEqual(get_output(Rectangle(2, 1).display), expected_output)
        expected_output = ("###\n"
                           "###\n"
                           "###\n"
                           "###\n")
        self.assertEqual(get_output(lambda: Rectangle(3, 4).display()), expected_output)  # the error occurs between here and the next line, on a line in unittestpy.py: "            output = sys.stdout.getvalue()"
        expected_output = ("\n"
                           "  ####\n"
                           "  ####\n")
        self.assertEqual(get_output(Rectangle(4, 2, 2, 1).display), expected_output)

    def test3_area(self):
        self.assertEqual(Rectangle(2, 2, 1).area(), 4)
        self.assertEqual(Rectangle(9, 1, 2).area(), 9)
        self.assertEqual(Rectangle(3, 5).area(), 15)
        self.assertEqual(Rectangle(1, 5, 0, 2).area(), 5)


if __name__ == '__main__':
    unittest.main()
