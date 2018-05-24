import csv


class UMLSRadlex(object):

    # project modules
    try:
        from umlsradlex import constants
    except ImportError:
        from . import constants

    radlex_csv = ""
    output_dir = ""

    def __init__(self, radlex_csv, output_dir):
        self.radlex_csv = radlex_csv
        self.output_dir = output_dir

    def integrate(self):
        with open(self.radlex_csv, "rt", encoding='utf8') as csvfile, \
                open(self.output_dir + '/out.csv', "wb") as outfile:

                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(reader, None)  # skip the headers
                writer = csv.writer(outfile)
                for row in reader:
                        printrow = ', '.join(row)
                        print(printrow)