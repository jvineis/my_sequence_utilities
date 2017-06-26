#!/usr/bin/env/python 

from Bio import SeqIO
from Bio.Seq import Seq
import sys

####This is a script to report the lenght of each contig in a fasta file.

### ~~~~~ RUN IT LIKE THIS ~~~~ ###

### python mu-contig_length_report.py in_fasta.fa out.txt ###

in_fasta = open(sys.argv[1], 'rU')
out_list = open(sys.argv[2], 'w')

for seq_record in SeqIO.parse(in_fasta, "fasta"):
    out_list.write(seq_record.id + '\t' + str(len(seq_record.seq)) + '\n')

in_fasta.close()
out_list.close()
