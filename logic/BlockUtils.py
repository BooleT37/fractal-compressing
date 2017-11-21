from logic.Constants import MIN_BLOCK_WIDTH, RANGES_PER_SIDE


def matrix_from_block(matrix, block):
    """
    :param matrix: np.array
    :param block: Block
    :return: np.array
    """
    x_start = block.coords[1]
    x_end = x_start + block.width
    y_start = block.coords[0]
    y_end = y_start + block.height
    return matrix[x_start:x_end, y_start:y_end]


def fill_submatrix(matrix, block, submatrix):
    """
    :param matrix: np.array
    :param block: models.Block
    :param submatrix: np.array
    :return: 
    """
    x_start = block.coords[1]
    x_end = x_start + block.width
    y_start = block.coords[0]
    y_end = y_start + block.height
    matrix[x_start:x_end, y_start:y_end] = submatrix


def get_range_width(image_width, image_height):
    return max(MIN_BLOCK_WIDTH, min(int(image_width / RANGES_PER_SIDE), int(image_height / RANGES_PER_SIDE)))
