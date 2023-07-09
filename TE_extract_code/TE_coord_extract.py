import argparse
from collections import defaultdict


parser = argparse.ArgumentParser(description='Outputs coordinates of repeat-masked sequences.')
parser.add_argument("-i", help='Input Clari-TE annotated gff3',required=True,)
parser.add_argument("-ms", help='Min score threshold', type=int,required=True)
parser.add_argument("-mp", help='Whether or not to include partial matches', default=False, action='store_true')

args = parser.parse_args()
i = args.i
ms = args.ms
mp = args.mp

def process_clari(inp_rep, min_score, partial_match):
    lines_read  = 0
    fragmented =  0
    complete  = 0
    match_part =  0

    thresh_removed = 0
    thresh_kept =  0
    for line in inp_rep:
        line = line.strip("\n")
        lines_read +=1
        print("line: "  +  str(lines_read))
        info_store = []
        if not line[0] == "#" or not line.strip():
            try:
                line = line.strip("\n")
                line = line.split("\t")
                name =  line[0]
                info_store.append(name)
                info = line[8]
                info = info.split(";")
                ID = info[0]
                ID = ID.split("=")
                ID = ID[1]
                ID = ID.split("_")
                start =  line[3]
                stop = line[4]
                info_store.append(start)
                info_store.append(stop)
                #MP = match part? 
                if "mp" not in ID:
                    status =  info[-1]
                    status = status.split("=")
                    status = status[-1]
                    print(status)
                    if status  ==  "complete":
                        complete +=1
                        comp = info[1]
                        comp = comp.strip(" ")
                        comp = comp.split("=")
                        comp  =  comp[1]
                        comp  = comp.split(" ")
                        comp_length  = len(comp)
                        if comp_length == 2:
                            fam = comp[0]
                            score = float(comp[1])
                            if score  >= min_score:
                                start = line[3]
                                end = line[4]
                                strand = line[6]
                                thresh_kept  +=1
                                with open("TE_coords.txt",  "a+") as  f:
                                    f.write(info[0] +  "_" +  "("+ strand +  ")"  +"\n")
                                    f.write(str(start) + ":" + str(end) + "\n")
                            else:
                                thresh_removed  +=1
                        else:
                            i=0
                            j = i+1
                            thresh_hits = 0
                            while i < len(comp):
                                # print(line)
                                # print(comp)
                                fam = comp[i]
                                # print(fam)
                                # print(comp[j])
                                try:
                                    score = float(comp[j])
                                    # print(score)
                                except:
                                    #Hitting a "no match" sequence so not of use
                                    continue
                                if score  >= min_score:
                                    thresh_hits +=1
                                    start = line[3]
                                    end = line[4]
                                    strand =  line[6]
                                    thresh_kept  +=1
                                    with open(fam +  ".txt",  "a+") as  f:
                                        f.write(info[0] +  "_" +  "("+ strand +  ")"  +"\n")
                                        f.write(str(start) + ":" + str(end) + "\n") 
                                i += 2
                                j = i+1
                            if thresh_hits ==  0:
                                thresh_removed  +=1
                            if thresh_hits  > 1:
                                print("WARNING: Multiple  hits above threshold for", info[0])
                    elif status  ==  "fragmented":
                        fragmented +=1
                        comp = info[1]
                        print("here",comp)
                        try:
                            comp = comp.strip(" ")
                            comp = comp.split("=")
                            comp  =  comp[1]
                            comp  = comp.split(" ")
                            comp_length  = len(comp)
                        except:
                            print("Error with Section 1")
                        if comp_length == 2:
                            try:
                                fam = comp[0]
                                score = float(comp[1])
                            except:
                                print("Error with section 2")
                            if score  >= min_score:
                                try:
                                    start = line[3]
                                    end = line[4]
                                    strand = line[6]
                                    thresh_kept  +=1
                                    with open("TE_coords_frag.txt",  "a+") as  f:
                                        f.write(info[0] +  "_" +  "("+ strand +  ")"  +"\n")
                                        f.write(str(start) + ":" + str(end) + "\n")
                                except:
                                    print("Error with section3 3")
                            else:
                                print("Didn't make the threshold")
                                thresh_removed  +=1
                        else:
                            try:
                                i=0
                                j = i+1
                                thresh_hits = 0
                                while i < len(comp):
                                    # print(line)
                                    # print(comp)
                                    fam = comp[i]
                                    # print(fam)
                                    # print(comp[j])
                                    try:
                                        score = float(comp[j])
                                        print("score",  score)
                                        if score  >= min_score:
                                            thresh_hits +=1
                                            start = line[3]
                                            end = line[4]
                                            strand = line[6]
                                            thresh_kept  +=1
                                            with open("TE_coords_frag.txt",  "a+") as  f:
                                                f.write(info[0] +  "_" +  "("+ strand +  ")"  +"\n")
                                                f.write(str(start) + ":" + str(end) + "\n") 
                                        i += 2
                                        j = i+1
                                    except:
                                        #Hitting a "no match" sequence so not of use
                                        print("Hitting a no match")
                                        i += 2
                                        j = i+1
                                if thresh_hits ==  0:
                                    thresh_removed  +=1
                                if thresh_hits  > 1:
                                    print("WARNING: Multiple  hits above threshold for", info[0])
                            except:
                                print("Error with sction 4")
                else:
                    match_part +=1
                    if partial_match == True:
                        MP_ID  = info[0]
                        print(MP_ID)
                        parent_info = info[1:]
                        MP_ID = MP_ID.split("=")
                        MP_ID = MP_ID [1]
                        MP_ID = MP_ID[3:]
                        MP_ID = MP_ID.split("_")
                        MP_ID_short = MP_ID[:-1]
                        MP_ID_short = "_".join(MP_ID_short)
                        if len(parent_info) == 1:
                            file_name = MP_ID_short
                            seq_name = MP_ID
                            seq_name = "_".join(seq_name)
                            start = line[3]
                            end = line[4]
                            strand = line[6]
                            with open("TE_MP.txt",  "a+") as  f:
                                f.write(seq_name + "_" +  "("+ strand +  ")" + "\n")
                                f.write(str(start) + ":" + str(end) + "\n") 
            except:
                print("Error processing line " + str(lines_read) + "\n")
                print("Line looks ike this"  + "\n")
                print(line + "\n")


    return()

with open(i) as inp:
    process_clari(inp, ms, mp)

#Need a range subprocess?

