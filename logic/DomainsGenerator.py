from logic.GeneratorUtils import generate_blocks_gtid


def generate_domains(width, height, domain_max_width, depth=3):
    domains = []
    while depth > 0:
        domains += generate_blocks_gtid(width, height, domain_max_width)
        domain_max_width = domain_max_width * 2
        depth -= 1
    return domains
