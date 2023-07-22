import requests
import time
import subprocess
from bs4 import BeautifulSoup
import pandas as pd
from Bio import SeqIO

db = 'protein'
query = 'influenza+AND+antibody+AND+human[orgn]'
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
url = base + f'esearch.fcgi?db={db}&term={query}&usehistory=y&retmax=20'

page = requests.get(url)
#print(page.text)
#print('********')

soup = BeautifulSoup(page.text, "xml")
results = soup.find_all('Id')

web = soup.find('WebEnv').text
key = soup.find('QueryKey').text
count = soup.find('Count').text

#print(web)
#print(count)
#print(key)

retmax = 1
retstart = 0

date = []
description = []
authors = []
journal = []
pubmed = []
seq_ids = []
sequences = []


while retstart < int(count):
    if retstart % 10 == 0:
        print(retstart)
    time.sleep(0.05)
    fetch_url = base + f'efetch.fcgi?db={db}&WebEnv={web}'
    fetch_url += f'&query_key={key}&retstart={retstart}'
    fetch_url += f'&retmax={retmax}&rettype=gp&retmode=text'
    page = requests.get(fetch_url)

    output_file = open('seq_info_all.txt', 'w')
    print(page.text, file=output_file)
    output_file.close()

    retstart += retmax

    subprocess.call('./scrape_info_prot.sh', shell=True)

    input_file = open('seq_info.txt', 'r')
    lines = input_file.readlines()

    try:
        date.append(lines[0])
    except:
        date.append('NA')
    
    try:
        description.append(lines[1])
    except:
        description.append('NA')

    try:
        authors.append(lines[2])
    except:
        authors.append('NA')
    
    try:
        journal.append(lines[3])
    except:
        journal.append('NA')

    try:
        pubmed.append(lines[4])
    except:
        pubmed.append('NA')


for seq_record in SeqIO.parse("prot_seq.fasta", "fasta"):
    sequences.append(str(seq_record.seq))

id_file = open('prot_id_file.txt', 'r')
for id in id_file:
    seq_ids.append(id)

dict = {'Date': date, 'Description': description, 'Authors': authors, 'Journal': journal, 'PubMed ID': pubmed, 'Protein ID': seq_ids, 'Sequence': sequences}
df = pd.DataFrame(dict)
df.to_excel('Protein HA Database Updated.xlsx')