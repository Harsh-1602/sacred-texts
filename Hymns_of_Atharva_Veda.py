import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/av/"

def get_hymn(hymn_no, result):
    no = [str(i) for i in range(20)]
    hymn_url=base_url+"av"+(hymn_no)+".htm"
    r=requests.get(hymn_url)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    p_tags=soup.find_all('p')[-2]
    
    text_no=""
    sloka=""
    for p in p_tags:
        text=(p.text)
        text=re.sub("\s\s+" , " ", text)
#         print(text)
        if(p.text.isdigit()):
            text_no=text_no+str(hymn_no)+"."+text+"\n"
            sloka=sloka+"\n"
        elif(len(text)==0 or (text[0]=='p' and text[1]==".")):
            pass
        else:
             sloka=sloka+text
#     print(sloka)   
    text_lines = text_no.split('<br/>')
    text_lines = text_lines[0].split('\n')
    sloka_lines=sloka.split('<br/>')
    sloka_lines = sloka_lines[0].split('\n')[1:]
    for text_n,sloka_n in zip(text_lines,sloka_lines):
        result+=text_n+"\t"+sloka_n+"\n"
        
    return result
        

result = ""
for i in range(1,21):
    url_book=base_url+"avbook"+str(i).zfill(2)+".htm"
    req = requests.get(url_book)
    req.encoding = 'utf-8'
    soup=bs4.BeautifulSoup(req.text,'html.parser')
    hymn=soup.find_all('br')
    # print(len(hymn)-2)
    length=len(hymn) - 2
    if(i==20):
        length=142
    for hymn_no in tqdm(range(length)):
        first_hymn=str(i*1000+hymn_no+1).zfill(5)
        result = get_hymn(first_hymn, result)
        
with open("Atharva_Veda.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)