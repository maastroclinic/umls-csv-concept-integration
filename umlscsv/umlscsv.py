import csv
import json
import os

from umlscsv.constants import *


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


class UMLScsv(object):

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

        self.code_index = HEADERS_RADLEX.index("Class ID")
        self.cui_index = HEADERS_RADLEX.index("UMLS_ID")
        self.str_index = HEADERS_RADLEX.index(self.config['mr_conso_overwrites']['str'])
        self.synonyms_index = HEADERS_RADLEX.index(self.config['mr_conso_synonyms']['str_synonyms'])

        self.overwrites_mr_conso = get_overwrites(HEADERS_MRCONSO, self.config['mr_conso_overwrites'])
        self.overwrites_mr_stry = get_overwrites(HEADERS_MRSTY, self.config['mr_sty_overwrites'])
        self.is_convert_code_to_cui = self.config['is_convert_code_to_cui']

    def set_indices(self):
        print('set config')
        for column in HEADERS_MRCONSO:
            print('set column:' + column)

    def get_index(self, key):
        try:
            self.code_index = HEADERS_MRCONSO.index(self.config['mrconso_map'][key])
        except ValueError as err:
            print("ValueError: {0} default value set".format(err))

    def convert_code_to_number(self, code):
        number = code.replace(ONTOLOGY_PREFIX_ID, '')
        while len(number) < 7:
            number = '0' + number
        return number

    def convert_code_to_cui(self, code):
        code = UMLS_PREFIX_CUI + self.convert_code_to_number(code)
        return code

    def write_mr_conso_row(self, writer, code, cui, str, is_pref):
        mr_conso_row = HEADERS_MRCONSO

        for i, v in self.overwrites_mr_conso.items():
            mr_conso_row[i] = v

        mr_conso_row[0] = cui
        mr_conso_row[6] = is_pref
        mr_conso_row[13] = code
        mr_conso_row[14] = str

        print(', '.join(mr_conso_row))
        writer.writerow(mr_conso_row)

    def write_mr_sty_row(self, writer, cui):
        mr_sty_row = HEADERS_MRSTY

        for i, v in self.overwrites_mr_stry.items():
            mr_sty_row[i] = v

        mr_sty_row[0] = cui

        print(', '.join(mr_sty_row))
        writer.writerow(mr_sty_row)

    def integrate(self):

        with open(self.radlex_csv, "rt", encoding='utf8') as csvfile, \
                open(self.output_dir + MR_CONSO_SUB_PATH, "w", encoding='utf8', newline="\n") as mr_conso, \
                open(self.output_dir + MRSTY_SUB_PATH, "w", encoding='utf8', newline="\n") as mr_sty:

            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader, None)  # skip the headers
            writer_mr_conso = csv.writer(mr_conso, delimiter='|')
            writer_mr_sty = csv.writer(mr_sty, delimiter='|')

            for radlex_row in reader:

                try:
                    code = radlex_row[self.code_index].replace(ONTOLOGY_PREFIX, '')
                    if ONTOLOGY_PREFIX_ID not in code:
                        continue
                    else:
                        is_pref = 'Y'
                        cui = radlex_row[self.cui_index]
                        str = radlex_row[self.str_index]

                        # cui = code
                        # if not cui:
                        cui = code.replace(ONTOLOGY_PREFIX_ID, '')
                        # if self.is_convert_code_to_cui:
                        #     cui = self.convert_code_to_cui(code)

                        self.write_mr_conso_row(writer_mr_conso, code, cui, str, is_pref)

                        for synonym in radlex_row[self.synonyms_index].split("|"):
                            if len(synonym) > 1:
                                is_pref = 'N'
                                self.write_mr_conso_row(writer_mr_conso, code, cui, synonym, is_pref)

                        self.write_mr_sty_row(writer_mr_sty, cui)

                except IndexError as err:
                    print("radlex_row", radlex_row)
                    print("IndexError: {0} ".format(err))
