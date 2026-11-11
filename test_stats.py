#!/usr/bin/env python3
"""Tests for stats.py. Run with `python3 test_stats.py`."""

import unittest

from stats import main, mean, median, spread, summarize


class MeanTests(unittest.TestCase):
    def test_single(self):
        self.assertEqual(mean([7]), 7)

    def test_several(self):
        self.assertAlmostEqual(mean([1, 2, 3, 4]), 2.5)

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            mean([])


class MedianTests(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_even_count_averages_the_two_middle_values(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_even_count_unsorted_input(self):
        self.assertEqual(median([10, 2, 8, 4]), 6)

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            median([])


class SpreadTests(unittest.TestCase):
    def test_range(self):
        self.assertEqual(spread([4, 1, 9]), 8)

    def test_single_value(self):
        self.assertEqual(spread([5]), 0)


class SummaryTests(unittest.TestCase):
    def test_format(self):
        self.assertEqual(
            summarize([1, 2, 3, 4]),
            "count=4 mean=2.50 median=2.50 spread=3.00",
        )


class CommandLineTests(unittest.TestCase):
    def test_missing_arguments_is_usage_error(self):
        self.assertEqual(main([]), 2)

    def test_bad_argument_is_usage_error(self):
        self.assertEqual(main(["3", "oops"]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
