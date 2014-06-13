import os
import re
import csv

fnameRegex = re.compile('^\d+.+\.csv', re.IGNORECASE)
filenames = []
for fname in os.listdir("."):
    if fnameRegex.search(fname) is not None:
	filenames.append(fname)

fout = open('seed.sql', mode='wb')

# open each file to get column names
tableRegex = re.compile('^\d+_(\w+)\.')
filenames = sorted(filenames)
for fname in filenames:
    tableName = tableRegex.match(fname).group(1)
    f = open(fname, mode='rb')
    reader = csv.DictReader(f)
    print fname
    colNames = reader.fieldnames
    f.close()

    colNamesStr = ','.join(colNames)
    fout.write('\\COPY ' + tableName + ' (' + colNamesStr + ') ' + 'FROM \'' + fname + '\' CSV HEADER\n' )

fout.close()
