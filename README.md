# Hijacking Sourmash

This repository contains scripts, information and data for the paper "Hijacking a rapid and scalable metagenomic method for plant comparative genomics highlights subgenome dynamics and evolution". 

For the sourmash program, see the sourmash [github](https://github.com/sourmash-bio/sourmash),[documentation](https://sourmash.readthedocs.io/en/latest/) and [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6720031/).

## Sourmash modification

As described in the publication, application of sourmash to polyploid genomes may benefit from the modification of sourmash's default single hierarchical clustering technique. This can be done after installation of sourmash by locating the file "commands.py" and modifying the clustering command presently on line 316:

```
Y = sch.linkage(D, method='single')
```

## Example sourmash commands 

The following section contains the commands used to produce the results for the Hijacking Sourmash paper. Exact directories were provided where "<DirectoryOfChromosomes>" is written. In sourmash plot, the labels originally procued from sourmash are overwridden by the flag "--labeltext new_labels.txt", where "new_labels.txt" ccontained exactly the same labels for the chromosomes, in exactly the same order, but with the directory structure that is produced for the labels by default, removed for legibility. 

### Example sourmash sketch command

This is the first command that will need to be performed for each set of chromosomes. Theroetically, one could use a single fasta file containing all of the chromosomes for the genome with the addition of the "--singleton" command. However, for publically deposited genomes, a genome file will contains numerous scaffolds and contigs alongside the sequences anchored to chromosomes which will make resulting signatures extremely large and visualisation will be difficult. Instead, one may with to seperate out chromosomes first using 

```
sourmash sketch dna -p k=2,k=3,k=4,k=5,k=6,k=7,k=8,k=9,k=10,k=11,k=12,k=13,k=14,k=15,k=16,k=17,k=18,k=19,k=20,k=21,k=31,k=41,k=51,k=61,abund  <DirectoryOfChromosomes>/*.fa

```
### Example sourmash compare command

#### Frequency

```
sourmash compare -k=21 --output k21_freq_compare --csv k21_freq_compare.csv <LocationOfSigs>
```
#### Composition
```
sourmash compare -k=21 --ignore-abundance --output k21_comp_compare --csv k21_comp_compare.csv <LocationOfSigs>
```

### Example sourmash plot command

```
sourmash plot k21_freq_compare --labels --labeltext new_labels.txt --csv k21_plot.csv
```



