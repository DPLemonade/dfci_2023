#!/bin/bash 
#this file is taking cordinates of each fasta file and extracting the  given/required region

strand=REV
cat "Blast_data_"$strand"_reads.txt"|while read line 
#cat reverse_error_file2_edited.txt|while read line 
do 
	read -a name <<< $line
	seq=$(echo ${name[0]}|sed 's/_seq//g')
	echo $line|tr " " "\t" > current_file.txt
	bedtools getfasta -fi RENAMED_FILES/REV/$seq"_Rnamed_Fasta.fasta" -bed current_file.txt -fo RnamedTrimed_Files/$strand"_Trimmed_2"/$seq"_Rnamed_Trimed_Fasta.fas" 
done

# bedtools getfasta [OPTIONS] -fi <input FASTA> -bed <BED/GFF/VCF>
# bedtools getfasta extracts sequences from a FASTA file for each of the intervals defined in a BED/GFF/VCF file
# -fo: specify output file
# -bed file contains coordinates of segment to be extracted

'''
$ cat test.fa
>chr1
AAAAAAAACCCCCCCCCCCCCGCTACTGGGGGGGGGGGGGGGGGG

$ cat test.bed
chr1 5 10

$ bedtools getfasta -fi test.fa -bed test.bed
>chr1:5-10
AAACC

# optionally write to an output file
$ bedtools getfasta -fi test.fa -bed test.bed -fo test.fa.out

$ cat test.fa.out
>chr1:5-10
AAACC
'''