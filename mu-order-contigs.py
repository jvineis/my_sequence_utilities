#!/usr/bin/python

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
#  This script takes a list of contigs.  Each contig should be  #
#  on a new row.  The contigs in the list will be reverse complimented
#  and added to a new fasta file (user defined).  Sequences not in the list will be 
#  written to the new fasta file in their original orientation.  The script is helpful
#  when looking at the origin of replication based on synteny with a reference
#  genome.

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

infile = open(sys.argv[1], 'rU')
headers = [line.strip() for line in infile]

inseq = open(sys.argv[2], 'rU')

new_fasta = open(sys.argv[3], 'w')
for seq_record in SeqIO.parse(inseq, "fasta"):
    if seq_record.id in headers:
        print "%s is a sequence to revcomp" % seq_record.id
        x = seq_record.seq.reverse_complement()
        new_fasta.write('>' + seq_record.id + '\n' + str(x))
    else:
        new_fasta.write('>' + seq_record.id + '\n' + str(seq_record.seq))
