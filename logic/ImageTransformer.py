import numpy as np
from scipy.misc import imresize

from models.AffineTransformations import AffineTransformations


def rotate_image_90_degrees(matrix):
    """
    Rotate counterclockwise
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :return matrix: numpy.array (shape=(n,m), dtype="int8")
    """
    return np.rot90(matrix)


def reflect_image_horizontally(matrix):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :return matrix: numpy.array (shape=(n,m), dtype="int8")
    """
    return np.fliplr(matrix)


def reflect_image_vertically(matrix):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :return matrix: numpy.array (shape=(n,m), dtype="int8")
    """
    return np.flipud(matrix)


def resize_image(matrix, new_shape):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :param new_shape: tuple
    :return matrix: numpy.array (shape=new_shape, dtype="int8")
    """
    if matrix.shape == new_shape:
        return np.copy(matrix)
    return imresize(matrix, size=new_shape)


def apply_affine_transform_by_num(matrix, transform_num):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :param transform_num: models.AffineTransformations.AffineTransformations
    :return:
    """
    if transform_num == AffineTransformations.NONE:
        return matrix
    if transform_num == AffineTransformations.ROTATE_90:
        return rotate_image_90_degrees(matrix)
    if transform_num == AffineTransformations.ROTATE_180:
        return rotate_image_90_degrees(rotate_image_90_degrees(matrix))
    if transform_num == AffineTransformations.ROTATE_270:
        return rotate_image_90_degrees(rotate_image_90_degrees(rotate_image_90_degrees(matrix)))
    if transform_num == AffineTransformations.REFLECT_HORIZONTALLY:
        return reflect_image_horizontally(matrix)
    if transform_num == AffineTransformations.ROTATE_90_AND_REFLECT_HORIZONTALLY:
        return reflect_image_horizontally(rotate_image_90_degrees(matrix))
    if transform_num == AffineTransformations.ROTATE_180_AND_REFLECT_HORIZONTALLY:
        return reflect_image_horizontally(rotate_image_90_degrees(rotate_image_90_degrees(matrix)))
    if transform_num == AffineTransformations.ROTATE_270_AND_REFLECT_HORIZONTALLY:
        return reflect_image_horizontally(rotate_image_90_degrees(rotate_image_90_degrees(rotate_image_90_degrees(matrix))))
    if transform_num == AffineTransformations.REFLECT_VERTICALLY:
        return reflect_image_vertically(matrix)
    if transform_num == AffineTransformations.ROTATE_90_AND_REFLECT_VERTICALLY:
        return reflect_image_vertically(rotate_image_90_degrees(matrix))
    if transform_num == AffineTransformations.ROTATE_180_AND_REFLECT_VERTICALLY:
        return reflect_image_vertically(rotate_image_90_degrees(rotate_image_90_degrees(matrix)))
    if transform_num == AffineTransformations.ROTATE_270_AND_REFLECT_VERTICALLY:
        return reflect_image_vertically(
            rotate_image_90_degrees(rotate_image_90_degrees(rotate_image_90_degrees(matrix))))
    if transform_num == AffineTransformations.REFLECT_HORIZONTALLY_AND_VERTICALLY:
        return reflect_image_vertically(reflect_image_horizontally(matrix))
    if transform_num == AffineTransformations.ROTATE_90_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY:
        return reflect_image_vertically(reflect_image_horizontally(rotate_image_90_degrees(matrix)))
    if transform_num == AffineTransformations.ROTATE_180_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY:
        return reflect_image_vertically(reflect_image_horizontally(rotate_image_90_degrees(rotate_image_90_degrees(matrix))))
    if transform_num == AffineTransformations.ROTATE_270_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY:
        return reflect_image_vertically(reflect_image_horizontally(rotate_image_90_degrees(rotate_image_90_degrees(rotate_image_90_degrees(matrix)))))


INVERSE_AFFINE_TRANSFORMATIONS = {
    AffineTransformations.NONE: AffineTransformations.NONE,
    AffineTransformations.ROTATE_90: AffineTransformations.ROTATE_270,
    AffineTransformations.ROTATE_180: AffineTransformations.ROTATE_180,
    AffineTransformations.ROTATE_270: AffineTransformations.ROTATE_90,
    AffineTransformations.REFLECT_HORIZONTALLY: AffineTransformations.REFLECT_HORIZONTALLY,
    AffineTransformations.ROTATE_90_AND_REFLECT_HORIZONTALLY: AffineTransformations.ROTATE_270_AND_REFLECT_HORIZONTALLY,
    AffineTransformations.ROTATE_180_AND_REFLECT_HORIZONTALLY: AffineTransformations.ROTATE_180_AND_REFLECT_HORIZONTALLY,
    AffineTransformations.ROTATE_270_AND_REFLECT_HORIZONTALLY: AffineTransformations.ROTATE_90_AND_REFLECT_HORIZONTALLY,
    AffineTransformations.REFLECT_VERTICALLY: AffineTransformations.REFLECT_VERTICALLY,
    AffineTransformations.ROTATE_90_AND_REFLECT_VERTICALLY: AffineTransformations.ROTATE_270_AND_REFLECT_VERTICALLY,
    AffineTransformations.ROTATE_180_AND_REFLECT_VERTICALLY: AffineTransformations.ROTATE_180_AND_REFLECT_VERTICALLY,
    AffineTransformations.ROTATE_270_AND_REFLECT_VERTICALLY: AffineTransformations.ROTATE_90_AND_REFLECT_VERTICALLY,
    AffineTransformations.REFLECT_HORIZONTALLY_AND_VERTICALLY: AffineTransformations.REFLECT_HORIZONTALLY_AND_VERTICALLY,
    AffineTransformations.ROTATE_90_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY: AffineTransformations.ROTATE_270_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY,
    AffineTransformations.ROTATE_180_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY: AffineTransformations.ROTATE_180_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY,
    AffineTransformations.ROTATE_270_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY: AffineTransformations.ROTATE_90_AND_REFLECT_HORIZONTALLY_AND_VERTICALLY
}


def apply_inverse_affine_transform_by_num(matrix, transform_num):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :param transform_num: models.AffineTransformations.AffineTransformations
    :return:
    """
    return apply_affine_transform_by_num(matrix, INVERSE_AFFINE_TRANSFORMATIONS.get(AffineTransformations(transform_num)))
