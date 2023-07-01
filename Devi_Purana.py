# Importing Required Libraries
import requests
import bs4
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup, NavigableString
import re
import numpy as np
base_url="https://www.sacred-texts.com/hin/db/"


# Book1
def bk_01(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("1st","First")
        # print(ans)
        numbers = re.findall(r'(?<!\()\d+(?:-\d+)?(?!\))', ans)
        numbers = [num.rstrip('.,:') for num in numbers]

        # Replace numbers enclosed in parentheses with placeholders
        text_with_placeholders = re.sub(r'\(\d+\)', lambda m: '({})'.format(len(m.group())), ans)

        # Split the text using the modified numbers
        texts = re.split(r'(?<!\()\d+(?:-\d+)?\.?\s?', text_with_placeholders)
        texts = [t.strip() for t in texts if t.strip()]

        # Replace the placeholders back with the original numbers
        numbers = [re.sub(r'\((\d+)\)', r'\1', num) for num in numbers]

        
    #     print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1'and current_adhyaya!='15') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_1.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Book2
#     Some differences in chapter 7 becasue of no text number not  present
def bk_02(book,chapters):

    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("2nd","Second")
#         print(ans)
        numbers = re.findall(r'(?<!\()\d+(?:-\d+)?(?!\))', ans)
        numbers = [num.rstrip('.,:') for num in numbers]

        # Replace numbers enclosed in parentheses with placeholders
        text_with_placeholders = re.sub(r'\(\d+\)', lambda m: '({})'.format(len(m.group())), ans)

        # Split the text using the modified numbers
        texts = re.split(r'(?<!\()\d+(?:-\d+)?\.?\s?', text_with_placeholders)
        texts = [t.strip() for t in texts if t.strip()]

        # Replace the placeholders back with the original numbers
        numbers = [re.sub(r'\((\d+)\)', r'\1', num) for num in numbers]

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1'and current_adhyaya!='15') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                if(current_adhyaya>7):
                    adhyaya.append(str(current_adhyaya+1))
                else:
                    adhyaya.append(str(current_adhyaya))

            else:
                if(current_adhyaya>7):
                    adhyaya.append(str(current_adhyaya+1))
                else:
                    adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_2.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Book 3
# Table present in the book has been removed 
def bk_03(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
        
#  Used to replace numbers in middle of the text with letters ans also the table with " "
        ans=ans.replace("AirFireWaterEarthEther1/21/81/81/81/8Air1/81/21/81/81/8Fire1/81/81/2","")
        ans=ans.replace("AirFireWaterEarthEtherTableFire1/81/81/21/81/8Water1/81/81/81/21/"," ")
        ans=ans.replace("Earth1/81/81/81/81/2Grosselement11111"," ")
        ans=ans.replace("1/81/8Water1/81/81/81/21/8"," ")
        ans = re.sub(r'\([^)]*½\)', '', ans)
        ans=ans.replace("other 4 elements","other four elements")
        
        ans=ans.replace("4 or 18"," four oe one")
        # print(ans)
        
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_3.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
    
        
# Book 4
def bk_04(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_4.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Book 5
def bk_05(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_5.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Book 6
def bk_06(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_6.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
       
# Book 7
def bk_07(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_7.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
       
        
# Book 8
# Some Differences in the Chapter 16 of this book due to some numeric figures missing and have been resolved by adding '1' in the begiginig of the text
def bk_08(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
        # print(ans)
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
        
#  Replacing the numbers specific to this book
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans=ans.replace("12 months","Twelve months")
        ans=ans.replace("These are 29","These are Twenty Nine")
#         ans=ans.replace("O Child","Zero Child")
        ans=ans.replace("0 Child","Zero Child")
        
        ans=ans.replace("(1/10) of the above "," of the above ")
        ans=ans.replace("(1,100) Yoyanas"," Yoyanas")
        ans=ans.replace("2¼ Kotis, 12½ lakhs and 25000 Yojanas"," ")
        
        ans=ans.replace("142,00000","Fourteen Million Two Hundred Thousand")
        ans=ans.replace("21 asterisms","")
        ans=ans.replace("2¼ Naksattras","Two and one fourth Naksattras")
        def replace_numbers(match):
            num = match.group(0)
            if num == '15':
                return 'Fifteen'
            elif num == '90152000':
                return 'Ninety Million One Hundred Fifty-Two Thousand'
            elif num == '36':
                return 'Thirty Six Lakh'
            else:
                return num

        # Replace specific numbers with their English equivalents
        ans = re.sub(r'\b(15|90152000|36)\b', replace_numbers, ans)
#         print(ans)
        
                
#  Spliitng the text into two list of numbers and hymns 
        numbers = re.findall(r'(?<!\()\d+(?:-\d+)?(?!\))', ans)
        numbers = [num.rstrip('.,:') for num in numbers]
        numbers = [num for num in numbers if num != '0']
# Inseting a number in the beginnig of the text of chapter 16 because the chapter does not have a text_no
        for i in range(len(numbers)):
            if numbers[i] == '1-45':
                numbers.insert(i + 1, '1')
        # Replace numbers enclosed in parentheses with placeholders
        text_with_placeholders = re.sub(r'\(\d+\)', lambda m: '({})'.format(len(m.group())), ans)

        # Split the text using the modified numbers
        texts = re.split(r'(?<!\()\d+(?:-\d+)?\.?\s?', text_with_placeholders)
        texts = [t.strip() for t in texts if t.strip()]

        # Replace the placeholders back with the original numbers
        numbers = [re.sub(r'\((\d+)\)', r'\1', num) for num in numbers]

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_8.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Book 9
def bk_09(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
            # print(ans)
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans = ans.replace("(i.e., 1,000 lakhs)", "")
        ans=ans.replace("5000","Five Thousand")
        ans=ans.replace("100,000","One Lakh")
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_9.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)


# Book 10
def bk_10(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
            # print(ans)
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans = ans.replace("(i.e., 1,000 lakhs)", "")
        ans=ans.replace("5000","Five Thousand")
        ans=ans.replace("100,000","One Lakh")
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

        
        # print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_10.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
 
       
# Book 11
# Some Differences in Chapter 11 of this book
def bk_11(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#             print(ans)
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans = ans.replace("(i.e., 1,000 lakhs)", "")
        ans=ans.replace("5000","Five Thousand")
        ans=ans.replace("100,000","One Lakh")
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
# Inserting a number for the text in chapter 11 (no text present in this chapter)
        for i in range(len(numbers)):
            if numbers[i]=='1-43':
                numbers.insert(i+1,'1')
                

        
#         print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))

            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_11.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
       
 #Book 12 


# Book 12
def bk_12(book,chapters):
    texts=""
    adhyaya=[]
    current_adhyaya=0
    text_no=[]
    hymn=[]
    for i in range(chapters):
        text=""
        url=base_url+"bk"+str(book).zfill(2)+"ch"+str(i+1).zfill(2)+".htm"
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup=bs4.BeautifulSoup(req.text,'html.parser')
    #     print(soup)
        for a_tag in soup.find_all('a'):
                a_tag.decompose()
        for x in soup.find_all():
    # fetching text from tag and remove whitespaces
            if len(x.get_text(strip=True)) == 0:
                # Remove empty tag
                x.extract()
        ans=""
        p_tags=soup.find_all('p')
        for p in p_tags[3:]:
            ans+=p.text
#             print(ans)
#  Replacing numbers in the middle of the text with words
        ans=ans.replace("18,000", "Eighteen Thousand")
        ans=ans.replace("18000","Eighteen Thousand")
        ans = re.sub(r'\b(\d+)(?:th|nd|st|rd)\b', '', ans)
        ans = re.sub(r'\([^)]*\d[^)]*\)', '', ans)# this removes all the text in the braces if it contains a letter
        ans = ans.replace("(i.e., 1,000 lakhs)", "")
        ans=ans.replace("5000","Five Thousand")
        ans=ans.replace("100,000","One Lakh")
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


        
#         print(str(len(texts))+"  "+str(len(numbers)))
        for num in numbers:
            text_no.append(str(num))
            if (num == '1') or (len(num)>0 and num[0]=='1' and num[1]=='-'):
                current_adhyaya += 1
                adhyaya.append(str(current_adhyaya))
            else:
                adhyaya.append(str(current_adhyaya))
        for text in texts:
            hymn.append(text)

    result="Chapter"+"\t"+"Text_no"+"\t"+"Hymn"+"\n"
    for adh_n,text_n,sloka_n in zip(adhyaya,text_no,hymn):
        result+=adh_n+"\t"+text_n+"\t"+sloka_n+"\n"


    with open("Devi_Purana_Book_12.tsv", "w", encoding='utf-8') as outfile:
        outfile.write(result)
       


index_url=base_url+"index.htm"
req = requests.get(index_url)
req.encoding = 'utf-8'
soup=bs4.BeautifulSoup(req.text,'html.parser')
book=[]
for i in soup.find_all('h3'):
    count=0
    for j in i.next_siblings:
        if j.name=='h3':
            break
        elif j.name=='a' and len(j.text)>0 :
            count=count+1
    book.append(count)
    
for i in tqdm(range(12)):
    x=i+1
    if(x==1):
        bk_01(x,book[i])
    if(x==2):
        bk_02(x,book[i])
    if(x==3):
        bk_03(x,book[i])
    if(x==4):
        bk_04(x,book[i])
    if(x==5):
        bk_05(x,book[i])
    if(x==6):
        bk_06(x,book[i])
    if(x==7):
        bk_07(x,book[i])
    if(x==8):
        bk_08(x,book[i])
    if(x==9):
        bk_09(x,book[i])
    if(x==10):
        bk_10(x,book[i])
    if(x==11):
        bk_11(x,book[i])
    if(x==12):
        bk_12(x,book[i])


                      


       

           