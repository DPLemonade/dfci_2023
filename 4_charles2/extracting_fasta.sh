#!/bin/bash
#this file is being used to extracting fasta files from a single fasta file into individual files

# Extract sequences from fasta according to names in .txt one by one and creating individual fasta files

cat demultiplex.bc1001--bc1001.hifi_reads_Adpt_QC_names1.txt|while read line 
do 
	touch INDIVIDUAL_ALIGNMENT/$line".fasta"
	echo $line > hoder.txt 

	seqtk subseq demultiplex.bc1001--bc1001.hifi_reads_Adpt_QC.fasta hoder.txt|tr "_" ":" |tr ":" "_" > INDIVIDUAL_ALIGNMENT/$line".fasta"
done


# Extract sequences with names in file name.lst, one sequence name per line:
# seqtk subseq in.fq name.lst

# echo $line > hoder.txt: replace existing text with $line
# echo $line > hoder.txt: append $line to existing text