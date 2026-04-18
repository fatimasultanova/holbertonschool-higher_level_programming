#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_repeated_elements(self):
        """Test a list with repeated elements."""
        repeated = [5, 5, 5, 5]
        self.assertEqual(max_integer(repeated), 5)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_max_at_beginning(self):
        """Test a list where the max is at the beginning."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        negatives = [-1, -5, -2, -10]
        self.assertEqual(max_integer(negatives), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        mixed = [-1, 5, -10, 2]
        self.assertEqual(max_integer(mixed), 5)

if __name__ == "__main__":
    unittest.main()
