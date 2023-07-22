#!/bin/bash

cat read_number.txt|while read line 
do 
	blastn -db ref/G36_WT_KABAT.fasta -query RENAMED_FILES/$line"_Rnamed_Fasta.fasta" -out BLAST2/$line"_blast_result.txt"
done 
