import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/wyv/wyvbk"
books=40
texts=""
adhyaya=[]
current_adhyaya=0
text_no=[]
hymn=[]

for i in range(books):
    text=""
    url=base_url+str(i+1).zfill(2)+".htm"
    req = requests.get(url)
    req.encoding = 'utf-8'
    soup=bs4.BeautifulSoup(req.text,'html.parser')
    for a_tag in soup.find_all('a'):
            a_tag.decompose()
    for x in soup.find_all():
# fetching text from tag and remove whitespaces
        if len(x.get_text(strip=True)) == 0:
            # Remove empty tag
            x.extract()
    p_tags=soup.find_all('p')
    for p in p_tags[1:]:
        text=text+p.text
    numbered_texts = re.split(r'(?<=\d)[ .]', text)
    
    numbered_texts = [(str(i+1), text.strip()) for i, text in enumerate(numbered_texts) if text.strip()]
    text_no.extend([number for number, _ in numbered_texts])
    hymn.extend([text for _, text in numbered_texts])
    
for num in text_no:
    if num == '1':
        current_adhyaya += 1
        adhyaya.append(str(current_adhyaya))
        
    else:
        adhyaya.append(str(current_adhyaya))

result="Books"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
    result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


with open("White_Yajur_Veda.tsv", "w", encoding='utf-8') as outfile:
    outfile.write(result)