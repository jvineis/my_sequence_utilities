#!/bin/env python

import os
import sys
import glob

#################################################################################
# input and stuff
#################################################################################

target_fasta = sys.argv[1]
output_dir = sys.argv[2]
#prefix name is the base name of your bowtie2-align command
prefix_name = sys.argv[3]
ref_name = sys.argv[4]

if not target_fasta.startswith('/') or not output_dir.startswith('/'):
    print "please provide a full path (I mean, a path that starts with '/')"
    sys.exit()


if not os.path.exists(output_dir):
    try:
        os.makedirs(output_dir)
    except:
        print "output dir wasn't there, tried to create one, but it didn't work :/"
        sys.exit()

#fasta_list = sorted(glob.glob(os.path.join(target_fasta, '*.fa')))
fasta_list = glob.glob(target_fasta+'*.fa')

for pair in fasta_list:
    print '- %s' % (os.path.basename(pair))

print
try:
    raw_input("Does this fasta look right? If not, press CTRL+C, otherwise press ENTER to continue..")
except:
    print
    sys.exit()


#################################################################################
# business time
#################################################################################

script_template = """#!/bin/bash/
clusterize bowtie2 -x %(ref_name)s -U %(fasta)s -f -S %(output_dir)s%(prefix)s.sam """

params = {}
params['project'] = prefix_name
params['input_dir'] = target_fasta
params['output_dir'] = output_dir
params['prefix'] = 'P'+prefix_name
params['ref_name'] = ref_name
params['fasta'] = ','.join([os.path.join(target_fasta,pair) for pair in fasta_list])


open('P%s_bowtie_mapping.shx' % params['project'], 'w').write(script_template % (params))
