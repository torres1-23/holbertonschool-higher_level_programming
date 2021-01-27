#!/usr/bin/python3
"""This module defines unittest for module "rectangle.py"

Usage:
    Use with unittest module to check if "rectangle" module is
    well implemented.
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestBase01(unittest.TestCase):
    """Check instantiation of Rectangle instances."""
    def test_01(self):
        """Check right inheritance."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_02(self):
        """Check behavior with args and id attribute."""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 43)
        r = Rectangle(2, 2, 4)
        self.assertEqual(r.id, 44)
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.id, 45)
        r = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual(r.id, 7)

    def test_03(self):
        """Check behavior with args and x getter
        and setter."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_04(self):
        """Check behavior with args and y getter
        and setter."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_05(self):
        """Checks exception raises."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestBase02(unittest.TestCase):
    """Check correct implementation of "area" method."""
    def test_01(self):
        """Check right return of method."""
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_02(self):
        """Check exception raises."""
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestBase03(unittest.TestCase):
    """Check correct implementation of "display" method."""
    @staticmethod
    def capture_stdout(rect, method):
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
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_01(self):
        """Check right print of method."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestBase03.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestBase03.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestBase03.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestBase03.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_02(self):
        """Check exception raises."""
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestBase04(unittest.TestCase):
    """Check correct implementation of __str__ method."""
    def test01(self):
        """Check right implementation of __str__."""
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))
        r = Rectangle(1, 2, 3, 4, 5)

    def test_02(self):
        """Check exception raises."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestBase05(unittest.TestCase):
    """Check correct implementation of update method."""
    def test01(self):
        """Check right implementation of update
        with args."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_02(self):
        """Check right implementation of update
        with kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_03(self):
        """Check exception raises."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)


if __name__ == '__main__':
    unittest.main()
