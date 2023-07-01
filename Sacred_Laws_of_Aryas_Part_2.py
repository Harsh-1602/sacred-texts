# Importing Required Libraries
import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe14/sbe14"


# Prasna 6 adhyaya 5 also included in this file only, It belongs to "PARISISHTA" 
# Prasna 1, Adhyaya-11, Kandika-20 is missing from the text(has been removed because of the enormous amount of numbers in it )
def baudhayana(start,end):

    texts=""
    kandika=[]
    prasna=[]
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
        pras = None
        pat = None
        khan = None
        h_tags=[]
        
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
        # print(info)
#         Geeting the values of Prasna , Patala ,Khanda from the H3 tag
        match_pras = re.search(r'PRASNA\s(\w+)', info,re.IGNORECASE)
        match_adh = re.search(r'ADHYÂYA\s(\d+)', info,re.IGNORECASE)
        match_kand = re.search(r'KANDIKÂ\s(\d+)', info,re.IGNORECASE)

        # Store the extracted values in variables
        pras = match_pras.group(1) if match_pras else None
        adh= match_adh.group(1) if match_adh else None
        kand = match_kand.group(1) if match_kand else None
        
        # print(pras,adh,kand)
        
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
          
        if kand== None:
            kand='-'
            
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
#         Handling for the missing text number in prasna 3 , adhyaya 1
        if pras=='3' and adh=='1' and kand=='-':
            numbers.insert(0,1)
        
        if len(numbers)==len(texts):
            for x in range(len(numbers)):
                text_no.append(str(numbers[x]));
                hymn.append(texts[x])
                prasna.append(pras)
                kandika.append(kand)
                adhyaya.append(adh)
                
        else:
            print("numbers and hymns and numbers do not match at PRASNA:"+pras+" Patala:"+pat+" Khanda:"+khan)
            
            
        result="Pransa_no"+"\t"+"Adhyaya_no"+"\t"+"Kandika_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for prs_n,pat_n,khan_n,text_n,sloka_n in zip(prasna,adhyaya,kandika,text_no,hymn):
            result+=prs_n+"\t"+pat_n+"\t"+khan_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Sacred_Laws_of_Aryas_Part_2_Baudhayana.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)


# Vashistha
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
        'XXIX':'29',
        'XXX':'30',
            }
    if roman_numeral in roman_to_decimal:
        return roman_to_decimal[roman_numeral]
def vasistha(start,end):
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
    
        #converting roman to number
        
        adh=convert_roman_to_decimal(adh)

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
                adhyaya.append(str(adh))
              
                
        else:
            print("numbers and hymns and numbers do not match at PRASNA:"+str(adh))
            
            
        result="Chapter_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
            result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("Sacred_Laws_of_Aryas_Part_2_Vaisistha.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

# Starter Code
start_baudh=34
end_baudh=92
start_vasis=4
end_vasis=34

vasistha(start_vasis,end_vasis)

baudhayana(start_baudh,end_baudh)

    


