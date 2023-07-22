#!/bin/bash

#this file is changing the names from files into numbers
cat bc1001.hifi_reads_Adpt_QC_names2.txt|while read line 
do 
    read -a name <<< $line
    touch RnamedFasta/RENAMED_FILES/${name[1]}"_Rnamed_Fasta.fasta"
    cat RnamedFasta/${name[0]}".fas"|sed 's/'${name[0]}'/'${name[1]}'_seq/' > RnamedFasta/RENAMED_FILES/${name[1]}"_Rnamed_Fasta.fasta"
   
done

# same as name_change.sh