from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("mor.csv")

x = df['Year']
# corresponding y axis values
y = df['Dalits']
y2=df['OBC']
y3=df['Muslims']
X_axis=np.arange(len(x))
# plotting the points 
# plt.plot(x, y)
# plt.bar(x,y, color ='green',
#         width = 0.2)

width = 0.25
  

bar1 = plt.bar(X_axis, y, width, color = 'r',label='Dalits')
  

bar2 = plt.bar(X_axis+width, y2, width, color='g',label="Other OBC's")
bar3 = plt.bar(X_axis+width*2, y3, width, color='b',label='Muslims')


plt.xticks(X_axis,x)
# naming the x axis
plt.xlabel('Year',size=20)
# naming the y axis
plt.ylabel('Seats',size=20)
plt.title('Analysis of BSP Lok Sabha Seats',size=24)
# giving a title to my graph


plt.tick_params(axis='x', which='major', labelsize=14.9)
plt.tick_params(axis='y',labelsize=20)
# function to show the plot
plt.legend()
plt.show()
