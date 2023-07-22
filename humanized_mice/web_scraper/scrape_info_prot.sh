#!/bin/bash
> seq_info.txt
awk '/^LOCUS/ {print $NF '\n'}' seq_info_all.txt >> seq_info.txt
awk '/DEFINITION/{flag=1} /ACCESSION/{flag=0} flag{for (i=1; i<=NF; i++) printf $i " "}' seq_info_all.txt | sed 's/DEFINITION//' >> seq_info.txt
awk '/AUTHORS/{flag=1} /TITLE/{flag=0} flag{if ($1=="AUTHORS") printf "\n"; for (i=1; i<=NF; i++) printf $i " "}' seq_info_all.txt | head -2 | sed 's/AUTHORS//' >> seq_info.txt
awk '/JOURNAL/ {print}' seq_info_all.txt | head -1 | sed 's/JOURNAL//' >> seq_info.txt
awk '/PUBMED/ {print}' seq_info_all.txt | head -1 | sed 's/PUBMED//' >> seq_info.txt