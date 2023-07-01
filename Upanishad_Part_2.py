import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe15/"

# Function to get the text from Kathta-Upanishad
def katha(start,length):
    text_no=[]
    adhyaya=[]
    valli=[]
    hymn=[]
    for i in range(length):
        
        if(i<3):
            adh=str(1)
        else:
            adh=str(2)
            
        val=str(i+1)
        
        
        url=base_url+"sbe"+str(start+i)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
        
        for x in soup.find_all():
        # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
                
        for i in soup.find_all('h3'):
            # to ge only the first h3 tag 
            c=0 
            ans="" #used for storing all the text as a string
            for j in i.next_siblings:
                if j.name=='h3':
        #            print("---------")
                    c=1
                    break
                elif j.name=='p' and (j.text[0]=='p'and j.text[1]=='.') or j.text[0]=='':
                    pass
                elif j.name=='p':
                    text = []
                    for x in j:
                        if isinstance(x, bs4.element.NavigableString):
                            text.append(x.strip())
                    ans=ans+(" ".join(text))
            if c==1:
                break
       #         Removing all the initial numbers fromt the texts 
        lines = re.split(r'\b\d+\.\s*', ans)
        lines = [line.strip() for line in lines if line.strip()]
        
        ct=1
        for line in lines:
            adhyaya.append(adh)
            valli.append(val)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)

    #     Storing all the values into result string
    result="Adhyaya"+"\t"+"Valli"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for ad_n,val_v,text_n,sloka_n in zip(adhyaya,valli,text_no,hymn):
        result+=ad_n+"\t"+val_v+"\t"+text_n+"\t"+sloka_n+"\n"
    
    with open("Upanishad_Part_2_Katha.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Function to get the hymns from Brihadaranyaka 
# Note: 1 Adhyaya 3 brahmana is absent from the website

def Brihadaranyaka(start,length):
    text_no=[]
    adhyaya=[]
    brahmana=[]
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
    "FIFTEENTH": 15
            }
    adh=str(1)
    brih=str(1)
    for i in range(length):
        
        
        url=base_url+"sbe"+str(start+i)+".htm"
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
                
        if(i==45):
            continue
        #removing the translation by hume as the similar translation is already present 
        else:
            if(soup.find_all('h2')):
                texts=soup.find('h2').text
                match = re.search(r'\b([A-Z]+)\b', texts)

                if match:
                    top1 = match.group(1)
                else:
                    top1 = ""
                adh=str(number[top1])
        for i in soup.find_all('h3'):
        # to ge only the first h3 tag 
            texts=i.text
            match = re.search(r'\b([A-Z]+)\b', texts)

            if match:
                top = match.group(1)
            else:
                top = ""
            brih=str(number[top])
        
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
            brahmana.append(brih)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Adhyaya"+"\t"+"Brahmana"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for ad_n,brah_v,text_n,sloka_n in zip(adhyaya,brahmana,text_no,hymn):
        result+=ad_n+"\t"+brah_v+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("Upanishad_Part_2_Brihdaranyaka.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)

# Maitrayan upanishad
def Maitrayan(start,length):
    text_no=[]
    prapathaka=[]
    hymn=[]
    for i in range(length):
        prapa=str(i+1)
        url=base_url+"sbe"+str(start+i)+".htm"
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
        ans=""
#         print(soup)
        for i in soup.find_all('h3'):
        # to ge only the first h3 tag 
        
            c=0 
            
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
            if ("Footnotes" in line):
                newline = ''
                for word in line.split(" "):
                    if not ("Footnotes" in word):
                        #print(word)
                        newline += word + " "
                    else:
                        break
                #print(newline)
                prapathaka.append(prapa)
                text_no.append(str(ct))
                hymn.append(newline)
                break
            #print(line)
            prapathaka.append(prapa)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Prapathaka"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for pr_n,text_n,sloka_n in zip(prapathaka,text_no,hymn):
        result+=pr_n+"\t"+text_n+"\t"+sloka_n+"\n"
        
    #print(result)    
    with open("Upanishad_Part_2_Maitrayan.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)

# Function to get the hymns from Mundaka Upanishad
def Mundaka(start,length):
    text_no=[]
    mundaka=[]
    khanda=[]
    hymn=[]
    y=1
    for i in range(length):
        
        if((y-1)%2==0):
            y=1
        if(i<2):
            mun_n = str(1)
        elif(i<4):
            mun_n = str(2)
        else:
            mun_n=str(3)
            
        khan_n = str(y)
        y+=1
        
        
        
        url=base_url+"sbe"+str(start+i)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
        
        for x in soup.find_all():
  
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:

                # Remove empty tag
                x.extract()

        for i in soup.find_all('h3'):
            c=0 # to ge only the first h3 tag 
            ans=""
            for j in i.next_siblings:
                if j.name=='h3':
        #            print("---------")
                    c=1
                    break
                elif j.name=='p' and (j.text[0]=='p'and j.text[1]=='.') or j.text[0]=='':
                    pass
                elif j.name=='p':
                    text = []
                    for x in j:
                        if isinstance(x, bs4.element.NavigableString):
                            text.append(x.strip())
                    ans=ans+(" ".join(text))
            if c==1:
                break
        lines = re.split(r'\b\d+\.\s*', ans)
        lines = [line.strip() for line in lines if line.strip()]
        
        ct=1
        for line in lines:

            mundaka.append(mun_n)
            khanda.append(khan_n)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)

    result="Mundaka"+"\t"+"Khanda"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for mun_n,khan_n,text_n,sloka_n in zip(mundaka,khanda,text_no,hymn):
        result+=mun_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
    

    with open("Upanishad_Part_2_mundaka.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)

#  Taittiriyaka Upanishad
def Taittiriyaka(start,length):
    text_no=[]
    anuvaka=[]
    vallis=[]
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
    "FIFTEENTH": 15
            }
    valli=str(1)
    anuv=str(1)
    for i in range(length):
        
        
        url=base_url+"sbe"+str(start+i)+".htm"
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
                
        if(soup.find_all('h2')):
            texts=soup.find('h2').text
            match = re.search(r'\b([A-Z]+)\b', texts)

            if match:
                top1 = match.group(1)
            else:
                top1 = ""
            valli=str(number[top1])
        for i in soup.find_all('h3'):
        # to ge only the first h3 tag 
            texts=i.text
            match = re.search(r'\b([A-Z]+)\b', texts)

            if match:
                top = match.group(1)
            else:
                top = ""
            anuv=str(number[top])
        
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
            anuvaka.append(anuv)
            vallis.append(valli)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Valli"+"\t"+"Anuvaka"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for valli_n,anuv_v,text_n,sloka_n in zip(vallis,anuvaka,text_no,hymn):
        result+=valli_n+"\t"+anuv_v+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("Upanishad_Part_2_Taittiriyaka.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Svetasvatara upanishad
def Svetasvatara(start,length):
    text_no=[]
    adhyaya=[]
    hymn=[]
    for i in range(length):
        adh=str(i+1)
        url=base_url+"sbe"+str(start+i)+".htm"
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
            adhyaya.append(adh)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Adhyaya"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for ad_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=ad_n+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("Upanishad_Part_2_Svetasvatara.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
        
# Prasana upanishad
def Prasna(start,length):
    text_no=[]
    question=[]
    hymn=[]
    for i in range(length):
        ques=str(i+1)
        url=base_url+"sbe"+str(start+i)+".htm"
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
            question.append(ques)
            text_no.append(str(ct))
            ct+=1
            hymn.append(line)
        #     Storing all the values into result string
    result="Question"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for qu_n,text_n,sloka_n in zip(question,text_no,hymn):
        result+=qu_n+"\t"+text_n+"\t"+sloka_n+"\n"
        
        
    with open("Upanishad_Part_2_Prasana.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
        
    



index_url=base_url+"index.htm"
req = requests.get(index_url)
req.encoding = 'utf-8'
soup=bs4.BeautifulSoup(req.text,'html.parser')
upanishad=[]
for i in soup.find_all('h3')[3:]:
    count=0
    for j in i.next_siblings:
        if j.name=='h3':
            break
        elif j.name=='a' and len(j.text)>0 :
            count=count+1
    upanishad.append(count)
    
no=15010  #storing the number of the first link 
for i in tqdm(range(7)):
    x=i+1
    if(x==1):
        katha(no,upanishad[i])
        no+=upanishad[i]
    if(x==2):
        Mundaka(no,upanishad[i])
        no+=upanishad[i]
    elif(x==3):
        Taittiriyaka(no,upanishad[i])
        no+=upanishad[i]
    elif(x==4):
        Brihadaranyaka(no,upanishad[i])
        no+=upanishad[i]
    elif(x==5):
        Svetasvatara(no,upanishad[i])
        no+=upanishad[i]
    elif(x==6):
        Prasna(no,upanishad[i])
        no+=upanishad[i]
    elif(x==7):
        Maitrayan(no,upanishad[i])
        no+=upanishad[i]
    
            
    

























