# Importing required Libraries

import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe29/sbe29"

# Sankhayana
# Adhyaya 6 khanda 5 missing due to some overlapping with adhyaya 6 khanda 4
def sankhayana(start,end):
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
#         Geeting the values of Prasna , Patala ,Khanda from the H3 tag
        match_adh = re.search(r'ADHYÂYA\s([\w\d]+)', info,re.IGNORECASE)
        match_khan = re.search(r'KHANDA\s(\d+)', info,re.IGNORECASE)

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
        
        if link==3:
            khan='1'
        elif link==68:
            khan='6'
        
        print(adh)
        print(khan)
            
            
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans=ans.replace("Comp. Âsvalâyana-Sraut. I, 12, 4.}","") #Adhyaya 1,khanda 7
        ans=ans.replace("10, 1","")# Adhyaya 2, Khanda 9
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
            
            
        result="Adhyaya_no"+"\t"+"Khanda_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,khan_n,text_n,sloka_n in zip(adhyaya,khanda,text_no,hymn):
            result+=prs_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_1_Sankhayana.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Asvalayana

def asvalayana(start,end):
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
#         Geeting the values of Prasna , Patala ,Khanda from the H3 tag
        match_adh = re.search(r'ADHYÂYA\s([\w\d]+)', info,re.IGNORECASE)
        match_khan = re.search(r'KANDIKÂ\s(\d+)', info,re.IGNORECASE)

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
        
        if link==101:
            khan='2'
        
        print(adh)
        print(khan)
            
            
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
            
            
        result="Adhyaya_no"+"\t"+"Kandika_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,khan_n,text_n,sloka_n in zip(adhyaya,khanda,text_no,hymn):
            result+=prs_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_1_Asvalayana.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Paraskara
def paraskara(start,end):
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
#         Geeting the values of Prasna , Patala ,Khanda from the H3 tag
        match_adh = re.search(r'KÂNDA\s([\w\d]+)', info,re.IGNORECASE)
        match_khan = re.search(r'KÂNDA\s(\d+)', info,re.IGNORECASE)
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
        
        if link==101:
            khan='2'
        
        print(adh)
        print(khan)
            
            
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
            
            
        result="Kanda_no"+"\t"+"Kandika_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,khan_n,text_n,sloka_n in zip(adhyaya,khanda,text_no,hymn):
            result+=prs_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_1_Paraskara.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Khadira

def khadira(start,end):
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
# removing the text with size as -1
        for font_tag in soup.find_all('font', size='-1'):
            font_tag.decompose()
        
        
        adh = None
        khan = None
        h_tags=[]
        if link==211:
            h_tags=soup.find_all('h4')
            info =i.text
            print(i.text)
            print("here")
        else:
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
        
#         Geeting the values of Prasna , Patala ,Khanda from the H3 tag
        match_adh = re.search(r'PATALA\s([\w\d]+)', info,re.IGNORECASE)
        match_khan = re.search(r'KHANDA\s(\d+)', info,re.IGNORECASE)

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
        
        if link==3:
            khan='1'
        elif link==68:
            khan='6'
        
        print(adh)
        print(khan)
            
            
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
            
            
        result="Patala_no"+"\t"+"Khanda_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,khan_n,text_n,sloka_n in zip(adhyaya,khanda,text_no,hymn):
            result+=prs_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Griha_Sutras_Part_1_Khadira.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)


start_sank=3
end_sank=99
sankhayana(start_sank,end_sank)

start_asva=100
end_asva=154
asvalayana(start_asva,end_asva)
start_para=155
end_para=207
paraskara(start_para,end_para)
start_khad=208
end_khad=227
khadira(start_khad,end_khad)