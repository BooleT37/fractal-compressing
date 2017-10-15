import unittest

from logic.DomainsGenerator import generate_domains
from models.Block import Block


class TestGenerateDomains(unittest.TestCase):
    def test_generate_one_domain(self):
        self.assertEqual([Block(1, 1, (0, 0))], generate_domains(1, 1, 1, 1))

    def test_generate_one_layer_of_perfectly_fit_domains(self):
        actual = generate_domains(10, 15, 5, 1)
        expected = [
            Block(5, 5, (0, 0)),
            Block(5, 5, (5, 0)),
            Block(5, 5, (0, 5)),
            Block(5, 5, (5, 5)),
            Block(5, 5, (0, 10)),
            Block(5, 5, (5, 10))
        ]
        self.assertEqual(expected, actual)

    def test_generate_one_layer_of_imperfectly_fit_domains(self):
        actual = generate_domains(16, 27, 7, 1)
        expected = [
            Block(5, 7, (0, 0)),
            Block(6, 7, (5, 0)),
            Block(5, 7, (11, 0)),
            Block(5, 7, (0, 7)),
            Block(6, 7, (5, 7)),
            Block(5, 7, (11, 7)),
            Block(5, 6, (0, 14)),
            Block(6, 6, (5, 14)),
            Block(5, 6, (11, 14)),
            Block(5, 7, (0, 20)),
            Block(6, 7, (5, 20)),
            Block(5, 7, (11, 20))
        ]
        self.assertEqual(expected, actual)

    def test_generate_three_layers_of_imperfectly_fit_domains(self):
        actual = generate_domains(17, 11, 6, 3)
        expected = [
            Block(6, 6, (0, 0)),
            Block(5, 6, (6, 0)),
            Block(6, 6, (11, 0)),
            Block(6, 5, (0, 6)),
            Block(5, 5, (6, 6)),
            Block(6, 5, (11, 6)),

            Block(8, 11, (0, 0)),
            Block(9, 11, (8, 0)),

            Block(17, 11, (0, 0))
        ]
        self.assertEqual(expected, actual)
