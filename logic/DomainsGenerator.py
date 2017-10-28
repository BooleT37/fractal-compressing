from logic.GeneratorUtils import generate_blocks_grid


def generate_domains(width, height, domain_max_width, depth=3):
    """
    :param width: number
    :param height: number
    :param domain_max_width: number
    :param depth: number
    :return: models.Block
    """
    domains = []
    while depth > 0:
        domains += generate_blocks_grid(width, height, domain_max_width)
        domain_max_width *= 2
        depth -= 1
    return domains
