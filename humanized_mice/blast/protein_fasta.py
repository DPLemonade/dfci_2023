import pandas as pd

input_filename = '2018_August_Flu-mAb_Database.xlsx'
output_filename = 'ha_seq.fasta'

output_file = open(output_filename, 'w')

df = pd.read_excel(input_filename)

df = df[:1438]

seq_data = []
strain_data = []
head_stem_data = []
ha_neutralized_data = []
how_mab_found_data = []

# Remove Influenza B sequences
for i in range(0, len(df)):

    if df['Influenza A/B'][i] == 'B':
        continue

    seq_data.append(df['VH Sequences'][i])
    strain_data.append(df['Strain'][i])
    head_stem_data.append(df['Head/Stem'][i])
    ha_neutralized_data.append(df['HA Neutralized '][i])
    how_mab_found_data.append(df['How mAb found'][i])


seq_data_filtered = []
strain_data_filtered = []
head_stem_data_filtered = []
ha_neutralized_data_filtered = []
how_mab_found_data_filtered = []


seq_data_no_duplicates = []
strain_data_no_duplicates = []
head_stem_data_no_duplicates = []
ha_neutralized_data_no_duplicates = []
how_mab_found_data_no_duplicates = []


# Filter sequences for nan, combine multiple lines into one and remove spaces
for i in range(0, len(seq_data)):

    if (pd.isna(seq_data[i])):
        continue

    try:
        if '\n' in seq_data[i]:
            seq_data[i] = "".join(seq_data[i].split('\n'))
        if ' ' in seq_data[i]:
            seq_data[i] = "".join(seq_data[i].split(' '))
    except:
        print(seq_data[i])

    seq_data_filtered.append(seq_data[i].upper())
    strain_data_filtered.append(strain_data[i])
    head_stem_data_filtered.append(head_stem_data[i])
    ha_neutralized_data_filtered.append(ha_neutralized_data[i])
    how_mab_found_data_filtered.append(how_mab_found_data[i])


# Remove duplicate sequences
for i in range(0, len(seq_data_filtered)):

    has_duplicate = False
    for j in range(0, i):
        if seq_data_filtered[j] == seq_data_filtered[i]:
            has_duplicate = True

    if has_duplicate == False:
        seq_data_no_duplicates.append(seq_data_filtered[i])
        strain_data_no_duplicates.append(strain_data_filtered[i])
        head_stem_data_no_duplicates.append(head_stem_data_filtered[i])
        ha_neutralized_data_no_duplicates.append(ha_neutralized_data_filtered[i])
        how_mab_found_data_no_duplicates.append(how_mab_found_data_filtered[i])

cleaned_df = pd.DataFrame({'Strain': strain_data_no_duplicates, \
                           'Head/Stem': head_stem_data_no_duplicates, \
                           'HA Neutralized': ha_neutralized_data_no_duplicates, \
                           'How mAb found': how_mab_found_data_no_duplicates, \
                            'Sequence': seq_data_no_duplicates})

cleaned_df.to_excel('cleaned_ha_database.xlsx')

for i in range(0, len(seq_data_no_duplicates)):
    print('>', i + 1, file=output_file)
    print(seq_data_no_duplicates[i], file=output_file)

output_file.close()


# Make database
# makeblastdb -in ha_seq.fasta -parse_seqids -blastdb_version 5 -dbtype prot -taxid 9606 -title ha_seq_db
# Database name: /Users/charleschien/Desktop/code/blast/ha_seq.fasta

# .fastq to .fasta
# cat A3_M1_collapse-unique.fastq | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > A3_M1_collapse-unique.fasta

# BLAST
# blastx –db /Users/charleschien/Desktop/code/blast/ha_seq.fasta –query B3_M1_collapse-unique.fasta -out B3_results.txt
# blastn -db ha_seq_nucl_db/ha_seq_nucl.fasta -query B3_fasta_files/B3_000.fasta -out B3_blast_results/B3_000_results.txt
# blastn -db ha_seq_nucl_db/ha_seq_nucl.fasta -query A3_M1_collapse-unique.fasta -out A3_results.txt

# Split .fasta files
# gsplit -a 3 -d -l 100000 A3_M1_collapse-unique.fasta A3_fasta_files/A3_ --additional-suffix=.fasta
