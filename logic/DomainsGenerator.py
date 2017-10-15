from logic.GeneratorUtils import fill_row_with_intervals
from models.Block import Block


def generate_domains(width, height, domain_max_width, depth=3):
    domains = []
    while depth > 0:
        domains += generate_one_layer_of_domains(width, height, domain_max_width)
        domain_max_width = domain_max_width * 2
        depth = depth - 1
    return domains


def generate_one_layer_of_domains(width, height, domain_max_width):
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


