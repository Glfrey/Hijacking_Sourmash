import argparse
from collections import defaultdict
from Bio.SeqIO.FastaIO import SimpleFastaParser
from pathlib import Path
import itertools
import os
from os import listdir
from os.path import isfile, join


parser = argparse.ArgumentParser(description='Merge files from extract TEs')
parser.add_argument("-i", help='Input directories',required=True,  nargs="+")

args = parser.parse_args()
i = args.i


def merge_files(inp_files):
    os.mkdir("combined_TEs")
    # query_dir  =  inp_files[1:]
    fullfiles =  []
    for dir in inp_files:
        for file in listdir(dir):
            if file.endswith(".fa"):
                fullfiles.append(file)
    uniquefiles = list(set(fullfiles))
    for file in uniquefiles:
        for dir in inp_files:
            old_file = join(dir, file)
            if  os.path.isfile(old_file):
                new_file =  join("combined_TEs", file)
                with  open(old_file) as old:
                    with open(new_file, "a+") as new:
                        for title,seq in SimpleFastaParser(old):
                            new.write(">" + title + '\n')
                            new.write(seq + '\n')


    return

merge_files(i)


