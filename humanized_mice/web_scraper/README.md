# Web Scraper

This folder contains relevant files used to build web scraper for anti-HA database.


## Overview

The goal of building and using this scraper is to construct an anti-HA database that includes newly discovered nucleotide/amino acid sequences and augments the existing manually-assembled database at the Marasco Lab. I used E-utilities APIs to scrape sequence data in the Nucleotide and Protein databases in Entrez and processed them using IMGT High-V Quest to obtain additional information about epitopes and V, D, and J regions. I collected a total of approximately 2,000 nucleotide sequences and 3,000 amino acid sequences.


## Data source and API

The Entrez Programming Utilities (E-utilities) are a set of nine server-side programs that provide a stable interface into the Entrez query and database system at the National Center for Biotechnology Information (NCBI). The E-utilities use a fixed URL syntax that translates a standard set of input parameters into the values necessary for various NCBI software components to search for and retrieve the requested data. The E-utilities are therefore the structured interface to the Entrez system, which currently includes 38 databases covering a variety of biomedical data, including nucleotide and protein sequences, gene records, three-dimensional molecular structures, and the biomedical literature.


## Files and workflow

1. Scrape sequences and organize into .fasta files
scrape_seq.py scrapes sequence data from the Nucleotide and Protein databases using ESearch and EFetch. ESearch stores all sequence data in the History Server while EFetch retrieves data in batches. ESearch queries use influenza, antibody, and human[organism] as keywords. The sequences are stored in _seq.fasta files while the corresponding IDs are stored in _id_file.txt.

2. Scrape sequence data and construct NIH database
scrape_info_.py scrapes additional information from the Nucleotide and Protein databases using the same method as scrape_seq.py, except that data is retrieved sequence by sequence. All sequence data is temporarily saved into seq_info_all.txt and parsed by scrape_info_.sh. Relevant data fields are temporarily stored into seq_info.txt and appended to the final DataFrame, which is saved as an .xlsx file labelled as only NIH data.

3. Construction of IMGT database
HA_ folders contain IMGT results using _seq.fasta files as input. Because IMGT High-V Quest only accepts nucleotide sequences, amino acids sequences are separated into multiple files (since EMBOSS can only reverse translate 500 sequences at once) and reverse translated using EMBOSS. parse_imgt.py files read the existing NIH database, append IMGT data, and save the combined database into .xlsx files labelled as NIH+IMGT.


## To-do

Since sequences are scraped using only three keywords, there might be non-HA sequences present in the database. Further filtering is required.