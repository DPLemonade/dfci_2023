import requests
import time
from bs4 import BeautifulSoup

db = 'protein'
query = 'influenza+AND+antibody+AND+human[orgn]'
base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
url = base + f'esearch.fcgi?db={db}&term={query}&usehistory=y&retmax=20'

id_file = open('nucl_id_file.txt', 'w')
seq_file = open('nucl_seq.fasta', 'w')

page = requests.get(url)
#print(page.text)
#print('********')

soup = BeautifulSoup(page.text, "xml")
results = soup.find_all('Id')

for id in results:
    print(id.text, file=id_file)

web = soup.find('WebEnv').text
key = soup.find('QueryKey').text
count = soup.find('Count').text

#print(web)
#print(count)
#print(key)

retmax = 500
retstart = 0

while retstart < int(count):
    print(retstart)
    time.sleep(1)
    fetch_url = base + f'efetch.fcgi?db={db}&WebEnv={web}'
    fetch_url += f'&query_key={key}&retstart={retstart}'
    fetch_url += f'&retmax={retmax}&rettype=fasta&retmode=text'
    page = requests.get(fetch_url)

    print(page.text, file=seq_file)
    retstart += retmax

id_file.close()
seq_file.close()