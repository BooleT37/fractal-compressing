import numpy as np

MAX_VALUE = 255


def adjust_for_one_pixel(x, brightness, contrast):
    val = x * contrast + brightness
    if val > MAX_VALUE:
        return MAX_VALUE
    if val < 0:
        return 0
    return val


def adjust_brightness_and_contrast(matrix, brightness, contrast):
    f = np.vectorize(adjust_for_one_pixel)
    return f(matrix, brightness, contrast)


def count_optimal_brightness_and_contrast(initial_matrix, target_matrix):
    n = initial_matrix.shape[0] * initial_matrix.shape[1]
    sum_x = np.sum(initial_matrix)
    sum_y = np.sum(target_matrix)
    sum_x2 = np.sum(initial_matrix * initial_matrix)
    sum_xy = np.sum(initial_matrix * target_matrix)

    contrast = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    brightness = (sum_y - contrast * sum_x) / n
    return brightness, contrast


def adjust_reverse_for_one_pixel(x, brightness, contrast):
    val = (x - brightness) / contrast
    if val > MAX_VALUE:
        return MAX_VALUE
    if val < 0:
        return 0
    return val


def adjust_reverse_brightness_and_contrast(matrix, brightness, contrast):
    f = np.vectorize(adjust_reverse_for_one_pixel)
    return f(matrix, brightness, contrast)