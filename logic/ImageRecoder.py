import json

import numpy as np
import png

from logic.ImageDecoder import decode
from logic.ImageEncoder import encode_file


def recode_image(target_image_path, blank_image_path, recoded_image_path, encode_data_path):
    encoded = encode_file(target_image_path)
    blank_image = png.Reader(blank_image_path).read()
    blank_image_matrix = np.array(list(blank_image[2])).reshape(blank_image[1], blank_image[0])
    if blank_image_matrix.shape != (encoded.height, encoded.width):
        raise Exception(f'The shape of blank image {blank_image_matrix.shape} is not equal to the shape of '
                        f'target image ({encoded.height}, {encoded.width})')
    matrix = decode(encoded, blank_image_matrix)

    img = png.fromarray(matrix, 'L', blank_image[3])
    img.save(recoded_image_path)
    fp = open(encode_data_path, 'w')
    json.dump(encoded, fp, indent=1, default=lambda o: o.__dict__)
    fp.close()
