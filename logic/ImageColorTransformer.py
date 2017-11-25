import math
import numpy as np
import png


def make_grayscale(image):
    planes = image[3]['planes']
    array = np.array(list(image[2]), dtype='int16').reshape(image[1] * image[0] * planes)
    grayscaled = make_array_grayscale(array, image[0], image[1], image[3]['alpha'])
    image[3]['greyscale'] = True
    image[3]['alpha'] = False
    image[3]['planes'] = 1
    return png.fromarray(grayscaled, 'L', image[3])


def make_array_grayscale(array, width, height, planes):
    res = np.empty(shape=(height, width), dtype='int16')

    for i in range(height):
        for j in range(width):
            index = i * j * planes
            res[i, j] = round(array[index] * 0.3 + array[index + 1] * 0.59 + array[index + 2] * 0.11)
    return res
