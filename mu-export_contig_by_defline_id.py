
from Bio import SeqIO
from Bio.Seq import Seq
import sys

input_fasta_name = sys.argv[1]
input_fasta = open(input_fasta_name, 'rU')
defline_character = sys.argv[2]
out_fasta = open(defline_character+'.fa', 'w')

count = 0
for seq_record in SeqIO.parse(input_fasta, "fasta"):
    if defline_character in seq_record.id:
        out_fasta.write(">"+seq_record.id+"\n"+str(seq_record.seq)+"\n")
        count += 1

print('mu-export_contig_by_defline_id just wrote %d seqs to %s' % (count, defline_character+'.fa'))
