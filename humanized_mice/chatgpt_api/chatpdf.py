'''import requests

headers = {
  'x-api-key': 'sec_xIxkuUOQkGmQf76rhiGddKh7LBKv2o02',
  'Content-Type': 'application/json'
}
#data = {'url': 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10266979/pdf/41586_2023_Article_6136.pdf'}
#data = {'url': 'https://www.science.org/doi/epdf/10.1126/scitranslmed.ade4976'}
data = {'url': 'https://arxiv.org/pdf/1706.03762.pdf'}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-url', headers=headers, json=data)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)

exit(0)'''

'''import requests

files = [
    ('file', ('file', open('paper_2.pdf', 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': 'sec_xIxkuUOQkGmQf76rhiGddKh7LBKv2o02'
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)'''

import requests

headers = {
    'x-api-key': 'sec_xIxkuUOQkGmQf76rhiGddKh7LBKv2o02',
    "Content-Type": "application/json",
}

data = {
    'sourceId': "src_vRsesMnfQwVLOxaQCXxy2",
    'messages': [
        {
            'role': "user",
            'content': "Are there any antibody sequences mentioned in the paper?",
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)