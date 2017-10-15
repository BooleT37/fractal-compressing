import math

from models.Block import Block


def fill_row_with_intervals(row_length, interval_max_length):
    """
    :param row_length:
    :param interval_max_length:
    :return:
    """
    if row_length == 0:
        return []
    intervals_fit = int(math.ceil(row_length / interval_max_length))
    interval_fract_length = row_length / intervals_fit

    cumulative_length = 0.
    cumulative_length_int = 0
    intervals = []
    for i in range(intervals_fit):
        cumulative_length += interval_fract_length
        interval_length = round(cumulative_length) - cumulative_length_int
        intervals.append(interval_length)
        cumulative_length_int += interval_length
    return intervals

def generate_blocks_gtid(width, height, domain_max_width):
    domains = []
    domain_widths = fill_row_with_intervals(width, domain_max_width)
    domain_heights = fill_row_with_intervals(height, domain_max_width)

    coords_y = 0
    for current_height in domain_heights:
        coords_x = 0
        for current_width in domain_widths:
            domains.append(Block(current_width, current_height, (coords_x, coords_y)))
            coords_x += current_width
        coords_y += current_height
    return domains
