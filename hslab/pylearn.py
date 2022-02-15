from os import uname
import requests
import html5lib
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords 

import itertools
from nltk.util import pr
import twint
import nest_asyncio
import datetime
import pandas as pd
nest_asyncio.apply()
import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords 
import spacy
import string
from collections import Counter
from string import punctuation
from collections import Counter
from string import punctuation
from pprint import pprint
from matplotlib import pyplot as plt

url="https://thewire.in/labour/coronavirus-lack-of-work-forces-workers-to-return-to-villages"
r=requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')

title=soup.title
print(title.get_text())
anchor=soup.find_all('a')

l=[]
for link in anchor:
    if(link.get('href') !='#'):
        l.append(link.get('href'))
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
external=soup.find_all(class_='grey-text')
unwanted=external[0].find_all('a')
ans=[]
for i in range(len(external)):
    print(external[i].text.strip())
f = open("text.txt", "a")

for i in range(len(external)):
    f.write(external[i].text.strip())
f.close()

#https://www.thehindu.com/news/cities/Delhi/social-distancing-goes-for-a-toss-in-sadar-bazar/article32987151.ece
#https://www.indiatoday.in/business/story/covid-19-lockdown-delhi-wholesale-markets-open-labour-shortage-broken-demand-supply-chain-closed-border-1684834-2020-06-02
#https://indianexpress.com/article/cities/delhi/delhi-covid-tailors-domestic-helps-job-losses-low-wages-7377292/
#https://thewire.in/labour/coronavirus-lack-of-work-forces-workers-to-return-to-villages
#https://theprint.in/india/in-covid-19-lockdown-many-of-delhis-poor-and-homeless-are-being-forced-to-starve/389790/