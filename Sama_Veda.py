import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np

base_url = "https://www.sacred-texts.com/hin/sv.htm"

def Samaveda_Scrap(url):
    hymn=[]
    parts=[]
    decades=[]
    books=[]
    text_no=[]
    chapters=[]
    text=""
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    for a_tag in soup.find_all('a'):
                a_tag.decompose()
    for x in soup.find_all():
# fetching text from tag and remove whitespaces
        if len(x.get_text(strip=True)) == 0:
            # Remove empty tag
            x.extract()
   
#     br_tags = soup.find_all('br')
#     for br_tag in br_tags:
#         br_tag.decompose()
#     print(soup)
    part=""
    book=""
    chapter=""
    decade=""
    for p in soup.find_all('p'):
        if p.text=="Om. Glory to the Samaveda! To Lord Ganesa glory! Om.":
            p.decompose()
    part_tag=soup.find_all('h1')[3:]
    for pa in part_tag:
        part=pa.text
        print(part)
        for bk in pa.next_siblings:
            if bk.name=='h1':
                print("here")
                break
            if bk.name =='h2':
                book=bk.text
                print(book)
                for chap in bk.next_siblings:
#                     print(chap.text)
                    if chap.name=='h2':
                        break
                    if chap.name=='h3':
                        chapter=chap.text
                        print(chapter)
                        for dec in chap.next_siblings:
                            ans=""
                            if dec.name=='h3':
                                break
                            if dec.name=='p':
                                ans=dec.get_text(separator=' ')
                                ans=ans.strip()
                            print(ans)
                            ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
#                             ans=ans.split('\n')
                    #  Spliitng the text into two list of numbers and hymns 
                            matches = re.findall(r'(\d+)\.\s+(.*)', ans)

                            # Split the matches into numbers and texts
                            numbers = [match[0] for match in matches]
                            texts = [match[1] for match in matches]
                            print(numbers)
                            print(texts)
                            if(len(numbers)==len(texts)):
                                for x in range(len(numbers)):
                                    text_no.append(str(numbers[x]))
                                    parts.append(part)
                                    books.append(book)
                                    decades.append(decade)
                                    chapters.append(chapter)
                                    hymn.append(texts[x])

                            if dec.name=='h4':
                                print(decade)
                                decade=dec.text
                                ans=""
                            
    result="Part"+"\t+""Book"+"\t"+"Chapter"+"\t"+"Decade"+"\t"+"Text"+"\t"+"Hymn"+"\n"
    for pt_n,bk_n,chap_n,dec_n,text_n,sloka_n in zip(parts,books,chapters,decades,text_no,hymn):
        result+=pt_n+"\t"+bk_n+"\t"+chap_n+"\t"+dec_n+"\t"+text_n+"\t"+sloka_n+"\n"
    with open("Sama_Veda.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)                    
                
        

    

Samaveda_Scrap(base_url)

