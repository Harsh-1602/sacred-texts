#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.wisdomlib.org/hinduism/book/ashtavakra-gita/d/doc"


# In[26]:



chap=1
start=81439
end=81459
chapter=[]
text_no=[]
hymn=[]
for link in range(start,end):
    ans=""
    texts=""
    url=base_url+str(link)+".html"
    print(url)
    req = requests.get(url)
    req.encoding = 'utf-8'
    soup=bs4.BeautifulSoup(req.text,'html.parser')
    p_tags=soup.find_all(lambda tag: tag.name == 'p' and tag.find('span', id=True)) 
#     print(p_tags)
    for p in p_tags:
        ans+=p.text
    
    numbers = re.findall(r'(?<!\()\d+(?:-\d+)?(?!\))', ans)
    numbers = [num.rstrip('.,:') for num in numbers]

    # Replace numbers enclosed in parentheses with placeholders
    text_with_placeholders = re.sub(r'\(\d+\)', lambda m: '({})'.format(len(m.group())), ans)

    # Split the text using the modified numbers
    texts = re.split(r'(?<!\()\d+(?:-\d+)?\.?\s?', text_with_placeholders)
    texts = [t.strip() for t in texts if t.strip()]

    # Replace the placeholders back with the original numbers
    numbers = [re.sub(r'\((\d+)\)', r'\1', num) for num in numbers]
    
    if len(numbers)==len(texts):
        for x in range(len(numbers)):
            text_no.append(str(numbers[x]));
            hymn.append(texts[x])
            chapter.append(str(chap))
    else:
        prinf("ERROR")
    if link==81456:
        hy=[]
        p_tag=soup.find_all('p')[6:]
        for p in p_tag:
            x=p.text
            res=re.search(r'18\.(.*)', x)
            if res:
                num=re.search(r'18\.(.*)', x).group(1).strip()
                text_no.append(str(num))
                hy.append(re.sub(r'18(\.\d+)?', '', x))
                chapter.append(str(chap))
            else: pass
        hy = [item.replace('\n', '') for item in hy]
        for h in hy:
            hymn.append(h)

            
        
    chap+=1
result="Chapter_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
for adh_n,text_n,sloka_n in zip(chapter,text_no,hymn):
    result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"
with open("Ashtavakra_Gita.tsv", "w", encoding='utf-8') as outfile:
    outfile.write(result)


# In[ ]:




