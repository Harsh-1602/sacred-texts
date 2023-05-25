import bs4
import requests
from tqdm import tqdm
import pandas as pd

base_url = "https://sacred-texts.com/hin/rvsan/"

# first_hymn = 1001

# last_hymn = 1191

def get_sanskrit_sentences(url):
    # get the html for hin as a string
    r = requests.get(url)
    r.encoding = 'utf-8'
    # extract body of the html
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    br_tags = soup.find_all('br')

    # The transliteration starts from the second half of the <br> tags
    start = len(br_tags) // 2
    transliterations = []

    for br in br_tags[start:]:
        # Get the text just before each <br> tag
        transliteration = br.previous_sibling
        # Remove leading/trailing white space
        transliteration = transliteration.strip()
        transliterations.append(transliteration)

    return transliterations

def get_sanskrit_text(url):
    # get the html for hin as a string
    r = requests.get(url)
    r.encoding = 'utf-8'
    # extract body of the html
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    br_tags = soup.find_all('br')

    # The transliteration starts from the second half of the <br> tags
    start = len(br_tags) // 2
    transliterations = []

    for br in br_tags[1:start+1]:
        # Get the text just before each <br> tag
        transliteration = br.previous_sibling
        # Remove leading/trailing white space
        transliteration = transliteration.strip()
        transliterations.append(transliteration)

    return transliterations

def get_english_sentences(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, 'html.parser')    
    p_tags = soup.find_all('p')
    hymn = p_tags[1]
    lines = hymn.prettify().split('<br/>')
    lines = [line.replace("<p>", "") for line in lines]
    lines = [line.replace("</p>", "") for line in lines]
    lines = [line.strip() for line in lines]
    return lines


def get_hymn(hymn_number):
    # convert hymn_number to string with 5 digits
    hymn_number = str(hymn_number).zfill(5)
    url_hin = base_url + "rv" + hymn_number + ".htm"
    url_eng = base_url.replace("/rvsan/", "/rigveda/") + "rv" + str(hymn_number) + ".htm"
    # get the html for skt
    skt_result = get_sanskrit_sentences(url_hin)[1:]
    # get the html for eng
    eng_result = get_english_sentences(url_eng)
    # get the html for skt
    skt_text_result=get_sanskrit_text(url_hin)[1:]
    if len(skt_result) != len(eng_result):
        print("Error: Number of Sanskrit and English sentences do not match")
        return
    if len(skt_text_result) != len(eng_result):
        print("Error: Number of Sanskrit and English sentences do not match")
        return
    result = ""
    for skt_text,skt, eng in zip(skt_text_result,skt_result, eng_result):
        result += skt_text + "\t"+ skt + "\t" + eng + "\n"
    return result

result_string = "Sanskit Text" + "\t" +"Sanskrit Transliteration" +"\t"+ "Translation"+"\n"
for i in range(1,11):
    url_book=base_url+"rvi"+str(i).zfill(2)+".htm"
    req = requests.get(url_book)
    req.encoding = 'utf-8'
    # extract body of the html
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    br_tags = soup.find_all('br')
    start = len(br_tags) 
    first_hymn=i*1000+1
    last_hymn=i*1000+start
    for hymn_number in tqdm(range(first_hymn, last_hymn)):
        result = get_hymn(hymn_number)
        if result:
            result_string += result + "\n"

with open("test1.tsv", "w",encoding='utf-8') as outfile:
    outfile.write(result_string)

df = pd.read_csv("test1.tsv", sep='\t')
