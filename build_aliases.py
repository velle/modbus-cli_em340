#!/usr/bin/env python3

import csv

DATA_FORMATS = {
    'INT16':'h',
    'INT32':'i',
    'UINT16':'H',
    'UINT32':'I',
}

def to_alias(s):
    s = s.replace('(+)','PLUS')
    s = s.replace('(-)','MINUS')

    s = s.replace(' ','_')
    s = s.replace('-','_')
    return s

with open('data/manually_typed.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    with open('data/EM340_aliases.txt','w') as aliasfile:
        for row in reader:
            addr = int(row['hexaddr'][:-1],16)
            alias = to_alias(row['name'])
            access = '%s/%s' % (addr,DATA_FORMATS[row['datatype']])
            line = '%s %s\n' % (alias,access,)
            aliasfile.write(line)
