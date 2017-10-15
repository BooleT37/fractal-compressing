import numpy as np
from scipy.misc import imresize


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
    return imresize(matrix, size=new_shape)