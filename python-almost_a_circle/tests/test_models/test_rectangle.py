import unittest
from models.rectangle import Rectangle


class MyTestCase(unittest.TestCase):
    def test0_general(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        r2d2 = Rectangle(1, 2)
        self.assertEqual(r.id + 1, r2d2.id)

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

    def test2_display(self):
        expected_output = "##"
        self.assertEqual(Rectangle(2, 1).display(), expected_output)
        expected_output = ("###\n"
                           "###\n"
                           "###\n"
                           "###\n")
        self.assertEqual(Rectangle(3, 4).display(), expected_output)
        expected_output = ("\n"
                           "  ###\n"
                           "  ###\n")
        self.assertEqual(Rectangle(4, 2, 2,  1).display(), expected_output)

if __name__ == '__main__':
    unittest.main()
