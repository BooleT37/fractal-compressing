import math

from PIL import Image as PilImage
import numpy as np

from logic.BlockUtils import matrix_from_block, get_range_width
from logic.Constants import DOMAINS_DEPTH, DOMAIN_TO_RANGE_SIZE_RATIO
from logic.DomainsGenerator import generate_domains
from logic.ImageTransformer import rotate_image_90_degrees, reflect_image_horizontally, reflect_image_vertically, \
    resize_image
from logic.PsnrCounter import count_psnr, MseIsZeroException
from logic.RangesGenerator import generate_ranges
from models.EncodedImage import EncodedImage
from models.TransformationInfo import TransformationInfo


def encode_file(path):
    image = PilImage.open(path)
    matrix = np.array(image.getdata(), dtype='int16').reshape(image.size[1], image.size[0])
    image.close()
    encoded = encode(matrix)
    # print(encoded)
    return encoded


def encode(image):
    """
    :param image: np.ndarray
    :return models.EncodedImage.EncodedImage
    """
    width = image.shape[1]
    height = image.shape[1]

    range_width = get_range_width(width, height)
    domain_width = range_width * DOMAIN_TO_RANGE_SIZE_RATIO

    ranges = generate_ranges(width, height, range_width)
    domains = generate_domains(width, height, domain_width, DOMAINS_DEPTH)
    return EncodedImage(
        width,
        height,
        list(map(lambda range_block: find_best_transformation(image, matrix_from_block(image, range_block), domains), ranges))
    )


def apply_transforms(image):
    """
    :param image: np.ndarray
    :return np.ndarray[]
    """
    image_rotated_90 = rotate_image_90_degrees(image)
    image_rotated_180 = rotate_image_90_degrees(image_rotated_90)
    image_rotated_270 = rotate_image_90_degrees(image_rotated_180)

    image_reflected_horizontally = reflect_image_horizontally(image)
    image_rotated_90_and_reflected_horizontally = reflect_image_horizontally(image_rotated_90)
    image_rotated_180_and_reflected_horizontally = reflect_image_horizontally(image_rotated_180)
    image_rotated_270_and_reflected_horizontally = reflect_image_horizontally(image_rotated_270)

    return [
        image,
        image_rotated_90,
        image_rotated_180,
        image_rotated_270,

        image_reflected_horizontally,
        image_rotated_90_and_reflected_horizontally,
        image_rotated_180_and_reflected_horizontally,
        image_rotated_270_and_reflected_horizontally,

        reflect_image_vertically(image),
        reflect_image_vertically(image_rotated_90),
        reflect_image_vertically(image_rotated_180),
        reflect_image_vertically(image_rotated_270),

        reflect_image_vertically(image_reflected_horizontally),
        reflect_image_vertically(image_rotated_90_and_reflected_horizontally),
        reflect_image_vertically(image_rotated_180_and_reflected_horizontally),
        reflect_image_vertically(image_rotated_270_and_reflected_horizontally),
    ]


def find_best_transformation(image, range_matrix, domains):
    """
    :param image: np.ndarray
    :param range_matrix: np.ndarray
    :param domains: models.Block
    :return: models.TransformationInfo.TransformationInfo
    """
    max_psnr = 0
    transformation_info_of_max_psnr = None

    domain_index = 0
    for domain_block in domains:
        domain_block_resized = resize_image(matrix_from_block(image, domain_block), range_matrix.shape)
        transform_num = 0
        for transform in apply_transforms(domain_block_resized):
            length = range_matrix.shape[0] * range_matrix.shape[1]
            try:
                psnr = count_psnr(transform.reshape(length), range_matrix.reshape(length))
            except MseIsZeroException:
                psnr = float("inf")
            if psnr > max_psnr:
                transformation_info = TransformationInfo(domain_index, transform_num, psnr)
                max_psnr = psnr
                transformation_info_of_max_psnr = transformation_info
            transform_num += 1
        domain_index += 1

    return transformation_info_of_max_psnr
