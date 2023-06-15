import bs4
import requests
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString,TAG

base_url = "https://www.sacred-texts.com/hin/sv.htm"
decades = []
def Samaveda_Scrap(url):
    lines=[]
    text=""
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
   
    
    for header in tqdm(soup.find_all('h3')[2:]):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, TAG):
                if nextNode.name == "h3":
                    break
                if (nextNode.get_text()[0] == str(1)):
                    lines = nextNode.prettify().split('<br/>')
                    lines = [line.replace("<p>", "") for line in lines]
                    lines = [line.replace("</p>", "") for line in lines]
                    lines = [line.strip() for line in lines]
                    decades += lines

    return decades

result = Samaveda_Scrap(base_url)
df = pd.DataFrame(decades)
df.to_excel("Samaveda.xlsx")

