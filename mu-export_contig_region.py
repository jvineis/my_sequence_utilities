#!/usr/bin/env python

from Bio import SeqIO
from Bio.Seq import Seq
import sys

input_fasta = open(sys.argv[1], 'rU')
start = sys.argv[2]
end = sys.argv[3]
out_fasta = open(sys.argv[4], 'w')


for seq_record in SeqIO.parse(input_fasta, "fasta"):
    x = seq_record.seq[int(start):int(end)]
#    print seq_record.seq[50:100]
    out_fasta.write(">"+seq_record.id+"\n"+str(x))
    
