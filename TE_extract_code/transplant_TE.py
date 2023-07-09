import argparse
from collections import defaultdict
from Bio.SeqIO.FastaIO import SimpleFastaParser
from pathlib import Path
import itertools
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import gzip


parser = argparse.ArgumentParser(description='Transplants repeats')
parser.add_argument("-r", help='Repeats',required=True,  nargs="+")
parser.add_argument("-i", help='Input sequence',required=True)


args = parser.parse_args()
i = args.i
r = args.r



def combine_seq(inrepeats, inpSeq):
    if not os.path.exists("transplanted"):
        os.mkdir("transplanted")
    with gzip.open(inpSeq, "rt") as inseq:
        name = Path(inpSeq).stem
        name  = name[:-3] +"_transplanted.fa"
        for reps in inrepeats:
            with open(reps) as repeats:
                transplanted =  join("transplanted", name)
                with open(transplanted,"a+") as t:
                    for title,seq in SimpleFastaParser(inseq):
                        print(title)
                        t.write(">" +title +  "\n")
                        t.write(seq +  "\n")
                    for title,seq in SimpleFastaParser(repeats):
                        t.write(">" + title +  "\n")
                        t.write(seq +  "\n")

    return()

combine_seq(r,i)
