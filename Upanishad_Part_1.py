import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe01/"


# Kaushitaki upanishad
def kaushitaki(start,length):
    text_no=[]
    adhyaya=[]
    hymn=[]
    for i in range(length):
        adh=str(i+1)
        url=base_url+"sbe"+str(start+i).zfill(5)+".htm"
        print(url)
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
        print(soup)
        for i in soup.find_all('h2'):
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
        lines = re.split(r'\b\d+\.\s*', ans)
        lines = [line.strip() for line in lines if line.strip()]
        
        ct=1
        for line in lines:
            adhyaya.append(adh)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Adhyaya"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("kaushutaki.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
        

# Talavakra upanishad
def Talavakra(start,length):
    text_no=[]
    khanda=[]
    hymn=[]
    for i in range(length):
        khan=str(i+1)
        url=base_url+"sbe"+str(start+i).zfill(5)+".htm"
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
        lines = re.split(r'\b\d+\.\s*', ans)
        lines = [line.strip() for line in lines if line.strip()]
        
        ct=1
        for line in lines:
            khanda.append(khan)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Khanda"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for khan_n,text_n,sloka_n in zip(khanda,text_no,hymn):
        result+=khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("Talavakra.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
        
#  Khandogya Upanishad 

def khandogya(start,length):
    text_no=[]
    prapathaka=[]
    khanda=[]
    hymn=[]
   
    #     mapping english to their corresponding numbers
    number = {
    "FIRST": 1,
    "SECOND": 2,
    "THIRD": 3,
    "FOURTH": 4,
    "FIFTH": 5,
    "SIXTH": 6,
    "SEVENTH": 7,
    "EIGHTH": 8,
    "NINTH": 9,
    "TENTH": 10,
    "ELEVENTH": 11,
    "TWELFTH": 12,
    "THIRTEENTH": 13,
    "FOURTEENTH": 14,
    "FIFTEENTH": 15,
    "SIXTEENTH": 16,
    "SEVENTEENTH": 17,
    "EIGHTEENTH": 18,
    "NINETEENTH": 19,
    "TWENTIETH": 20,
#     "TWENTY": 20,
    "TWENTY-FIRST": 21,
    "TWENTY-SECOND": 22,
    "TWENTY-THIRD": 23,
    "TWENTY-FOURTH": 24,
    "TWENTY-FIFTH": 25,
    "TWENTY-SIXTH": 26,
    "TWENTY-SEVENTH": 27,
    "TWENTY-EIGHTH": 28,
    "TWENTY-NINTH": 29,
    "THIRTIETH": 30
            }
    
    prap=str(1)
    khan=str(1)
    for i in range(length):
#         no=start+1.zfill(5)
        url=base_url+"sbe"+str(start+i).zfill(5)+".htm"
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
        print(soup)

        if(soup.find_all('h2')):
            texts=soup.find('h2').text
#             print(text)
            match = re.search(r'\b([A-Z]+)\b', texts)

            if match:
                top1 = match.group(1)
            else:
                top1 = ""
            prap=str(number[top1])
       
        for i in soup.find_all('h3'):
        # to ge only the first h3 tag 
            texts=i.text
            match = re.search(r'\b([A-Z-]+)\b', texts)

            if match:
                top = match.group(1)
            else:
                top = ""
            khan=str(number[top])
        
            c=0 
            ans=""
            for j in i.next_siblings:
                if j.name=='h3':
                    c=1
                    break

                elif j.name=='p':
#                     print(j.text)
                    ans+=j.text       
            

            if c==1:
                break
            print(ans)
#  Splitting the ans into lines by a number followed by a "." literal
        lines = re.split(r'\b\d+\.\s*', ans)
        lines = [line.strip() for line in lines if line.strip()]
        
        ct=1
    
        for line in lines:
            prapathaka.append(prap)
            khanda.append(khan)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
#             Storing all the values into result string
    result="Prapthaka"+"\t"+"Khanda"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for prap_n,khan_v,text_n,sloka_n in zip(prapathaka,khanda,text_no,hymn):
        result+=prap_n+"\t"+khan_v+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("khandogya.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)

    
    

























index_url=base_url+"index.htm"
req = requests.get(index_url)
req.encoding = 'utf-8'
soup=bs4.BeautifulSoup(req.text,'html.parser')
upanishad=[]
for i in soup.find_all('h3')[1:]:
    count=0
    for j in i.next_siblings:
        if j.name=='h3':
#            print("---------")
            break
        elif j.name=='a' and len(j.text)>0 :
#              print(j)
            count=count+1
    upanishad.append(count)
    
no=1022  #storing the number of the first link 

for i in range(4):
    x=i+1
    if(x==1):
        khandogya(no,upanishad[i])
        no+=upanishad[i]
    if(x==2):
        Talavakra(no,upanishad[i])
        no+=upanishad[i]
    elif(x==3):
        Aitareya(no,upanishad[i])
        no+=upanishad[i]
    elif(x==4):
        kaushitaki(no,upanishad[i])
        no+=upanishad[i]

    

























