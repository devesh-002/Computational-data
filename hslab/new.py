import seaborn as sns
import pandas as janna
import sklearn
import numpy as np
import pandas as pd
# df1 = janna.read_csv("coal.csv")
# df2 = janna.read_csv("HDI.csv")
# # print(merged_df)
# column1 = df1["Production00"]
# column2 = df2["HDI00"]
# df00 = df1
# df00.pop('Production99')
# df00.pop('States')
# df00['HDI00'] = column2
# df99 = janna.read_csv("coal.csv")
# df99.pop('Production00')
# df99.pop('States')
# df99['HDI99'] = df2["HDI99"]
# # print(df99)
# y = df00['Production00']
# x = df00['HDI00']
# plt.title('Correlation of 2007-08')
# print(df99.corr())
# print(df00.corr())
# plt.scatter(x, y)
# plt.plot(np.unique(x),
#          np.poly1d(np.polyfit(x, y, 1))
#          (np.unique(x)), color='red')

# plt.xlabel('HDI')
# plt.ylabel('Production')
# plt.savefig("hs.png")
# ans = sns.heatmap(df00, annot=True, fmt='.2g', cmap='coolwarm')
# figure = ans.get_figure()
# figure.savefig('svm_conf.png', dpi=400)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

D={'till': 6, 'cloth': 6, 'come': 6, 'sell': 6, 'famili': 6, 'take':7, 'shop': 7, 'due': 7, 'coronavirus': 7, 'custom': 7, 'mani': 7, 'lower': 7, 'rate': 7, 'labour':7, 'job':7, 'use': 7, 'go': 7, 'ask': 7, 'place': 8, 'last': 8, 'employ': 8, 'time': 8, 'week': 9, 'month': 9, 'us': 9, 'nt': 9, 'one': 10, 'get': 10, 'lockdown': 10, 'pay': 10, 'street': 11, 'also': 11, 'year': 11, 'market': 12, 'vendor': 12, 'would': 12, 'earn': 12, 'mcg': 13, 'bazar': 13, 'around': 14, 'delhi': 15, 'work': 16, 'day': 16, 'sadar': 18, 'peopl': 19, 'rs': 22, 'said': 44}
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(rotation=90)
plt.xticks( range(len(D)), list(D.keys()))
print(len(D))
plt.title('Test analysis',size=24)
# giving a title to my graph


plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y',labelsize=20)
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x

plt.show()
df = pd.read_csv(r"f.csv", encoding ="latin-1")
 
comment_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in df.CONTENT:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()