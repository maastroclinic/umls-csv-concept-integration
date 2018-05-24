import unittest
from umlsradlex.umlsradlex import UMLSRadlex

radlex_csv = ""
output_dir = ""


class TestUMLSIntegration(unittest.TestCase):

    def test_upper(self):
        umls_radlex = UMLSRadlex(radlex_csv, output_dir)


if __name__ == '__main__':
    unittest.main()