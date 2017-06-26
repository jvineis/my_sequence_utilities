#!/bin/usr/env python
import sys

infile = open(sys.argv[1], 'rU')

dict_out = {}
for line in infile:
    x = line.strip().split("\t")
    dict_out[x[0]] = x[0:len(x)]

outfile = open(sys.argv[2], 'w')

for key in dict_out.keys():
    outfile.write(dict_out[key][0]+"\t"+dict_out[key][1]+"\t"+dict_out[key][2]+"\t"+dict_out[key][3]+"\n")
