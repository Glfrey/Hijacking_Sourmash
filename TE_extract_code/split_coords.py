import argparse
import itertools
from pathlib import Path

parser = argparse.ArgumentParser(description='Split coord file')
parser.add_argument("-c", help='Input coordinates',required=True)

args = parser.parse_args()
c = args.c

def split(full_set):
    count = 0
    for line1,line2 in itertools.zip_longest(*[full_set]*2):
        if count == 0:
            with open("TE_Coords_S0.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 1:
            with open("TE_Coords_S1.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 2:
            with open("TE_Coords_S2.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 3:
            with open("TE_Coords_S3.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 4:
            with open("TE_Coords_S4.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 5:
            with open("TE_Coords_S5.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 6:
            with open("TE_Coords_S6.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 7:
            with open("TE_Coords_S7.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 8:
            with open("TE_Coords_S8.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 9:
            with open("TE_Coords_S9.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 10:
            with open("TE_Coords_S10.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 11:
            with open("TE_Coords_S11.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 12:
            with open("TE_Coords_S12.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 13:
            with open("TE_Coords_S13.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 14:
            with open("TE_Coords_S14.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 15:
            with open("TE_Coords_S15.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 16:
            with open("TE_Coords_S16.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 17:
            with open("TE_Coords_S17.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 18:
            with open("TE_Coords_S18.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 19:
            with open("TE_Coords_S19.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        elif count == 20:
            with open("TE_Coords_S20.txt", "a+") as f:
                f.write(line1)
                f.write(line2)
        count+=1
        if count  == 21:
            count = 0
    
    return()

with open(c) as  full_file:
    split(full_file)
