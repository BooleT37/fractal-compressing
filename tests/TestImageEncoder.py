import unittest

import numpy as np
from PIL import Image as PilImage

from logic.ImageEncoder import encode


class TestImageEncoder(unittest.TestCase):
    def test_encode_simple(self):
        image = PilImage.open("./images/basn0g01.png")
        matrix = np.array(image.getdata(), dtype='int16').reshape(image.size[1], image.size[0])
        data = encode(matrix)
        self.assertGreater(len(data.transformations), 0)
        self.assertIsNotNone(data.transformations[0].transform_num)
        self.assertGreater(data.transformations[0].psnr, 0)
