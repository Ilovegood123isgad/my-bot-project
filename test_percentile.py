#!/usr/bin/env python3
"""Tests for percentile(). Run with `python3 test_percentile.py`."""

import unittest

from stats import percentile


class PercentileTests(unittest.TestCase):
    def test_zero_returns_the_smallest_value(self):
        self.assertEqual(percentile([1, 2, 3, 4], 0), 1.0)

    def test_quarter(self):
        self.assertEqual(percentile([1, 2, 3, 4], 25), 1.75)

    def test_half(self):
        self.assertEqual(percentile([1, 2, 3, 4], 50), 2.5)

    def test_hundred_returns_the_largest_value(self):
        self.assertEqual(percentile([1, 2, 3, 4], 100), 4.0)

    def test_ninety(self):
        self.assertEqual(percentile([1, 2, 3, 4, 5], 90), 4.6)

    def test_single_value(self):
        self.assertEqual(percentile([5], 37), 5.0)

    def test_unsorted_input(self):
        self.assertEqual(percentile([4, 1, 3, 2], 25), 1.75)

    def test_fractional_percentile(self):
        self.assertAlmostEqual(percentile([1, 2, 3, 4], 12.5), 1.375)

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            percentile([], 50)

    def test_rejects_negative_percentile(self):
        with self.assertRaises(ValueError):
            percentile([1, 2, 3, 4], -0.1)

    def test_rejects_percentile_above_hundred(self):
        with self.assertRaises(ValueError):
            percentile([1, 2, 3, 4], 100.1)

    def test_error_messages_name_the_function(self):
        with self.assertRaisesRegex(ValueError, r"percentile\(\)"):
            percentile([], 50)
        with self.assertRaisesRegex(ValueError, r"percentile\(\)"):
            percentile([1], 101)


if __name__ == "__main__":
    unittest.main(verbosity=2)
