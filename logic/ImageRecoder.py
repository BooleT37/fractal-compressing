import json

import numpy as np
import png

from logic.ImageDecoder import decode
from logic.ImageEncoder import encode_file


def recode_image(target_image_path, blank_image_path, recoded_image_path, encode_data_path):
    encoded = encode_file(target_image_path)
    initial_image = png.Reader(blank_image_path).read()
    initial_image_matrix = np.array(list(initial_image[2])).reshape(initial_image[1], initial_image[0])
    matrix = decode(encoded, initial_image_matrix)

    img = png.fromarray(matrix, 'L', initial_image[3])
    img.save(recoded_image_path)
    fp = open(encode_data_path, 'w')
    json.dump(encoded, fp, indent=1, default=lambda o: o.__dict__)
    fp.close()
