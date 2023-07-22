Explanation of files

ha_seq_db: HA database
ha_seq_nucl_db: Reverse translated HA database (using EMBOSS)

2018_August_Flu-mAb_Database.xlsx: Raw HA database
cleaned_ha_dataset.xlsx: Database after removing duplicate sequences and Influenza B sequences

plot_results.py: generates graph that shows distribution of frequency across different sequences
protein_fasta.py: Parses raw HA database and produces cleaned_ha_dataset.xlsx

_M1_collapse-unique.fasta: Query sequences

BLAST_results.txt: Overview of BLAST results for A3, B3, and C3

_results.txt: BLAST results
_results_seq_cnt.txt: Explained in parse_results.sh
_results_seq90_cnt.txt: Same as _results_seq_cnt.txt, but only contains sequences with Identity matches >= 90%
.png files are explained in plot_results.py file

parse_results.sh: Extracting results from _results.txt files