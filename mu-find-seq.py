#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

##your fasta file of interest
infile = open(sys.argv[1], 'rU')
seq_to_find = sys.argv[2]
for seq_record in SeqIO.parse(infile, "fasta"):
    if seq_to_find in seq_record.seq:
        print seq_record.id + "\n" + seq_record.seq
    else:
        if seq_to_find in seq_record.seq.reverse_complement():
            print "It was reversecomp"+"\n"+ seq_record.id + "\n" + seq_record.seq                
