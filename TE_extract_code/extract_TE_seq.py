import argparse
from collections import defaultdict
from Bio.SeqIO.FastaIO import SimpleFastaParser
from pathlib import Path
import itertools
from Bio.Seq import Seq
import ray


parser = argparse.ArgumentParser(description='Given TE coordinates outputs the corresponding sequences')
parser.add_argument("-c", help='Input coordinates',required=True)
parser.add_argument("-f", help='Output family', action='store_true')
parser.add_argument("-sf", help='Output subfamily', action='store_true')
parser.add_argument("-d", help='Directory containing reference chromosomes')


args = parser.parse_args()
c = args.c
f = args.f
sf = args.sf
d = args.d

# ray.init()

# @ray.remote(num_cpus=32)
def extract_TEs(coords, fam_set, sub_set, ref_dir):
    count = 0
    for line1,line2 in itertools.zip_longest(*[coords]*2):
        print("working on sequence ", count)
        count +=1
        line1 = line1.strip("\n")
        print(line1)
        line1 = line1.split("_")
        name  =  line1[0][3:]
        family = line1[1]
        sub_fam  = line1[2]
        number =  line1[3]
        orientation = line1[4][1]
        coord_lst = line2.split(":")

        try:
            int(name[3])
        except:
            name =  "Un"

        print("query name", name)

        if not name =="Un":
            name = name[-2:]
    
        print("truncated name", name)

        print("searching for file", name+".fa")
        
        with open(ref_dir + "/" + name+".fa", "r") as ref:
            for title,seq in SimpleFastaParser(ref):
                start_coord  =  int(coord_lst[0])
                end_coord  =  int(coord_lst[1])
                print("start", start_coord)
                print("end", end_coord)
                TE  = seq[start_coord:end_coord]
                if orientation ==  "-":
                    print("reversing...")
                    TE = Seq(TE)
                    TE = TE.complement()

            header =  "_".join(line1)
            TE  = TE.upper()

            if  family == "no" and fam_set  == True or family == "no"  and sub_set  == True:
                print(family)
                with open("no_matches.fa", 'a+') as f:
                    f.write(">" + header + "\n")
                    f.write(str(TE)  +  "\n")
            else:
                if fam_set ==  True:
                    with open(name + "_" + family+"_TEs.fa",'a+') as f:
                        f.write(">" + header + "\n")
                        f.write(str(TE)  +  "\n")
                        if sub_fam  == True:
                            with open(name +"_TEs.fa",'a+') as f:
                                f.write(">" + header + "\n")
                                f.write(str(TE)  +  "\n")

                        


    return()

with open(c) as TE_coords:
    extract_TEs(TE_coords, f, sf, d)
    # future = extract_TEs.remote(TE_coords, f, sf)
    # extraction = ray.get(future) 
    print("All done")
    

#TODO Test "N" content of TE content to see if we need to implement a filter.
