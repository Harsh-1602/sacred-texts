# Importing required Libraries
import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe02/sbe02"


# Gautama
# Function to convert roman to decimal
def convert_roman_to_decimal(roman_numeral):
    roman_to_decimal = {
        'I': '1',
        'II': '2',
        'III': '3',
        'IV': '4',
        'V': '5',
        'VI': '6',
        'VII': '7',
        'VIII': '8',
        'IX': '9',
        'X': '10',
        'XI': '11',
        'XII': '12',
        'XIII': '13',
        'XIV': '14',
        'XV': '15',
        'XVI': '16',
        'XVII': '17',
        'XVIII': '18',
        'XIX': '19',
        'XX': '20',
        'XXI': '21',
        'XXII': '22',
        'XXIII': '23',
        'XXIV': '24',
        'XXV': '25',
        'XXVI': '26',
        'XXVII': '27',
        'XXVIII': '28',
            }
    if roman_numeral in roman_to_decimal:
        return roman_to_decimal[roman_numeral]
def gautama(start,end):
    texts=""
    adhyaya=[]
    text_no=[]
    hymn=[]
    
    for link in range(start,end):
        url=base_url+str(link).zfill(2)+".htm"
        # print(url)
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

        h_tags=[]
        h_tags=soup.find_all('h3')
        for i in h_tags:
            if(i.text=="Footnotes"):
                break
            else:
                # print(i.text)
                info=str(i.text)
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


        # Use regular expression to extract the Roman numeral
        match = re.search(r'(?i)\b([IVXLCDM]+)\b', info)
        adh = match.group(1) if match else None
        # print(adh)
        
        #converting roman to number
        
        
        adh=convert_roman_to_decimal(adh)

        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
#        #Some problems was there in chapter 28 and has been solved
        if link ==92:
            parts = ans.split("Footnotes")
            # Retrieve the first part of the split string
            ans = parts[0].strip()


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
                adhyaya.append(str(adh))
              
                
        else:
            print("numbers and hymns and numbers do not match at PRASNA:"+str(adh))
            
            
        result="Chapter_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
            result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Sacred_Laws_of_Aryas_Part_1_Gautama.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)
    
# Apastamba
def apastamba(start,end):
    texts=""
    khanda=[]
    prasna=[]
    patala=[]
    text_no=[]
    hymn=[]
    
    for link in range(start,end):
        url=base_url+str(link).zfill(2)+".htm"
        # print(url)
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
        if(link==4):
            h_tags=soup.find_all('h3')[2:]
        else:
            h_tags=soup.find_all('h3')
        for i in h_tags:
            # print(i.text)
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
        match_pras = re.search(r'PRASNA\s([\w\d]+)', info,re.IGNORECASE)
        match_pat = re.search(r'patala\s(\d+)', info, re.IGNORECASE)
        match_khan = re.search(r'KHANDA\s(\d+)', info,re.IGNORECASE)

        # Store the extracted values in variables
        pras = match_pras.group(1) if match_pras else None
        pat = match_pat.group(1) if match_pat else None
        khan = match_khan.group(1) if match_khan else None
        
        #converting roman to number
        if pras=='I':
            pras='1'
        elif pras=='II':
            pras='2'
        
          

            
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
                prasna.append(pras)
                khanda.append(khan)
                patala.append(pat)
                
        else:
            print("numbers and hymns and numbers do not match at PRASNA:"+pras+" Patala:"+pat+" Khanda:"+khan)
            
            
        result="Pransa_no"+"\t"+"Patala_no"+"\t"+"Khanda_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,pat_n,khan_n,text_n,sloka_n in zip(prasna,patala,khanda,text_no,hymn):
            result+=prs_n+"\t"+pat_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Sacred_Laws_of_Aryas_Part_1_Apastamba.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)


# Starter Program
start_apas=4
end_apas=65
start_gaut=65
end_gaut=93

apastamba(start_apas,end_apas)
gautama(start_gaut,end_gaut)

    



