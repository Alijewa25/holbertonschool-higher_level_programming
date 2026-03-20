#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer(list=[])"""

    def test_ordered_list(self):
        """Test with an ordered list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of positive integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with a list where the max is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_one_negative(self):
        """Test with a list containing one negative number."""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negatives(self):
        """Test with a list containing only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_identical_elements(self):
        """Test with a list containing identical elements."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()
