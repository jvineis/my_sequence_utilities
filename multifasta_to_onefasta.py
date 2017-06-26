#!/usr/bin/env python
from Bio import SeqIO
import sys

input_handle = open(sys.argv[1], "rU")
outfile= open(sys.argv[2], "w")
seqs_list = []
sequences = SeqIO.parse(input_handle, "fasta")
for record in sequences:
   #print record.seq
   seqs_list.append(record.seq)
for i in seqs_list:
   print>>outfile, i
