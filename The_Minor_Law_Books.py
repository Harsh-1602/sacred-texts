import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe33/sbe33"

def title_of_law(start,end):
    tit=1
    title=[]
    text_no=[]
    hymn=[]
    texts=""
    for link in range(start,end):
        if(link>33):
            tit+=1
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
        if(link==8):
            h_tags=soup.find_all('h3')
        elif(link>33):
            h_tags=soup.find_all('h5')
        else:
            h_tags=soup.find_all('h4')
        for i in h_tags:
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
        
        if(link>33):
            print(ans)
        ans= re.sub(r'\[.*?\]', '', ans)   
        ans=ans.replace("74. One","One")
        ans=ans.replace("*","")
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        if(tit==16):
            tit+=1
            
            
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
                title.append(str(tit))
                
        else:
            print("numbers and hymns and numbers do not match at adhyaya:"+str(tit))
            print(ans)
            
            
        result="Title_of_Law_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for tit_n,text_n,sloka_n in zip(title,text_no,hymn):
            result+=tit_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("The_Minor_Law_Books_Titles_of_Law.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)
    

def quotation(start,end):
    tit=0
    title=[]
    text_no=[]
    hymn=[]
    texts=""
    for link in range(start,end):
        tit+=1
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
#         if(link==8):
        h_tags=soup.find_all('h3')
#         elif(link>33):
#             h_tags=soup.find_all('h5')
#         else:
#             h_tags=soup.find_all('h4')
        for i in h_tags:
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
        
        ans=ans.replace("1, 2.","1-2.")
        ans= re.sub(r'\[.*?\]', '', ans)   
        ans=ans.replace("*","")
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        print(ans)
            
            
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
                title.append(str(tit))
                
        else:
            print("numbers and hymns and numbers do not match at adhyaya:"+str(tit))
            print(ans)
            
            
        result="Chapter_No"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for tit_n,text_n,sloka_n in zip(title,text_no,hymn):
            result+=tit_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("The_Minor_Law_Books_Quotations_of_Narada.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)
    
def frag_of_brih(start,end):
    tit=0
    title=[]
    text_no=[]
    hymn=[]
    texts=""
    for link in range(start,end):
        tit+=1
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
#         if(link==8):
        h_tags=soup.find_all('h3')
#         elif(link>33):
#             h_tags=soup.find_all('h5')
#         else:
#             h_tags=soup.find_all('h4')
        for i in h_tags:
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
        
#         ans=ans.replace("1, 2.","1-2.")
        ans= re.sub(r'\[.*?\]', '', ans)   
        ans=ans.replace("*","")
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
                title.append(str(tit))
                
        else:
            print("numbers and hymns and numbers do not match at adhyaya:"+str(tit))
            print(ans)
            
            
        result="Chapter_No"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
        for tit_n,text_n,sloka_n in zip(title,text_no,hymn):
            result+=tit_n+"\t"+text_n+"\t"+sloka_n+"\n"
        with open("The_Minor_Law_Books_Fragments_of_Brihaspati.tsv", "w", encoding='utf-8') as outfile:
            outfile.write(result)

            
start_title=8
end_title=50
title_of_law(start_title,end_title)
start_quot=51
end_quot=58
quotation(start_quot,end_quot)
start_brih=59
end_brih=86
frag_of_brih(start_brih,end_brih)