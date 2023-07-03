import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbr/sbe12/sbe12"


def convert_text_to_number(text):
    numbers = {
        'FIRST': '1',
        'SECOND': '2',
        'THIRD': '3',
        'FOURTH': '4',
        'FIFTH': '5',
        'SIXTH': '6',
        'SEVENTH': '7',
        'EIGHTH': '8',
        'NINTH': '9',
        'TENTH': '10',
        'ELEVENTH': '11',
        'TWELFTH': '12',
        'THIRTEENTH': '13',
        'FOURTEENTH': '14',
        'FIFTEENTH': '15'
        # Add more numbers as needed
    }

    number = numbers.get(text)
    return number if number else text

def get_word_before(string, target_word):
    pattern = r"\b(\w+)\s+" + re.escape(target_word)  # Regex pattern to match the word before the target word
    match = re.search(pattern, string)
    if match:
        return match.group(1)  # Return the word before the target word
    else:
        return None  # Return None if no match is found

# Kanda 1
# Adhyaya 1 missing 
def first_kanda(start,end):

    
    texts=""
    brahmana=[]
    adhyaya=[]
    text_no=[]
    hymn=[]
    prev_adh=""
    
    for link in range(start,end):
        url=base_url+str(link).zfill(2)+".htm"
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
            
            
        khan = 1
        adh = None
        brah = None
        h_tags=[]
        if link==3:
            h_tags=soup.find_all('h3')[1:]
        else:
            h_tags=soup.find_all('h3')
        for i in h_tags:
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
        
        adh=get_word_before(info,"ADHYÂYA")
        if adh== None:
            adh=prev_adh
        brah=get_word_before(info,"BRÂHMANA")
        if link==3:
            adh="FIRST"
            brah="FIRST"
        
        adh=convert_text_to_number(adh)
        brah=convert_text_to_number(brah)


    
        prev_adh=adh
        print(adh,brah)
        
   
            
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
                brahmana.append(brah)
                adhyaya.append(adh)
                
        else:
            print("numbers and hymns and numbers do not match at adhyaya:"+str(adh)+" barh:"+str(brah))
            print(ans)
            
            
        result="Adhyaya_no"+"\t"+"Brahmana_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for adh_n,brah_n,text_n,sloka_n in zip(adhyaya,brahmana,text_no,hymn):
            result+=adh_n+"\t"+brah_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("The_Satapatha_Brahmana_Part_1_Khanda_1.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Kanda 2
# Adhyaya 1 missing 
def second_kanda(start,end):
    
    texts=""
    brahmana=[]
    adhyaya=[]
    text_no=[]
    hymn=[]
    prev_adh=""
    
    for link in range(start,end):
        url=base_url+str(link).zfill(2)+".htm"
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
            
            
        khan = 1
        adh = None
        brah = None
        h_tags=[]
        if link==40:
            h_tags=soup.find_all('h3')[1:]
        else:
            h_tags=soup.find_all('h3')
        for i in h_tags:
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
 
        adh=get_word_before(info,"ADHYÂYA")
        if adh== None:
            adh=prev_adh
        brah=get_word_before(info,"BRÂHMANA")
        if link ==40:
            adh="FIRST"
            brah="FIRST"
        
        adh=convert_text_to_number(adh)
        brah=convert_text_to_number(brah)


    
        prev_adh=adh
        print(adh,brah)
        
   
        ans=ans.replace(" at 8, 11, or 12 ","")
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
        
        if link ==55 or link==40:
            numbers.insert(0,"Preface")
        
        if len(numbers)==len(texts):
            for x in range(len(numbers)):
                text_no.append(str(numbers[x]));
                hymn.append(texts[x])
                brahmana.append(brah)
                adhyaya.append(adh)
                
        else:
            print("numbers and hymns and numbers do not match at adhyaya:"+str(adh)+" barh:"+str(brah))
            print(ans)
            
            
        result="Adhyaya_no"+"\t"+"Brahmana_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for adh_n,brah_n,text_n,sloka_n in zip(adhyaya,brahmana,text_no,hymn):
            result+=adh_n+"\t"+brah_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("The_Satapatha_Brahmana_Part_1_Khanda_2.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Driver Code
start_first=3
end_first=40
first_kanda(start_first,end_first)
start_sec=40
end_sec=64
second_kanda(start_sec,end_sec)
