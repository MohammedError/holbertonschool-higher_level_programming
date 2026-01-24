#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max integer at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test with a list of ints and floats"""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("Brennan"), 'r')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["Brennan", "Louis", "Hello"]), "Louis")

    def test_none(self):
        """Test with None"""
        with self.assertRaises(TypeError):
            max_integer(None)
