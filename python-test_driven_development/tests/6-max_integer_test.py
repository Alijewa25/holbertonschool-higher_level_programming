#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """max_integer funksiyası üçün test keysləri"""

    def test_ordered_list(self):
        """Sıralanmış müsbət ədədlər siyahısını test edir."""
        self.assertEqual(max_integer(), 4)

    def test_unordered_list(self):
        """Sıralanmamış müsbət ədədlər siyahısını test edir."""
        self.assertEqual(max_integer(), 4)

    def test_max_at_beginning(self):
        """Maksimum ədədin siyahının ilk elementi olduğu halı test edir."""
        self.assertEqual(max_integer(), 4)

    def test_empty_list(self):
        """Boş siyahı verildikdə funksiyanın None qaytardığını test edir."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Siyahıda yalnız bir element olduqda işləməsini test edir."""
        self.assertEqual(max_integer(), 7)

    def test_one_negative(self):
        """Siyahıda bir mənfi ədəd olduqda test edir."""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negatives(self):
        """Siyahı yalnız mənfi ədədlərdən ibarət olduqda test edir."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_identical_elements(self):
        """Siyahıdakı bütün elementlər eyni olduqda test edir."""
        self.assertEqual(max_integer(), 5)


if __name__ == '__main__':
    unittest.main()
