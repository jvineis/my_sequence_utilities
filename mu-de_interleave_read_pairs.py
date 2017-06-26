#!/usr/bin/env python

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# This script is designed to split an interleave fastq that was created by the dmwelch lab from  #
# what was once a paired read file. I can't find the pairs and this is a good python exercise for#
# a rainy monday morning. The original headers of the files had tabs so I had to fix them like   #
# This: zcat paired450.fa.gz | sed 's/\t/_/g' > paired_450_fixed_header.fa                       #
#       zcat paired800.fa.gz | sed 's/\t/_/g' > paired_850_fixed_header.fa                       #
# The original files are here /groups/rotifer/Avgenome/Illumina.

# run the script like this 
# "python ~/scripts/mu-de_interleave_read_pairs.py paired_450_fixed_header"

import sys
from Bio import SeqIO
import gzip 

infile_prefix = sys.argv[1] 
infile_name = infile_prefix+".fa"
infastq = open(infile_name, 'rU') # read in the fastq file
out_name_1 = infile_prefix+"_R1.fa"
out_name_2 = infile_prefix+"_R2.fa"
seq_out1 = open(out_name_1, 'w')
seq_out2 = open(out_name_2, 'w')

for rec in SeqIO.parse(infastq, "fasta"):
    if "ATCAG_1" in rec.id:
        seq_out1.write(">"+str(rec.id)+"\n"+str(rec.seq)+"\n")
    elif "ATCAG_2" in rec.id:
        seq_out2.write(">"+str(rec.id)+"\n"+str(rec.seq)+"\n")

infastq.close()
seq_out1.close()
seq_out2.close()
