import pandas as pd

df = pd.read_excel('Protein HA Database Updated.xlsx')
# Remove first column (Unnamed:0)
df.drop(columns=df.columns[0], axis=1, inplace=True)

data = pd.read_csv('HA_prot_1/1_Summary.txt', sep="\t", header=None)
# Remove column NaN
data.drop(columns=data.columns[-1], axis=1, inplace=True)
# Set first row as column names and remove first row
data.columns = pd.Series.to_list(data.loc[0])
data.drop(index=data.index[0], axis=0, inplace=True)
data = data.reset_index(drop=True)

# Append remaining IMGT results
for i in range(2, 7):
    new_data = pd.read_csv(f'HA_prot_{i}/1_Summary.txt', sep="\t", header=None)
    # Remove column NaN
    new_data.drop(columns=new_data.columns[-1], axis=1, inplace=True)
    # Set first row as column names and remove first row
    new_data.columns = pd.Series.to_list(new_data.loc[0])
    new_data.drop(index=new_data.index[0], axis=0, inplace=True)
    new_data = new_data.reset_index(drop=True)
    data = data.append(new_data, ignore_index=True)

# Remove column Sequence ID
data.drop(columns=data.columns[1], axis=1, inplace=True)
# Remove column Sequence number
data.drop(columns=data.columns[0], axis=1, inplace=True)

result = pd.concat([df, data], axis=1)
result['Protein ID'] = result['Protein ID'].astype(str)
result.to_excel('Protein HA Database Combined.xlsx')