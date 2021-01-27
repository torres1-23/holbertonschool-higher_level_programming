#!/usr/bin/python3
"""This module defines unittest for module "base.py"

Usage:
    Use with unittest module to check if "base" module is well implemented.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase01(unittest.TestCase):
    """Check instantiation of Base instances."""
    def test_01(self):
        """Check behavior when args is None and empty."""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base(None)
        self.assertEqual(b.id, 4)
        b = Base(None)
        self.assertEqual(b.id, 5)
        b = Base(None)
        self.assertEqual(b.id, 6)

    def test_02(self):
        """Check behavior with args."""
        b = Base(95)
        self.assertEqual(b.id, 95)
        b = Base(16)
        self.assertEqual(b.id, 16)
        b = Base(87)
        self.assertEqual(b.id, 87)
        b = Base(-9)
        self.assertEqual(b.id, -9)
        b = Base(100e+100)
        self.assertEqual(b.id, 100e+100)
        b = Base('hola')
        self.assertEqual(b.id, 'hola')
        b = Base(8.7)
        self.assertEqual(b.id, 8.7)
        b = Base({'a': 1, 'b': 2})
        self.assertEqual(b.id, {'a': 1, 'b': 2})
        b = Base([1, 2])
        self.assertEqual(b.id, [1, 2])
        b = Base(True)
        self.assertEqual(b.id, True)
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))

    def test_03(self):
        """Check behavior after args."""
        b = Base(795)
        self.assertEqual(b.id, 795)
        b = Base(612)
        self.assertEqual(b.id, 612)
        b = Base(None)
        self.assertEqual(b.id, 7)

    def test_04(self):
        """Check attribute "id" is public."""
        b = Base()
        b.id = 58
        self.assertEqual(b.id, 58)

    def test_05(self):
        """Check exception raises."""
        with self.assertRaises(AttributeError):
            Base().__nb_instances
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase02(unittest.TestCase):
    """Check "def to_json_string(list_dictionaries)" method."""
    def test_01(self):
        """Check type of return of method."""
        r = Rectangle(1, 1)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        r = Rectangle(1, 1, 1)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        r = Rectangle(1, 1, 1, 1)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        r = Rectangle(1, 7, 2, 86, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        s = Square(1)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
        s = Square(1, 1)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
        s = Square(1, 1, 1)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_02(self):
        """Check if return list is as expected."""
        r = Rectangle(1, 1)
        good_out = '[{"x": 0, "y": 0, "id": 16, "height": 1, "width": 1}]'
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        r = Rectangle(1, 1, 1)
        good_out = '[{"x": 1, "y": 0, "id": 17, "height": 1, "width": 1}]'
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        r = Rectangle(1, 1, 1, 1)
        good_out = '[{"x": 1, "y": 1, "id": 18, "height": 1, "width": 1}]'
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        r = Rectangle(1, 7, 2, 86, 6)
        good_out = '[{"x": 2, "y": 86, "id": 6, "height": 1, "width": 7}]'
        json_dictionary = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        s = Square(1)
        good_out = '[{"x": 0, "y": 0, "id": 19, "size": 1}]'
        json_dictionary = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        s = Square(1, 1)
        good_out = '[{"x": 1, "y": 0, "id": 20, "size": 1}]'
        json_dictionary = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        s = Square(1, 1, 1)
        good_out = '[{"x": 1, "y": 1, "id": 21, "size": 1}]'
        json_dictionary = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))
        s = Square(1, 7, 2, 86)
        good_out = '[{"x": 7, "y": 2, "id": 86, "size": 1}]'
        json_dictionary = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(sorted(good_out), sorted(json_dictionary))

    def test_03(self):
        """Check if return list is as expected when more
        than one instance."""
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_04(self):
        """Check if return list is as expected when argument is empty."""
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))

    def test_05(self):
        """Check exception raises."""
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase03(unittest.TestCase):
    """Check "def save_to_file(cls, list_objs)" method."""
    def test_01(self):
        """Check if list saved is OK."""
        r = Rectangle(1, 1)
        good_out = '[{"x": 0, "y": 0, "id": 22, "height": 1, "width": 1}]'
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        r = Rectangle(1, 1, 1)
        good_out = '[{"x": 1, "y": 0, "id": 23, "height": 1, "width": 1}]'
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        r = Rectangle(1, 1, 1, 1)
        good_out = '[{"x": 1, "y": 1, "id": 24, "height": 1, "width": 1}]'
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        r = Rectangle(10, 7, 2, 8, 5)
        good_out = '[{"x": 2, "y": 8, "id": 5, "height": 10, "width": 7}]'
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        s = Square(1)
        good_out = '[{"x": 0, "y": 0, "id": 25, "size": 1}]'
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        s = Square(1, 1)
        good_out = '[{"x": 1, "y": 0, "id": 26, "size": 1}]'
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        s = Square(1, 1, 1)
        good_out = '[{"x": 1, "y": 1, "id": 27, "size": 1}]'
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))
        s = Square(1, 1, 1, 98)
        good_out = '[{"x": 1, "y": 1, "id": 98, "size": 1}]'
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(sorted(good_out) == sorted(f.read()))

    def test_02(self):
        """Check if list saved is OK when
        more than one instance."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_03(self):
        """Check if list saved is OK when
        no argument."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        

    def test_04(self):
        """Checks exception raises."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass


class TestBase04(unittest.TestCase):
    """Check "def from_json_string(json_string)" method."""
    def test_01(self):
        """Checks if type is as expected."""
        list_input = [{"id": 4, "width": 7, "height": 48}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))
        list_input = [{"id": 4, "size": 1}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_02(self):
        """Checks if return is as expected."""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        list_input = [{"id": 89, "size": 4, "x": 7}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_03(self):
        """Checks if return is as expected,
        when more than one instances."""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_04(self):
        """Check if list saved is OK when
        no argument."""
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))

    def test_05(self):
        """Checks exception raises."""
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase05(unittest.TestCase):
    """Check "def create(cls, **dictionary)" method."""
    def test_01(self):
        """Checks if return is as expected."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


class TestBase06(unittest.TestCase):
    """Check "def load_from_file(cls)" method."""
    def test_01(self):
        """Checks if return is as expected."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_02(self):
        """Checks if return is as expected, when saving
        and then loading files"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_03(self):
        """Checks if return is as expected, when saving
        and then loading files"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_04(self):
        """Check if list loaded is OK when
        no argument."""
        output = Rectangle.load_from_file()
        self.assertEqual([], output)
        output = Square.load_from_file()
        self.assertEqual([], output)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass


if __name__ == '__main__':
    unittest.main()
