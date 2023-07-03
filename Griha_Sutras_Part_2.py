import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe30/sbe30"


# Gobhila
# Chapter 26 missing abnormalities not found
def gobhila(start,end):
    texts=""
    khanda=[]
    adhyaya=[]
    text_no=[]
    hymn=[]
    prev_adh=""
    
    for link in range(start,end):
        url=base_url+str(link).zfill(3)+".htm"
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
        adh = None
        khan = None
        h_tags=[]

        h_tags=soup.find_all('h3')
        for i in h_tags:
            print(i.text)
            info=i.text
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

        match_adh = re.search(r'PRAPÂTHAKA\s([\w\d]+)', info,re.IGNORECASE)
        match_khan = re.search(r'KÂNDIKÂ\.?\s+(\w+)', info,re.IGNORECASE)
        # Store the extracted values in variables
        adh = match_adh.group(1) if match_adh else prev_adh
        khan = match_khan.group(1) if match_khan else None
        
        #converting roman to number
        if adh=='I':
            adh='1'
        elif adh=='II':
            adh='2'
        elif adh=='III':
            adh='3'
        elif adh=='IV':
            adh='4'
        elif adh=='V':
            adh='5'
        elif adh=='VI':
            adh='6'
        prev_adh=adh
        
        if link==8:
            khan='5'
        
        print(adh)
        print(khan)
        if link ==26:
            parts = ans.split("Footnotes")
            # Retrieve the first part of the split string
            ans = parts[0].strip()
            
        ans=ans.replace("Sûtras 15-19.","") # Prapthaka 1 and kandika 4  
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
#  Spliitng the text into two list of numbers and hymns 
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
                adhyaya.append(adh)
                khanda.append(khan)
                
        else:
            print("numbers and hymns and numbers do not match at Adhyaya:"+str(adh)+"Khanda"+str(khan))
            print(ans)
            
            
        result="Prapathaka"+"\t"+"Kandika_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,khan_n,text_n,sloka_n in zip(adhyaya,khanda,text_no,hymn):
            result+=prs_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_2_Gobhila.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Apastaba
def apastamba(start,end):
    texts=""
    khanda=[]
    adhyaya=[]
    text_no=[]
    hymn=[]
    prev_adh=""
    
    for link in range(start,end):
        url=base_url+str(link).zfill(3)+".htm"
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
        adh = None
        khan = None
        h_tags=[]

        h_tags=soup.find_all('h3')
        for i in h_tags:
            print(i.text)
            info=i.text
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

        match_adh = re.search(r'PATALA\s([\w\d]+)', info,re.IGNORECASE)
        match_khan = re.search(r'SECTION\.?\s+(\w+)', info,re.IGNORECASE)
        # Store the extracted values in variables
        adh = match_adh.group(1) if match_adh else prev_adh
        khan = match_khan.group(1) if match_khan else None
        
        #converting roman to number
        if adh=='I':
            adh='1'
        elif adh=='II':
            adh='2'
        elif adh=='III':
            adh='3'
        elif adh=='IV':
            adh='4'
        elif adh=='V':
            adh='5'
        elif adh=='VI':
            adh='6'
        prev_adh=adh
        
        if link==8:
            khan='5'
        
        print(adh)
        print(khan)
#         if link ==26:
#             parts = ans.split("Footnotes")
#             # Retrieve the first part of the split string
#             ans = parts[0].strip()
            
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
#  Spliitng the text into two list of numbers and hymns 
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
                adhyaya.append(adh)
                khanda.append(khan)
                
        else:
            print("numbers and hymns and numbers do not match at Adhyaya:"+str(adh)+"Khanda"+str(khan))
            print(ans)
            
            
        result="Patala_no"+"\t"+"Section_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,khan_n,text_n,sloka_n in zip(adhyaya,khanda,text_no,hymn):
            result+=prs_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_2_Apastamba.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# hirayakesin
def hiranyakesin(start,end):
    texts=""
    kandika=[]
    prasna=[]
    adhyaya=[]
    text_no=[]
    hymn=[]
    prev_pras=""
    for link in range(start,end):
        url=base_url+str(link).zfill(3)+".htm"
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
        pras = None
        pat = None
        khan = None
        h_tags=[]
        
        h_tags=soup.find_all('h3')
        for i in h_tags:
            print(i.text)
            info=i.text
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
        print(info)
#         Geeting the values of Prasna , Patala ,Khanda from the H3 tag
        match_pras = re.search(r'PRASNA\s(\w+)', info,re.IGNORECASE)
        match_adh = re.search(r'PATALA\s(\d+)', info,re.IGNORECASE)
        match_kand = re.search(r'SECTION\s(\d+)', info,re.IGNORECASE)

        # Store the extracted values in variables
        pras = match_pras.group(1) if match_pras else prev_pras
        adh= match_adh.group(1) if match_adh else None
        kand = match_kand.group(1) if match_kand else None
        
        print(pras,adh,kand)
        prev_pras=pras
        
        #converting roman to number
        if pras=='I':
            pras='1'
        elif pras=='II':
            pras='2'
        elif pras=='III':
            pras='3'
        elif pras=='IV':
            pras='4'
#             Handling for the chapter with so many numbers i.e removing it
        if pras=='1' and adh=='11' and kand=='20':
            continue
          
        
        ans=ans.replace(" Pâraskara I, 16, 2.)","") # prasna II patala 1 and Seciton 3    
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans=ans.replace("8. See above, I, 1, 3, 5; I, 1, 4, 1.","")# Prasna 1 PATAL 6 SECTION 19
#  Spliitng the text into two list of numbers and hymns 
        numbers = re.findall(r'(?<!\()\d+(?:-\d+)?(?!\))', ans)
        numbers = [num.rstrip('.,:') for num in numbers]

        # Replace numbers enclosed in parentheses with placeholders
        text_with_placeholders = re.sub(r'\(\d+\)', lambda m: '({})'.format(len(m.group())), ans)

        # Split the text using the modified numbers
        texts = re.split(r'(?<!\()\d+(?:-\d+)?\.?\s?', text_with_placeholders)
        texts = [t.strip() for t in texts if t.strip()]

        # Replace the placeholders back with the original numbers
        numbers = [re.sub(r'\((\d+)\)', r'\1', num) for num in numbers]
#         Handling for the missing text number in prasna 3 , adhyaya 1
#         if pras=='3' and adh=='1' and kand=='-':
#             numbers.insert(0,1)
        
        if len(numbers)==len(texts):
            for x in range(len(numbers)):
                text_no.append(str(numbers[x]));
                hymn.append(texts[x])
                prasna.append(pras)
                kandika.append(kand)
                adhyaya.append(adh)
                
        else:
            print("numbers and hymns and numbers do not match at PRASNA:"+str(pras)+" Patala:"+str(adh)+" SEction:"+str(kand))
            print(ans)
            
            
        result="Pransa_no"+"\t"+"PATALA_no"+"\t"+"Section_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,pat_n,khan_n,text_n,sloka_n in zip(prasna,adhyaya,kandika,text_no,hymn):
            result+=prs_n+"\t"+pat_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_2_HIranyakesin.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)


# Driver code
start_gob=4
end_gob=43
gobhila(start_gob,end_gob)

start_apas=94
end_apas=117
apastamba(start_apas,end_apas)
start_hira=44
end_hira=93
hiranyakesin(start_hira,end_hira)
# start_khad=208
# end_khad=227
# khadira(start_khad,end_khad)
