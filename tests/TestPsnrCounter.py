import unittest

from logic.PsnrCounter import count_psnr


class TestPsnrCounter(unittest.TestCase):
    def test_count_psnr_of_equal_pixels(self):
        pixels = [0, 1, 2]
        with self.assertRaises(Exception) as context:
            count_psnr(pixels, pixels)

        self.assertEqual("Pixels are equal, PSNR is undefined", str(context.exception))

    def test_count_psnr_of_different_pixels(self):
        pixels1 = [0, 1, 2]
        pixels2 = [0, 2, 3]

        self.assertAlmostEqual(49.89, count_psnr(pixels1, pixels2), 2)
