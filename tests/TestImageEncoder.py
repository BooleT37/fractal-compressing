import unittest

import numpy as np
from PIL import Image as PilImage

from logic.Constants import MAX_PSNR
from logic.ImageEncoder import encode


class TestImageEncoder(unittest.TestCase):
    def test_encode_simple(self):
        image = PilImage.open("./images/basn0g01.png")
        matrix = np.array(image.getdata(), dtype=int).reshape(image.size[1], image.size[0])
        data = encode(matrix)
        self.assertGreater(len(data), 0)
        self.assertIsNotNone(data[0].transform_num)
        self.assertLess(data[0].psnr, MAX_PSNR + 1)
