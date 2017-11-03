from PIL import Image as PilImage
import numpy as np

from logic.BlockUtils import get_range_width, matrix_from_block, fill_submatrix
from logic.Constants import DOMAINS_DEPTH
from logic.DomainsGenerator import generate_domains
from logic.ImageTransformer import apply_inverse_affine_transform_by_num, resize_image
from logic.RangesGenerator import generate_ranges


def decode_with_file(data, filename):
    initial_image = PilImage.open(filename)
    initial_image_matrix = np.array(initial_image.getdata(), dtype='int16').reshape(initial_image.size[1],
                                                                                initial_image.size[0])
    initial_image.close()
    return decode(data, initial_image_matrix)


def decode(data, initial_image):
    """
    :param data: models.TransformationInfo.TransformationInfo
    :param initial_image: numpy.array(shape=(m,n))
    :return np.ndarray
    """
    width = data.width
    height = data.height

    range_width = get_range_width(width, height)
    domain_width = range_width * 2

    ranges = generate_ranges(width, height, range_width)
    domains = generate_domains(width, height, domain_width, DOMAINS_DEPTH)

    index = 0
    for range_block in ranges:
        trns_info = data.transformations[index]
        domain = domains[trns_info.domain_index]
        domain_matrix = matrix_from_block(initial_image, domain)
        transformed_domain_matrix = apply_inverse_affine_transform_by_num(domain_matrix, trns_info.transform_num)
        resized_domain_matrix = resize_image(transformed_domain_matrix, (range_block.height, range_block.width))
        fill_submatrix(initial_image, range_block, resized_domain_matrix)
        index += 1
    return initial_image