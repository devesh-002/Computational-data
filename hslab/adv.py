import string
import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords 

import string
from collections import Counter
from string import punctuation
from collections import Counter
from string import punctuation
from pprint import pprint
from nltk.util import pr

from numpy.lib.function_base import percentile
f=open("text.txt","r")
text=f.read()
f.close
import spacy
en = spacy.load("en_core_web_sm")

spacy_tokens=[tok.text.lower() for tok in en.tokenizer(text) ]

import re
spacy_tokens = [re.sub(r'[^\w\s]', '', tok) for tok in spacy_tokens ]
words = [word for word in spacy_tokens if word.isalpha()]

stop_words = set(stopwords.words('english'))
word_list=[word for word in words if word not in stop_words]

snowball = SnowballStemmer('english')
spacy_tokens=[snowball.stem(word) for word in word_list]
# Using counter
word_freq=Counter(spacy_tokens)

x=dict(word_freq)
sorted_x = sorted(x.items(), key=lambda kv: kv[1])
print(sorted_x)
import matplotlib.pyplot as plt

D={'till': 6, 'cloth': 6, 'come': 6, 'sell': 6, 'famili': 6, 'take':7, 'shop': 7, 'due': 7, 'coronavirus': 7, 'custom': 7, 'mani': 7, 'lower': 7, 'rate': 7, 'labour':7, 'job':7, 'use': 7, 'go': 7, 'ask': 7, 'place': 8, 'last': 8, 'employ': 8, 'time': 8, 'week': 9, 'month': 9, 'us': 9, 'nt': 9, 'one': 10, 'get': 10, 'lockdown': 10, 'pay': 10, 'street': 11, 'also': 11, 'year': 11, 'market': 12, 'vendor': 12, 'would': 12, 'earn': 12, 'mcg': 13, 'bazar': 13, 'around': 14, 'delhi': 15, 'work': 16, 'day': 16, 'sadar': 18, 'peopl': 19, 'rs': 22, 'said': 44}
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(rotation=90)
plt.xticks( range(len(D)), list(D.keys()))
print(len(D))
plt.title('2017 UP election result analysis',size=24)
# giving a title to my graph


plt.tick_params(axis='x', which='major', labelsize=14.9)
plt.tick_params(axis='y',labelsize=20)
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x

plt.show()