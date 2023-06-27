import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup

def get_text(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, 'html.parser')    
    p_tags = soup.find_all('p')[0]
    lines = p_tags.prettify().split('<br/>')
    lines = [line.replace("<p>", "") for line in lines]
    lines = [line.replace("</p>", "") for line in lines]
    lines = [line.strip() for line in lines]
    result=""
    for line in lines:
        result+=line+"\n"
    return result

base_url="https://www.sacred-texts.com/hin/sbe42/"
r=requests.get(base_url+"index.htm")
r.encoding = 'utf-8'
soup = bs4.BeautifulSoup(r.text, 'html.parser')
# print(soup.text)
text="Hymn_No"+"\t"+"Translation"+"\n"
links=soup.find_all('a')[7:]
for link in links:
    if(link.get("href")!= None):
        new_url=base_url+str(link.get("href"))
#         print(new_url)
        text+=get_text(new_url)+"\n"



with open("Atharva_veda.tsv", "w",encoding='utf-8') as outfile:
    outfile.write(text)