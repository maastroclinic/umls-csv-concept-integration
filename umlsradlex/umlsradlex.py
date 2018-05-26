import csv
import configparser
import json


class UMLSRadlex(object):

    # project modules
    try:
        from umlsradlex import constants
    except ImportError:
        from . import constants

    radlex_csv = ""
    output_dir = ""

    def __init__(self, radlex_csv, output_dir, config_file):
        self.radlex_csv = radlex_csv
        self.output_dir = output_dir
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def set_indices(self):
        print('set config')


    def integrate(self):
        with open(self.radlex_csv, "rt", encoding='utf8') as csvfile, \
                open(self.output_dir + '/out.csv', "w", encoding='utf8', newline="\n") as outfile:

                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(reader, None)  # skip the headers
                writer = csv.writer(outfile, delimiter='|')
                for row in reader:

                        printrow = ', '.join(row)
                        print(printrow)
                        writer.writerow(row)

