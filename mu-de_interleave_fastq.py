#!/usr/bin/env python 

import sys
from Bio import SeqIO
from Bio.Seq import Seq

input_fastq = sys.argv[1]
read1 = open(input_fastq.strip(".fastq")+"_R1.fastq",'w')
read2 = open(input_fastq.strip(".fastq")+"_R2.fastq",'w')
with open(input_fastq, 'rU') as f:
    for rec in SeqIO.parse(f, "fastq"):
        print rec.id
#        if "1:N:0" in rec.id:
#            SeqIO.write(rec, read1, "fastq")
#        else:
#            SeqIO.write(rec, read2, "fastq")
