#!/bin/bash

#this file is renaming file from into number
cat bc1001.hifi_reads_Adpt_QC_names2.txt|while read line 
do 
    read -a name <<< $line

    touch RnamedFasta/RENAMED_FILES/${name[1]}"_Rnamed_Fasta.fasta"
    cat RnamedFasta/${name[0]}".fas"|sed 's/'${name[0]}'/'${name[1]}'_seq/' > RnamedFasta/RENAMED_FILES/${name[1]}"_Rnamed_Fasta.fasta"
   
done


# sed 's/'${name[0]}'/'${name[1]}'_seq/': replace first occurrence of name[0] in each line with name[1]