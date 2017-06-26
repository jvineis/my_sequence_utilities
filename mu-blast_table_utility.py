#!/bin/usr/env python

import sys
#from Bio import SearchIO
from Bio.Blast import NCBIXML
#blast_infile = open(sys.argv[1], 'rU')
for rec in NCBIXML.parse(open(sys.argv[1], 'r')):
    for alignment in rec.alignments:
        for hsp in alignment.hsps:
            print(hsp.hit)
    
