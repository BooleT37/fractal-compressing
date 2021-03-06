from logic.BlockUtils import get_range_width, matrix_from_block, fill_submatrix
from logic.ColorsTransformer import adjust_brightness_and_contrast
from logic.Constants import DOMAINS_DEPTH, DOMAIN_TO_RANGE_SIZE_RATIO
from logic.DomainsGenerator import generate_domains
from logic.ImageTransformer import resize_image, apply_affine_transform_by_num
from logic.RangesGenerator import generate_ranges


def decode(data, initial_image):
    """
    :param data: models.TransformationInfo.TransformationInfo
    :param initial_image: numpy.array(shape=(m,n))
    :return np.ndarray
    """
    width = data.width
    height = data.height

    range_width = get_range_width(width, height)
    domain_width = range_width * DOMAIN_TO_RANGE_SIZE_RATIO

    ranges = generate_ranges(width, height, range_width)
    domains = generate_domains(width, height, domain_width, DOMAINS_DEPTH)

    index = 0
    print("\nFilling ranges:")
    for index, range_block in enumerate(ranges):
        print(f'{index + 1}...')
        trns_info = data.transformations[index]
        domain = domains[trns_info.domain_index]
        domain_matrix = matrix_from_block(initial_image, domain)
        transformed_domain_matrix = apply_affine_transform_by_num(domain_matrix, trns_info.transform_num)
        resized_domain_matrix = resize_image(transformed_domain_matrix, (range_block.height, range_block.width))
        adjusted_domain_matrix = adjust_brightness_and_contrast(
            resized_domain_matrix,
            trns_info.brightness,
            trns_info.contrast
        )
        fill_submatrix(initial_image, range_block, adjusted_domain_matrix)
        index += 1
    return initial_image
