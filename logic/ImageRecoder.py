from PIL import Image

from logic.ImageDecoder import decode_with_file
from logic.ImageEncoder import encode_file


def recode_image(target_image_path, blank_image_path, recoded_image_path):
    matrix = decode_with_file(encode_file(target_image_path), blank_image_path)
    img = Image.fromarray(matrix, 'L')
    img.save(recoded_image_path)