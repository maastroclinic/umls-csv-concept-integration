import csv

# project modules
try:
    import constants
except ImportError:
    from . import constants


with open('./resources/RADLEX.csv', "rt", encoding='utf8') as csvfile, open('./resources/out.csv', "wb") as outfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
                printrow = ', '.join(row)
                print(printrow)