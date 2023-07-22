#!/bin/bash

cat A3/A3_results.txt | grep 'Identities' -B 5| grep '(100%)\|(9[0-9]%)' -B 5 | awk '/>/ {print}' | sed 's/>//' | awk '{print $1}' | sort -n | uniq -c > A3/A3_results_seq90_cnt.txt
#awk '/>/ {print}' A3/A3_results.txt | sed 's/>//' | awk '{print $1}' | sort -n | uniq -c > A3/A3_results_seq_cnt.txt

# A3_results_seq_cnt.txt: file containing number of hits for each sequence
# Format: (No. of hits, sequence number)

# A3_results_seq90_cnt.txt: file containing number of hits that had Identity score larger than 90%