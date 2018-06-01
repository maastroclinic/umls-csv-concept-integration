import unittest
from umlscsv.umlscsv import UMLScsv

radlex_csv = "./../resources/RADLEX-2.csv"
output_dir = "./../out"
config_file = "./../config.json"


class TestUMLSIntegration(unittest.TestCase):

    def test_upper(self):
        umls_radlex = UMLScsv(radlex_csv, output_dir, config_file)
        umls_radlex.integrate()


if __name__ == '__main__':
    unittest.main()