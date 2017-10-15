import unittest
import numpy as np

from logic.ImageTransformer import rotate_image_90_degrees, \
    reflect_image_horizontally, \
    reflect_image_vertically, \
    resize_image


class TestImageTransformer(unittest.TestCase):

    def setUp(self):
        self.matrix = np.array([[1,2], [3,4]], dtype="int8")

    def test_rotate_image_90_degrees(self):
        rotated_matrix = np.array([[2,4], [1,3]], dtype="int8")
        np.testing.assert_equal(rotated_matrix, rotate_image_90_degrees(self.matrix))

    def test_reflect_image_horizontally(self):
        flipped_matrix = np.array([[2,1], [4,3]], dtype="int8")
        np.testing.assert_equal(flipped_matrix, reflect_image_horizontally(self.matrix))

    def test_reflect_image_vertically(self):
        flipped_matrix = np.array([[3,4], [1,2]], dtype="int8")
        np.testing.assert_equal(flipped_matrix, reflect_image_vertically(self.matrix))

    def test_new_shape_of_resized_image(self):
        new_shape = (3, 5)
        resized_image = resize_image(self.matrix, new_shape=new_shape)
        self.assertEqual(new_shape, resized_image.shape)
