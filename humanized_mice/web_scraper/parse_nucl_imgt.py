import pandas as pd

df = pd.read_excel('Nucleotide HA Database (only NIH data).xlsx')
# Remove first column (Unnamed:0)
df.drop(columns=df.columns[0], axis=1, inplace=True)

data = pd.read_csv('HA_nucl/1_Summary.txt', sep="\t", header=None)
# Remove column NaN
data.drop(columns=data.columns[-1], axis=1, inplace=True)
# Remove column Sequence ID
data.drop(columns=data.columns[1], axis=1, inplace=True)
# Remove column Sequence number
data.drop(columns=data.columns[0], axis=1, inplace=True)
# Set first row as column names and remove first row
data.columns = pd.Series.to_list(data.loc[0])
data.drop(index=data.index[0], axis=0, inplace=True)
data = data.reset_index(drop=True)

result = pd.concat([df, data], axis=1)
result['Nucleotide ID'] = result['Nucleotide ID'].astype(str)
result.to_excel('Nucleotide HA Database (NIH+IMGT).xlsx')