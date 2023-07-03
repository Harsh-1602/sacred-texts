# All the text in between the "[]" have been removed 
# There were small errors in chapter 23 and 56 and they have been solved 

import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/sbe07/sbe07"


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
        'XXIX': '29',
        'XXX': '30',
        'XXXI': '31',
        'XXXII': '32',
        'XXXIII': '33',
        'XXXIV': '34',
        'XXXV': '35',
        'XXXVI': '36',
        'XXXVII': '37',
        'XXXVIII': '38',
        'XXXIX': '39',
        'XL': '40',
        'XLI': '41',
        'XLII': '42',
        'XLIII': '43',
        'XLIV': '44',
        'XLV': '45',
        'XLVI': '46',
        'XLVII': '47',
        'XLVIII': '48',
        'XLIX': '49',
        'L': '50',
        'LI': '51',
        'LII': '52',
        'LIII': '53',
        'LIV': '54',
        'LV': '55',
        'LVI': '56',
        'LVII': '57',
        'LVIII': '58',
        'LIX': '59',
        'LX': '60',
        'LXI': '61',
        'LXII': '62',
        'LXIII': '63',
        'LXIV': '64',
        'LXV': '65',
        'LXVI': '66',
        'LXVII': '67',
        'LXVIII': '68',
        'LXIX': '69',
        'LXX': '70',
        'LXXI': '71',
        'LXXII': '72',
        'LXXIII': '73',
        'LXXIV': '74',
        'LXXV': '75',
        'LXXVI': '76',
        'LXXVII': '77',
        'LXXVIII': '78',
        'LXXIX': '79',
        'LXXX': '80',
        'LXXXI': '81',
        'LXXXII': '82',
        'LXXXIII': '83',
        'LXXXIV': '84',
        'LXXXV': '85',
        'LXXXVI': '86',
        'LXXXVII': '87',
        'LXXXVIII': '88',
        'LXXXIX': '89',
        'XC': '90',
        'XCI': '91',
        'XCII': '92',
        'XCIII': '93',
        'XCIV': '94',
        'XCV': '95',
        'XCVI': '96',
        'XCVII': '97',
        'XCVIII': '98',
        'XCIX': '99',
        'C': '100'
    }
    roman_numeral = roman_numeral.replace('.', '')

    if roman_numeral in roman_to_decimal:
        return roman_to_decimal[roman_numeral]
    else:
        return None


# Driver Code

start=3
end=103
texts=""
adhyaya=[]
text_no=[]
hymn=[]

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
    if link==3:
        adh=soup.find('h2').text
    else:
        adh=soup.find('h1').text
    if(adh=='XV[1]'):
        adh='XV'
    adh=convert_roman_to_decimal(adh)
    print(adh)
    
    ans=""
    p_tags=soup.find_all('p')
    for p in p_tags:
        ans=ans+p.text
        
    ans = re.sub(r'\[.*?\]', '', ans) #removing all the data in between "[]"
    ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
    ans=ans.replace(".2 1.",". 21.")# Chpater 21 error solved
    ans=ans.replace("2 7.","; 27.") # Chapter 56 error solved
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
    
    if adh=='13':
            numbers.insert(0,1)
            
    if len(numbers)==len(texts):
        for x in range(len(numbers)):
            text_no.append(str(numbers[x]));
            hymn.append(texts[x])
            adhyaya.append(str(adh))


    else:
        print("numbers and hymns and numbers do not match at Chapter:"+str(adh))
        print(ans)


    result="Chapter_no"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"
    with open("The_Institutes_of_Vishnu.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
    