#Seperates fasta file by chromosome

from Bio import SeqIO
from Bio.SeqIO.FastaIO import SimpleFastaParser
import argparse
import sys
import os


parser = argparse.ArgumentParser(description='Extracts assembled chromosomes/contigs/scaffolds from bulk fasta file')
parser.add_argument("-i", help='Input file',required=True)


if len(sys.argv) < 1:
    print("You must provide input!", file = sys.stderr)
    parser.print_help(sys.stderr)
    sys.exit(1)


args = parser.parse_args()
i = args.i

cwd = os.getcwd()
unplaced_dirname = ("unplaced")
placed_dirname = ("placed")
os.mkdir(unplaced_dirname)
os.mkdir(placed_dirname)

with open(i) as input:
    for title,seq in SimpleFastaParser(input):
            if "chromosome" in title:
                os.chdir(placed_dirname)
                with open(title+".fa", "a+") as new:
                    new.write(">"+title+"\n")
                    new.write(seq)
                    os.chdir('..')
            else:
                os.chdir(unplaced_dirname)
                with open(title+".fa", "a+") as new:
                    new.write(">"+title+"\n")
                    new.write(seq)
                    os.chdir('..')
