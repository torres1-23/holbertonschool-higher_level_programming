#!/usr/bin/python3
"""This module defines unittest for module "square.py"

Usage:
    Use with unittest module to check if "square" module is
    well implemented.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestBase01(unittest.TestCase):
    """Check instantiation of Square instances."""
    def test_01(self):
        """Check right inheritance."""
        self.assertIsInstance(Square(10), Base)
        self.assertIsInstance(Square(10), Square)

    def test_02(self):
        """Check behavior with args and id attribute."""
        s = Square(10)
        self.assertEqual(s.id, 96)
        s = Square(2, 10)
        self.assertEqual(s.id, 97)
        s = Square(2, 2, 10)
        self.assertEqual(s.id, 98)
        s = Square(2, 2, 10, 988)
        self.assertEqual(s.id, 988)

    def test_03(self):
        """Check behavior with size setter and getter."""
        self.assertEqual(5, Square(5, 2, 3, 9).size)
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_04(self):
        """Check behavior with width setter and getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_05(self):
        """Check behavior with height setter and getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_06(self):
        """Check behavior with args x getter"""
        self.assertEqual(0, Square(10).x)

    def test_07(self):
        """Check behavior with args y getter"""
        self.assertEqual(0, Square(10).y)

    def test_08(self):
        """Checks exception raises."""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestBase02(unittest.TestCase):
    """Check correctimplementation of area method."""
    def test_01(self):
        """Check right return."""
        self.assertEqual(100, Square(10, 0, 0, 1).area())
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_02(self):
        """Check exception raises."""
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestBase03(unittest.TestCase):
    """Check correct implementation of str method."""
    def test_01(self):
        """Check right return."""
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_02(self):
        """Check exception raises."""
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)


class TestBase04(unittest.TestCase):
    """Check correct implementation of "display" method."""
    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.

        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_01(self):
        """Check right print."""
        s = Square(2, 0, 0, 9)
        capture = TestBase04.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())
        s = Square(3, 1, 0, 18)
        capture = TestBase04.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())
        s = Square(4, 0, 1, 9)
        capture = TestBase04.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())
        s = Square(2, 3, 2, 1)
        capture = TestBase04.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_02(self):
        """Check exception raises."""
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


if __name__ == '__main__':
    unittest.main()
