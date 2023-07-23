# BLAST

This folder contains relevant files used to perform BLAST processing and analysis for the humanized mice datasets.


## Overview

Since the humanized mice dataset A3, B3, and C3 contain various antibodies present in the humanized mice, further filtering using BLAST is required to identify anti-HA antibodies and the frequency in which they occur. I BLASTed the A3, B3, and C3 sequences against the existing HA database in the Marasco Lab.


## Files and workflow

1. Preprocessing of HA database
protein_fasta.py is used to complete the preprocessing step. It first retains only Influenza A sequences, removes duplicate sequences from the 2018 database file, then extracts relevant datafields and compiles the processed anti-HA sequences into cleaned_ha_database.xlsx. A ha_seq.fasta file that only contains the sequences is also constructed.

2. BLAST
BLASTing A3, B3, and C3 against the HA database is performed in this step. Since blastx was deemed excessively time-consuming after some initial attempts, the HA database was reverse translated using EMBOSS and blastn was used instead. The results are stored in the _results.txt files. The amino acid database and reverse translated nucleotide databases and named ha_seq_db and ha_seq_nucl_db.

3. Processing BLAST results
Additional interpretation of the BLAST results is required. The first step was to parse the raw BLAST results, which was accomplished via parse_results.sh. The _results_seq_cnt.txt file contains the number of hits for each sequence in the HA database, while _results_seq90_cnt.txt contains number of hits that had Identity scores larger than 90%. Both files use the same format, with the two numbers in each row representing the number of hits and the sequence number. An overview of the BLAST results for all three datasets is contained in BLAST_results.txt.
Note: sequences in cleaned_ha_database.xlsx are numbed 0~691 while sequences in the result files are numbered 1~692.

4. Plotting of results
Plots were constructed using plot_results.py. In each plot, the X axis represents the sequence number while the Y axis represents the number of hits for each sequences in percentage values normalized using total number of sequences. The plot.png files contain all sequences while plot_2.png sequences only contain sequences numbered 400~692. The 90plot.png files contain sequences that have Identity scores larger than or equal to 90%.


## To-do

Make results for sequences with 100% Identity score.