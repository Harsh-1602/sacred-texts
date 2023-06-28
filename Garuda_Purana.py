# Some anomalies in the last chapter(16) due the I in brahma is represented as 1, text no prev to 108

import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/gpu/gpu"

chapters=16
texts=""
adhyaya=[]
current_adhyaya=0
text_no=[]
hymn=[]
for i in range(chapters):
    text=""
    url=base_url+str(i+3).zfill(2)+".htm"
    req = requests.get(url)
    req.encoding = 'utf-8'
    soup=bs4.BeautifulSoup(req.text,'html.parser')
#     print(soup)
    for a_tag in soup.find_all('a'):
            a_tag.decompose()
    for x in soup.find_all():
# fetching text from tag and remove whitespaces
        if len(x.get_text(strip=True)) == 0:
            # Remove empty tag
            x.extract()
    for i in soup.find_all('h3'):
        # to ge only the first h3 tag 
        c=0 
        ans=""
        for j in i.next_siblings:
            if j.name=='h3':
                c=1
                break

            elif j.name=='p':
                ans+=j.text

        if c==1:
            break

    numbers = re.findall(r'\d+(?:-\d+)?', ans)
    numbers = [num.rstrip('.,:') for num in numbers]
    texts = re.split(r'\d+(?:-\d+)?\.?\s?', ans)
    texts = [t.strip() for t in texts if t.strip()]
#     print(str(len(texts))+"  "+str(len(numbers)))
    for num in numbers:
        text_no.append(str(num))
        if (num == '1'and current_adhyaya!='15') or (num[0]=='1' and num[1]=='-'):
            current_adhyaya += 1
            adhyaya.append(str(current_adhyaya))

        else:
            adhyaya.append(str(current_adhyaya))
    for text in texts:
        hymn.append(text)

result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
    result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


with open("Garuda_Purana.tsv", "w", encoding='utf-8') as outfile:
    outfile.write(result)