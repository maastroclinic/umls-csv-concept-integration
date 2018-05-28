import csv
import json
import os

from umlsradlex.constants import *


def get_overwrites(header, overwrite_map):
    overwrites = {}
    for k, v in overwrite_map.items():
        try:
            index = header.index(k)
            overwrites[index] = v
        except ValueError as err:
            print(header)
            print("ValueError not in header: {0}".format(err))
    return overwrites


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

        if not os.path.exists(output_dir + META_DIR):
            os.makedirs(output_dir + META_DIR)

        with open(config_file, 'r') as f:
            self.config = json.load(f)

        self.cui_index = HEADERS_RADLEX.index("Class ID")
        self.str_index = HEADERS_RADLEX.index(self.config['mr_conso_overwrites']['str'])
        self.synonyms_index = HEADERS_RADLEX.index(self.config['mr_conso_synonyms']['str_synonyms'])

        self.overwrites_mr_conso = get_overwrites(HEADERS_MRCONSO, self.config['mr_conso_overwrites'])
        self.overwrites_mr_stry = get_overwrites(HEADERS_MRSTY, self.config['mr_sty_overwrites'])


    def set_indices(self):
        print('set config')
        for column in HEADERS_MRCONSO:
            print('set column:' + column)


    def get_index(self, key):
        try:
            self.cui_index = HEADERS_MRCONSO.index(self.config['mrconso_map'][key])
        except ValueError as err:
            print("ValueError: {0} default value set".format(err))



    def integrate(self):
        with open(self.radlex_csv, "rt", encoding='utf8') as csvfile, \
                open(self.output_dir + MR_CONSO_SUB_PATH, "w", encoding='utf8', newline="\n") as mr_conso, \
                open(self.output_dir + MRSTY_SUB_PATH, "w", encoding='utf8', newline="\n") as mr_sty:

            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader, None)  # skip the headers
            writer_mr_conso = csv.writer(mr_conso, delimiter='|')
            writer_mr_sty = csv.writer(mr_sty, delimiter='|')

            index = 0
            for radlex_row in reader:
                index = index+1
                try:
                    mr_conso_row = HEADERS_MRCONSO
                    mr_sty_row = HEADERS_MRSTY

                    cui = radlex_row[self.cui_index].replace(RADLEX_PREFIX, '')
                    if "RID" not in cui:
                        continue
                   
                    for i, v in self.overwrites_mr_conso.items():
                        mr_conso_row[i] = v

                    mr_conso_row[0] = cui
                    mr_conso_row[14] = radlex_row[self.str_index]

                    printrow = ', '.join(mr_conso_row)
                    print(printrow)
                    writer_mr_conso.writerow(mr_conso_row)

                    for synonym in radlex_row[self.synonyms_index].split("|"):
                        if len(synonym) > 1:
                            mr_conso_row[14] = synonym
                            writer_mr_conso.writerow(mr_conso_row)

                    for i, v in self.overwrites_mr_stry.items():
                        mr_sty_row[i] = v

                    mr_sty_row[0] = cui

                    printrow = ', '.join(mr_sty_row)
                    print(printrow)
                    writer_mr_sty.writerow(mr_sty_row)
                except IndexError as err:
                    print("radlex_row", radlex_row)
                    print("IndexError: {0} ".format(err))
