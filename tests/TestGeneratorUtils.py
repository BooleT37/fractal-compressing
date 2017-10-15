import unittest

from logic.GeneratorUtils import fill_row_with_intervals


class TestFillRowWithIntervals(unittest.TestCase):
    def test_fill_empty_row_with_intervals(self):
        self.assertEqual([], fill_row_with_intervals(0, 1))

    def test_fill_row_with_one_interval(self):
        self.assertEqual([1], fill_row_with_intervals(1, 1))

    def test_fill_row_with_two_intervals(self):
        self.assertEqual([5, 5], fill_row_with_intervals(10, 5))

    def test_fill_row_with_three_intervals(self):
        self.assertEqual([7, 6, 7], fill_row_with_intervals(20, 7))

    def test_fill_row_with_one_interval_of_large_size(self):
        self.assertEqual([10], fill_row_with_intervals(10, 13))
