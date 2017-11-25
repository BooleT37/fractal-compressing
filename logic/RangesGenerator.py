from logic.GeneratorUtils import generate_blocks_grid


def generate_ranges(width, height, range_max_width):
    """
    :param width: int
    :param height: int
    :param range_max_width: int
    :return: list of blocks (Block)
    """
    ranges = generate_blocks_grid(width, height, range_max_width)
    return ranges
