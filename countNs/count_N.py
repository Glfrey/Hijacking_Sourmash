import argparse
from Bio import SeqIO
from Bio.SeqIO.FastaIO import SimpleFastaParser


parser = argparse.ArgumentParser(description='Stores edge k-mers in a set')
parser.add_argument("-i", help='Input fasta fil',required=True)


args = parser.parse_args()
i = args.i


n_count = 0
total_count = 0

with open(i) as input:
    for title,seq in SimpleFastaParser(input):
        for nt in seq:
            if nt == "N" or nt == "n":
                n_count  +=1
            total_count +=1

percent = n_count / total_count * 100

print("Total bases:", total_count)
print("N bases", n_count)
print("Percent covered by N's", percent)
