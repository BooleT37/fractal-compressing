import math

from logic.BlockUtils import matrix_from_block
from logic.Constants import MIN_BLOCK_WIDTH, DOMAINS_DEPTH, RANGES_PER_SIDE, PSNR_THRESHOLD, MAX_PSNR
from logic.DomainsGenerator import generate_domains
from logic.ImageTransformer import rotate_image_90_degrees, reflect_image_horizontally, reflect_image_vertically, \
    resize_image
from logic.PsnrCounter import count_psnr
from logic.RangesGenerator import generate_ranges
from models.TransformationInfo import TransformationInfo


def encode(image):
    width = image.shape[1]
    height = image.shape[1]

    range_width = max(MIN_BLOCK_WIDTH, min(int(width / RANGES_PER_SIDE), int(height / RANGES_PER_SIDE)))

    ranges = generate_ranges(width, height, range_width)
    domains = generate_domains(width, height, range_width * 2, DOMAINS_DEPTH)
    return list(map(lambda range_block: find_closest_domain(image, matrix_from_block(image, range_block), domains), ranges))


def apply_transforms(image):
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


def find_closest_domain(image, range_matrix, domains):
    min_psnr = MAX_PSNR
    transformation_info_of_min_psnr = None
    for domain_block in domains:
        domain_block_resized = resize_image(matrix_from_block(image, domain_block), range_matrix.shape)
        transform_num = 0

        for transform in apply_transforms(domain_block_resized):
            length = range_matrix.shape[0] * range_matrix.shape[1]
            psnr = count_psnr(transform.reshape(length), range_matrix.reshape(length))
            if psnr < min_psnr:
                transformation_info = TransformationInfo(transform_num, psnr)
                if psnr <= PSNR_THRESHOLD:
                    return transformation_info
                else:
                    min_psnr = psnr
                    transformation_info_of_min_psnr = transformation_info
            transform_num += 1

    return transformation_info_of_min_psnr
