import numpy as np


def rotate_image_90_degrees(matrix):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :return matrix: numpy.array (shape=(n,m), dtype="int8")
    """
    raise NotImplementedError()


def reflect_image_horizontally(matrix):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :return matrix: numpy.array (shape=(n,m), dtype="int8")
    """
    raise NotImplementedError()


def reflect_image_vertically(matrix):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :return matrix: numpy.array (shape=(n,m), dtype="int8")
    """
    raise NotImplementedError()


def resize_image(matrix, new_shape):
    """
    :param matrix: numpy.array (shape=(n,m), dtype="int8")
    :param new_shape: tuple
    :return matrix: numpy.array (shape=new_shape, dtype="int8")
    """
    raise NotImplementedError()