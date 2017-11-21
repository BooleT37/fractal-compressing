import unittest

import numpy as np

from logic.ColorsTransformer import adjust_brightness_and_contrast, MAX_VALUE, count_optimal_brightness_and_contrast


class TestColorTransformer(unittest.TestCase):
    def test_adjust_brightness(self):
        initial = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype='int16')
        expected = np.array([[10, 10, 10], [10, 10, 10], [10, 10, 10]], dtype='int16')
        self.assertTrue(np.array_equal(expected, adjust_brightness_and_contrast(initial, 10, 1)))

    def test_adjust_contrast(self):
        initial = np.array([[100, 100, 100], [100, 100, 100], [100, 100, 100]], dtype='int16')
        expected = np.array([[150, 150, 150], [150, 150, 150], [150, 150, 150]], dtype='int16')
        self.assertTrue(np.array_equal(expected, adjust_brightness_and_contrast(initial, 0, 1.5)))

    def test_adjust_brightness_and_contrast(self):
        initial = np.array([[100, 100, 100], [100, 100, 100], [100, 100, 100]], dtype='int16')
        expected = np.array([[180, 180, 180], [180, 180, 180], [180, 180, 180]], dtype='int16')
        self.assertTrue(np.array_equal(expected, adjust_brightness_and_contrast(initial, -20, 2)))

    def test_adjust_brightness_with_overflow(self):
        initial = np.array([[200, 200, 200], [200, 200, 200], [200, 200, 200]], dtype='int16')
        expected = np.array(
            [[MAX_VALUE, MAX_VALUE, MAX_VALUE], [MAX_VALUE, MAX_VALUE, MAX_VALUE], [MAX_VALUE, MAX_VALUE, MAX_VALUE]],
            dtype='int16')
        self.assertTrue(np.array_equal(expected, adjust_brightness_and_contrast(initial, 100, 1)))

    def test_adjust_brightness_with_negative_overflow(self):
        initial = np.array([[50, 50, 50], [50, 50, 50], [50, 50, 50]], dtype='int16')
        expected = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype='int16')
        self.assertTrue(np.array_equal(expected, adjust_brightness_and_contrast(initial, -150, 1)))

    def test_adjust_contrast_with_overflow(self):
        initial = np.array([[200, 200, 200], [200, 200, 200], [200, 200, 200]], dtype='int16')
        expected = np.array(
            [[MAX_VALUE, MAX_VALUE, MAX_VALUE], [MAX_VALUE, MAX_VALUE, MAX_VALUE], [MAX_VALUE, MAX_VALUE, MAX_VALUE]],
            dtype='int16')
        self.assertTrue(np.array_equal(expected, adjust_brightness_and_contrast(initial, 0, 1.5)))

    def test_count_optimal_brightness_and_contrast_for_equal_matrices(self):
        initial = np.array([[10, 0], [5, 15]])
        target = np.array([[10, 0], [5, 15]])
        self.assertEqual(count_optimal_brightness_and_contrast(initial, target), (0, 1))

    def test_count_optimal_brightness_for_simple_matrices(self):
        initial = np.array([[10, 0], [5, 15]])
        target = np.array([[15, 5], [10, 20]])
        self.assertEqual(count_optimal_brightness_and_contrast(initial, target), (5, 1))

    def test_count_optimal_contrast_for_simple_matrices(self):
        initial = np.array([[10, 0], [5, 15]])
        target = np.array([[20, 0], [10, 30]])
        self.assertEqual(count_optimal_brightness_and_contrast(initial, target), (0, 2))

    def test_count_optimal_brightness_and_contrast_for_complex_matrices(self):
        initial = np.array([[10, 0], [5, 15]])
        target = np.array([[15, 5], [10, 15]])

        actual = count_optimal_brightness_and_contrast(initial, target)
        self.assertAlmostEqual(actual[0], 6, 2)
        self.assertAlmostEqual(actual[1], 0.7, 2)
