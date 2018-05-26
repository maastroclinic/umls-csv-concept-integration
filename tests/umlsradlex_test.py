import unittest
from umlsradlex.umlsradlex import UMLSRadlex

radlex_csv = "./../resources/RADLEX.csv"
output_dir = "./../out"
config_file = "'./../config.json"


class TestUMLSIntegration(unittest.TestCase):

    def test_upper(self):
        umls_radlex = UMLSRadlex(radlex_csv, output_dir, config_file)
        umls_radlex.integrate()


if __name__ == '__main__':
    unittest.main()