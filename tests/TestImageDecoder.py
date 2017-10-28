import unittest

import numpy as np
from PIL import Image as PilImage

from logic.ImageDecoder import decode
from models.EncodedImage import EncodedImage
from models.TransformationInfo import TransformationInfo


class TestImageDecoder(unittest.TestCase):
    def test_decode_simple(self):
        test_data = EncodedImage(32, 32, [
            TransformationInfo(3, 2, 1.5377041029302496),
            TransformationInfo(3, 2, 1.7355185115872591),
            TransformationInfo(3, 0, 1.6413061015493893),
            TransformationInfo(1, 2, 0.6455438457978917),
            TransformationInfo(1, 3, 1.5127358896679735),
            TransformationInfo(1, 0, 1.3761708857621358),
            TransformationInfo(1, 2, 0.6455438457978917),
            TransformationInfo(0, 0, 1.5358755477640922),
            TransformationInfo(3, 0, 1.6413061015493893),
            TransformationInfo(1, 2, 0.6455438457978917),
            TransformationInfo(1, 0, 1.6134212232762306),
            TransformationInfo(1, 3, 1.76656723287262),
            TransformationInfo(1, 2, 0.6455438457978917),
            TransformationInfo(0, 0, 1.5358755477640922),
            TransformationInfo(0, 1, 1.662785504805508),
            TransformationInfo(0, 5, 1.6878335872187524)
        ])
        initial_image = PilImage.open("./images/basn0g01.png")
        initial_image_matrix = np.array(initial_image.getdata(), dtype=int).reshape(initial_image.size[1], initial_image.size[0])
        matrix = decode(test_data, initial_image_matrix)
        self.assertGreater(matrix.shape[0], 0)
        self.assertGreater(matrix.shape[1], 0)