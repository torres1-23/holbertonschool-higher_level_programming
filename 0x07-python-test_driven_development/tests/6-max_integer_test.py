#!/usr/bin/python3

"""This module defines function tests for
   "def max_integer(list=[])"

Usage:
    "python3 -m unittest tests.6-max_integer_test", it will run tests
    on the module 6-max_integer_test.py"
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines methodes to tests the module 6-max_integer_test.py"""

    def test_maxint1(self):
        """Test an ordered list of integers."""
        list_1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_1), 4)

    def test_maxint2(self):
        """Test an unordered list of integers."""
        list_2 = [98, 798, 0, 758]
        self.assertEqual(max_integer(list_2), 798)

    def test_maxint3(self):
        """Test a list with a beginning max value."""
        list_3 = [4875, 3, 2, 1]
        self.assertEqual(max_integer(list_3), 4875)

    def test_maxint4(self):
        """Test an empty list."""
        list_4 = []
        self.assertEqual(max_integer(list_4), None)

    def test_maxint5(self):
        """Test a list with a single element."""
        list_5 = [79652]
        self.assertEqual(max_integer(list_5), 79652)

    def test_maxint6(self):
        """Test a list of floats."""
        list_6 = [1.53, -6.33, -9.123, 158.2, 6.0]
        self.assertEqual(max_integer(list_6), 158.2)

    def test_maxint7(self):
        """Test a list of ints and floats."""
        list_7 = [13.53, 15.5, -9, 15, 6, 98]
        self.assertEqual(max_integer(list_7), 98)

    def test_maxint8(self):
        """Test a string."""
        list_8 = "Hello"
        self.assertEqual(max_integer(list_8), 'o')

    def test_maxint9(self):
        """Test a list of strings."""
        list_9 = ["Hello", "how", "are", "you"]
        self.assertEqual(max_integer(list_9), "you")

    def test_maxint10(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
