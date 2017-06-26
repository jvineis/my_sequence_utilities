#!/usr/bin/env python

import sys
from Bio import SeqIO

with open(sys.argv[1], 'rU') as handle:
    for record in SeqIO.parse(handle, "fastq"):
        print(record.id)

