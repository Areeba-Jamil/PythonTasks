#WordCloud

#import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#select the data for wordcloud
data = pd.read_csv("android-games.csv")

#Checking the Data
data.head()

#Checking NaN Values
data.isna().sum()

#creating text variable
text = " ".join(cat.split()[1] for cat in data.category)

word_cloud = WordCloud(collocations = False, background_color = 'black').generate(text)

#Display Word Cloud
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
