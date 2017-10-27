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