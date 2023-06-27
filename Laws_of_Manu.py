import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/manu/manu"

chapters=11
text=""
adhyaya=[]
current_adhyaya=0
for i in range(chapters):
    url=base_url+str(i+1).zfill(2)+".htm"
    req = requests.get(url)
    req.encoding = 'utf-8'
    soup=bs4.BeautifulSoup(req.text,'html.parser')
    p_tags=soup.find_all('p')
    
    for p in p_tags:
        text+=p.text
        
text_no = re.findall(r'\d+\.', text)
text_no = [num.strip('.') for num in text_no]
hymn = re.split(r'\d+\.', text)
hymn = [text.strip() for text in hymn if text.strip()]
for num in text_no:
    if num == '1':
        current_adhyaya += 1
        adhyaya.append(str(current_adhyaya))
        
    else:
        adhyaya.append(str(current_adhyaya))

result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
    result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


with open("Laws_of_Manu.tsv", "w", encoding='utf-8') as outfile:
    outfile.write(result)


