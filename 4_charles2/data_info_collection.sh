#!/bin/bash
#this file extracts information from the database generated.
touch blast_data.txt
cat read_number.txt|while read line
do 
	cat BLAST2/$line"_blast_result.txt"|grep Query|head -1|tr "\n" "\t" >> blast_data.txt
	cat BLAST2/$line"_blast_result.txt"|grep Query|head -2|tail -1|awk '{print $1,$2}'|tr "\n" "\t" >> blast_data.txt
	cat BLAST2/$line"_blast_result.txt"|grep Sbjct|head -1|awk '{print $1,$2}'|tr "\n" "\t" >> blast_data.txt
	cat BLAST2/$line"_blast_result.txt"|grep Query|tail -1|awk '{print $1,$4}'|tr "\n" "\t" >> blast_data.txt
	cat BLAST2/$line"_blast_result.txt"|grep Sbjct|tail -1|awk '{print $1,$4}' >> blast_data.txt
	
done

# grep Query: display lines in file that contain Query
# awk '{print $1, $2}': print first and second field delimited by white spaces in each line
# tr "\n" "\t": change '\n' into '\t'